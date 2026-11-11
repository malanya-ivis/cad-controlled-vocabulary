"""Evaluate authored vocabulary-search cases against annotated JSON records.

This is a local record-filter demonstration, not CAD recognition or an RAG
implementation. Missing annotations never prove absent physical geometry.
Uses only the Python standard library.
"""
from pathlib import Path
import hashlib
import itertools
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
VAULT = ROOT / "mold-cad-vocabulary"
EXAMPLES = VAULT / "45_Part_Examples"
RECORDS = ["Simple_CAD_Feature_Records.json", "Final_Selected_Feature_Records.json",
           "Supplemental_Feature_Records.json"]


def concepts(feature):
    out = {a["concept_id"] for a in feature.get("concept_assignments", [])}
    if feature.get("concept_id"):
        out.add(feature["concept_id"])
    return out


def attributes(feature):
    values = {**feature.get("properties", {}), **feature.get("attributes", {})}
    end = values.get("end_condition")
    if end is not None and "termination" not in values:
        values["termination"] = "through" if end == "through_via_entrance_form" else end
    return values


def satisfies(feature, criterion, include_candidates=False):
    assigned = concepts(feature)
    if include_candidates:
        assigned |= set(feature.get("candidate_concept_ids", []))
    required = set(criterion.get("all_concept_ids", []))
    if criterion.get("concept_id"):
        required.add(criterion["concept_id"])
    if not required.issubset(assigned):
        return False
    values = attributes(feature)
    for key, wanted in criterion.get("attributes", {}).items():
        if key not in values or values[key] != wanted:
            return False
    for key, wanted in criterion.get("quantities", {}).items():
        actual = values.get(key)
        if not isinstance(actual, dict):
            return False
        if actual.get("value") != wanted["value"] or actual.get("unit") != wanted["unit"]:
            return False
    return True


def part_scope(parts, case):
    out = []
    for part in parts:
        synthetic = part.get("origin") == "synthetic_teaching_model"
        scope = case.get("origin_scope", "supplied_only")
        if scope == "supplied_only" and synthetic:
            continue
        if scope == "synthetic_only" and not synthetic:
            continue
        if case.get("part_scope") and part["part_id"] not in case["part_scope"]:
            continue
        out.append(part)
    return out


def filter_features(parts, case):
    matched, unknown, keys = [], [], []
    counts = {}
    for part in parts:
        groups = [[f for f in part["features"] if satisfies(f,c)] for c in case["criteria"]]
        if all(groups):
            matched.append(part["part_id"])
            ids = sorted({f["feature_id"] for g in groups for f in g})
            keys.extend([[part["part_id"],fid] for fid in ids])
            counts[part["part_id"]] = len(ids)
        else:
            candidates = [[f for f in part["features"] if satisfies(f,c,True)]
                          for c in case["criteria"]]
            if all(candidates):
                unknown.append(part["part_id"])
    return {"status":"supported_draft_matches" if matched else
                     "unknown" if unknown else "no_supported_record",
            "match_parts":sorted(matched), "unknown_parts":sorted(unknown),
            "matched_feature_keys":sorted(keys), "matched_occurrence_counts":counts}


def relation_endpoints(relation):
    return relation.get("subject",relation.get("source_feature_id")), \
           relation.get("object",relation.get("target_feature_id"))


def filter_relations(parts, case):
    matched, unknown, evidence = [], [], []
    for part in parts:
        fs = {f["feature_id"]:f for f in part["features"]}
        sources = {fid for fid,f in fs.items() if case["source_concept"] in concepts(f)}
        targets = {fid for fid,f in fs.items() if case["target_concept"] in concepts(f)}
        possible = {(a,b) for a,b in itertools.product(sources,targets) if a != b}
        if not possible:
            continue
        found = False
        relations = part.get("relations",[]) + part.get("relation_assessments",[])
        for relation in relations:
            a,b = relation_endpoints(relation)
            if relation["predicate"] != case["predicate"] or (a,b) not in possible:
                continue
            # Existing positive relation records omit result. Explicit unknown
            # assessments stay unknown and never become False.
            value = relation.get("result", True)
            if value == case.get("result",True) and value in (True,False):
                found = True
                evidence.append({"part_id":part["part_id"],"source":a,"target":b,
                                 "predicate":case["predicate"],"result":value})
        (matched if found else unknown).append(part["part_id"])
    return {"status":"supported_draft_matches" if matched else
                     "unknown" if unknown else "no_supported_record",
            "match_parts":sorted(matched),"unknown_parts":sorted(unknown),
            "matched_relations":evidence}


