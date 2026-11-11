---
category: comparative_study
status: draft
---
# 実例で比べる形の違い

用語を選ぶときは、外観の印象だけでなく、輪郭・壁・底・断面を確認します。下はこのvaultの用語候補を実例に対応させた草案です。

| 比較 | 実例 | この例での判断の手掛かり |
|---|---|---|
| [[Counterbore|座ぐり]]／[[Countersink|皿ざぐり]] | [[CAD_Counterbore_Example]]／[[CAD_Countersink_Example]] | 座ぐりは円筒形の広い入口と平らな肩。皿ざぐりは入口に向かって円すい状に広がる |
| [[Pocket|ポケット]]／[[Slot|長穴]] | [[CAD_Rectangular_Pocket_Example]]／[[CAD_8972_Slot_and_Recesses]] | 前者は矩形の底と壁。後者のF01は一定方向に長く、両端が丸い。段があっても下まで貫通する |
| [[Fillet|フィレット]]／[[Chamfer|面取り]] | [[CAD_7145_Fillet_and_Internal_Structure]]／下の単純な面取り例 | 前者の断面は曲がった移行。後者は斜めの直線でつなぐ移行 |
| [[Rib|リブ]]／[[Boss|ボス]] | [[CAD_Rib_Boss_Comparison]] | 同じ外形寸法で、板状に長く続く突起と局所的な円柱状突起を比較。Bossの一般定義は草案 |

![[7145_sections.png]]
![[simple_chamfer_sections.png]]

面取り例の元データ：[chamfer.stl](/home/malanya/projects/cad-structure-search/data/simple_CAD_dataset/chamfer.stl)。輪郭と面の向きに基づく形の判断です。CADの作成コマンドは不明です。

## 用語と属性を分ける

- 「貫通」「止まり」「段付き」は特徴の状態として記録します。状態ごとに新しい概念ノートを作る必要はありません。
- 長穴の入口に段があっても、円筒形の座ぐりとは同じにしません。
- 一つの凹部で底が一部残り、一部が開いている場合もあります。8972の右中の凹部がその例です。底の有無を二択だけで記録すると情報が落ちます。
- 同じ領域にポケットと内部空間という説明を付ける場合は、同じ特徴IDを使います。二つの用語が同義語になるわけではありません。

[[CAD_Rib_Boss_Comparison]]にリブ／ボスの対になる提供STLを追加しました。[[CAD_Cross_Rib_Example]]は交差の例です。どの例でも用途を形から決めません。

[[CAD_Fillet_Boss_Name_Check]]は、丸い環状凸部をファイル名だけでFilletにできない例です。[[CAD_Enclosed_Open_Void_Teaching]]は明示した教材で空洞の開閉を比べます。教材と実物の確認範囲は[[Targeted_CAD_Gap_Examples]]で区別します。
