---
category: part_example
status: mesh_based_draft
part_id: STL-7145
physical_unit: unknown
source_sha256: 42500e4e55059a3530716c149250a2818edf9e68f5bde5741d92407325a38039
---
# STL 7145：外側の丸みと外観に見えない空間

![[7145_sections.png]]

## 外側を見る

上面と側面の間には丸い移行部分があります。X=0とY=0の断面でも曲がった輪郭が見えるため、[[Fillet|フィレット]]の形状例（F01）として記録します。STLは平面の集まりなので、正確な曲面やCADの作成コマンドまでは確認できません。

## 内側を見る

外観図では上面と側面が見えます。断面を見ると、−Z側に開いた[[Internal_Void|内部の空間]]と、その間に材料が残った仕切りが分かります（F02）。Z=0.0125の断面には複数の空間が見えます。

この断面だけで、それぞれの空間が全体で独立しているとは決めません。仕切りを[[Rib|リブ]]と呼ぶかも、形の記述範囲を確認してから決めます。「補強」「反り対策」という用途は不明です。

> 上面の周りに丸い移行部分がある。部品の内側には下側に開いた空間と仕切りがある。

## 検索に必要な記録

外観の丸みと内部空間は別の特徴として保存します。内部空間については `opening_direction: -Z` を保存できますが、独立した空洞の数と空間同士の接続は `unknown` です。見えていないものを「ない」と判断しません。

[[Shape_Comparison_Examples]] で、丸みと面取りの断面を比較できます。

## 根拠と範囲

元ファイル：[7145.stl](/home/malanya/projects/cad-structure-search/data/final_selected/stl/7145.stl)。値はすべて **input_units（入力座標の単位）** です。物理単位と金型としての用途は未確認です。同番号のSTEPファイルはありますが、STLとの単位・倍率の対応は確認していません。

[[selected_sections.json]] と [[inventory.json]] に形状の観察・元ファイルの記録があります。8972の線による確認は [[8972_ray_observations.json]] に保存しました。検索用の記述は [[Final_Selected_Feature_Records.json]]、全体の案内は [[Final_Selected_Dataset_Study]] です。用語への対応は草案です。元データは変更していません。