def check_required_evidence(parts, case):
    eligible = []
    for part in parts:
        ids = set(case.get("candidate_concept_ids",[]))
        if not ids or any(concepts(f) & ids for f in part["features"]):
            eligible.append(part)
    key = case["required_evidence"]
    available = []
    for part in eligible:
        if key == "physical_unit":
            known = part.get("physical_unit") not in (None,"unknown")
        elif key == "reference_pull_direction":
            known = part.get("reference_pull_direction") not in (None,"unknown")
        elif key == "documented_purpose":
            known = any(f.get("purpose") == case["purpose"] and
                        f.get("purpose_evidence",{}).get("kind") in
                        ("drawing","design_specification","designer_statement","analysis")
                        for f in part["features"])
        else:
            raise ValueError(f"Unknown evidence requirement: {key}")
        if known:
            available.append(part["part_id"])
    # Evidence presence only: no mm conversion, release analysis or function
    # inference is implemented. A changed corpus needs its cases reviewed.
    return {"status":"requires_case_review" if available else "insufficient_evidence",
            "match_parts":[],"unknown_parts":sorted(p["part_id"] for p in eligible),
            "required_evidence":key,"records_with_required_evidence":sorted(available)}


def main():
    parts, provenance = [], []
    for name in RECORDS:
        path = EXAMPLES / name
        obj = json.loads(path.read_text())
        for p in obj["parts"]:
            p["record_file"] = name
            parts.append(p)
        provenance.append({"file":name,"sha256":hashlib.sha256(path.read_bytes()).hexdigest()})
    cases_path = EXAMPLES / "Search_Verification_Cases.json"
    spec = json.loads(cases_path.read_text())
    results = []
    dispatch = {"features":filter_features,"relation":filter_relations,
                "required_evidence":check_required_evidence}
    for case in spec["cases"]:
        actual = dispatch[case["mode"]](part_scope(parts,case),case)
        expected = case["expected"]
        checks = {k:actual.get(k)==value for k,value in expected.items()}
        detail = [{"part_id":p["part_id"],"record_file":p["record_file"],
                   "origin":p.get("origin","user_supplied_stl"),"evidence":p.get("evidence",[])}
                  for p in parts if p["part_id"] in actual["match_parts"]]
        results.append({"case_id":case["case_id"],"question_ja":case["question_ja"],
                        "actual":actual,"expected":expected,"checks":checks,
                        "passed":all(checks.values()),"supporting_records":detail})
    output = {"date":"2026-10-07","method":"structured filter over manual draft records",
              "limits":["No CAD geometry recognition, database or RAG evaluation",
                        "Passing means expected record behavior, not approved shape definitions",
                        "No supported record is not physical absence",
                        "Default corpus excludes synthetic teaching models"],
              "record_provenance":provenance,
              "case_spec_sha256":hashlib.sha256(cases_path.read_bytes()).hexdigest(),
              "case_count":len(results),"passed_count":sum(r["passed"] for r in results),
              "results":results}
    (EXAMPLES / "Search_Verification_Results.json").write_text(json.dumps(output,ensure_ascii=False,indent=2)+"\n")
    for r in results:
        print(r["case_id"],"PASS" if r["passed"] else "FAIL",r["actual"]["status"],
              ",".join(r["actual"]["match_parts"]))
    print(f"{output['passed_count']}/{output['case_count']} record-behavior cases passed")
    return 0 if output["passed_count"] == output["case_count"] else 1


if __name__ == "__main__":
    sys.exit(main())
