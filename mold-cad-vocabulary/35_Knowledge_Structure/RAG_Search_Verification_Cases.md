---
category: search_design
status: record_filter_demonstration
updated: 2026-10-07
---
# 課題3：どんな記録があれば検索できるか

19問について、必要な項目と期待する結果を作りました。既存の手動JSON記録と[[Supplemental_Feature_Records.json]]を読み、条件に合う記録を絞る小さなスクリプトで確認しました。19問とも期待する記録上の動きと一致しました。

これは形状を自動認識する検証や、DB・RAGの実装評価ではありません。用語の意味や手動ラベルが正しいことを証明する結果でもありません。課題3で必要なデータ項目と、不明なときの回答を確認する例です。

## 対象と検索の単位

- 提供モデル：従来8件＋今回3件＝11件の詳細な草案記録。
- 教材：閉鎖空洞と開口空間の2件。通常の検索から除き、Q11・Q12だけで使います。
- 同じ特徴に条件をそろえる場合：Q04は一つのSlotに貫通状態と入口の段を要求します。
- 同じ部品に別々の特徴を要求する場合：Q07は同じ部品にFilletとInternal Voidがあるかを調べます。
- 同じ領域の複数説明：Q12は一つのfeature_idに二つの概念があっても一度だけ数えます。

数値だけで形状の全体を再検査していません。検索結果は元記録の部品ID・特徴IDと根拠に戻れるようにします。

## 問題、必要な項目、期待する結果

| ID | 探したいこと | 必要な項目・関係 | 今の記録で期待する結果 |
|---|---|---|---|
| Q01 | 座ぐり付きの穴 | CounterboreとHole、entrance_form_of | counterboreのF-02→F-01 |
| Q02 | 皿ざぐり付きの穴 | CountersinkとHole、entrance_form_of | countersinkのF-02→F-01 |
| Q03 | 止まりのポケット | Pocket、termination=blind | rectpocketのF-01、8972のF02～F06 |
| Q04 | 段付きの貫通長穴 | 同じSlotにthroughとentrance_step=true | 8972のF01 |
| Q05 | 底が一部残る凹部 | Pocket、floor_state=partial | 8972のF07 |
| Q06 | +Z側へ開く内部空間 | Internal Void、opening_direction=+Z | 4423のF01 |
| Q07 | 丸い移行と内部空間がある同じ部品 | 同じpart_idにMC-008とMC-013 | 7145。別部品の記録を合わせない |
| Q08 | input_unitsで厚さ3のリブ | Rib、厚さの値・単位 | ribのF01、rib_crossのF-01・F-02。mmではない |
| Q09 | ボスの草案記録がある提供モデル | MC-007の割当 | bossとfillet_boss。一般定義の確認は続ける |
| Q10 | fillet_bossから確認済みのFilletを探す | 候補と割当の区別 | unknown。F02は丸い環状凸部で、Fillet割当は未確定 |
| Q11 | 教材の閉じた内部空洞 | 教材を明示、enclosure=enclosed | TEACH-enclosedのF01 |
| Q12 | 同じ領域にPocketとInternal Voidがある教材 | 同じfeature_idに二つの割当 | TEACH-openのF01を1回数える |
| Q13 | 1400の穴が内部でつながるか | connects_toの幾何根拠 | unknown。intersectsの観察だけから決めない |
| Q14 | 5mm未満の肉厚を探せるか | 物理単位、値、測定位置・方法 | 単位の根拠不足。input_unitsをmmに変えない |
| Q15 | 冷却に使う経路を探せるか | 当該特徴の用途と設計資料 | 用途の根拠不足。穴をCooling Channelに自動変換しない |
| Q16 | 反り対策のリブを探せるか | reduce_warpageの設計・解析根拠 | 用途の根拠不足。Ribという名称だけから目的を付けない |
| Q17 | +Z方向のアンダーカットを探せるか | 指定した抜き方向と確認結果 | 抜き方向の根拠不足。凹部を一律にUndercutにしない |
| Q18 | counterboreに皿ざぐりの記録があるか | 対象部品を限定したMC-003の記録 | 対応記録なし。物理形状全体の不存在とは別 |
| Q19 | 1400の穴同士が交差しないと確定できるか | 全体検査によるintersects=false | unknown。選択断面で未観察という記録をfalseにしない |

## DB・RAGへ移すとき分かったこと

1. **文章から条件を作る。** 例えば「段付きの貫通長穴」を、MC-005、through、entrance_stepという同一特徴の条件にします。名称の対応と意味は概念ノートを参照します。
2. **値と関係で絞る。** 寸法、単位、開口状態、特徴同士の関係は、記録された項目を使います。文の似ている順だけではQ04やQ13の条件を保証できません。
3. **根拠と状態を回答する。** 結果の部品・特徴ID、断面・測定の参照を返します。用途、方向、単位が不明なら、不明な項目を説明します。
4. **教材と実データを区別する。** `origin`で分け、教材を実金型の検索結果に混ぜません。

追加で、[[CAD_Geometry_Representation_and_Evidence]]に形状データの種類、幾何参照、要求値と実測値、根拠状態を分ける項目案を整理しました。現在のSTL検索例にはSTEPの面・エッジ参照や3D公差注記は含まれていません。

既存二JSONの項目名には違いがあります。Simpleの`properties/end_condition`とFinalの`attributes/termination`は、今回の読み取り処理だけで対応させました。元記録を置き換えてはいません。`through_via_entrance_form`は、主穴が入口形状を通じて貫通するという記録として保持し、検索時のterminationではthroughに対応させます。

## 結果の意味と再確認

| 結果 | 意味 |
|---|---|
| supported_draft_matches | 条件に合う草案記録がある。専門家の承認済みという意味ではない |
| unknown | 候補割当、接続・交差などの確認が足りない |
| insufficient_evidence | 単位、方向、用途等の必要な根拠がない |
| no_supported_record | 対象記録に対応する注釈がない。部品にその形が絶対にないという意味ではない |

問題と期待値は[[Search_Verification_Cases.json]]、実行結果は[[Search_Verification_Results.json]]です。結果ファイルには参照した記録と問題ファイルのSHA-256も保存しました。

プロジェクトのルートから再確認するコマンド：

```sh
python3 tools/evaluate_vocab_search_cases.py
```

データの定義や割当を変更したときは、期待結果も根拠とともに見直します。資料の判断範囲は[[Claim_Evidence_Matrix]]、特徴の関係は[[Feature_Relations]]を参照してください。
