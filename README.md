# job/TSV_generates100.pyの仕様書

## [目的]<h2>
「TSV＿generate100.py」を使用する人は以下のケースを想定している。<br>

*・1万個のサンプルデータが欲しい。<br>
・TSVファイルを100個複製したい。<br>
・Exelファイルを取得したい。<br>*

## [結果]<h2>
「TSV＿generate100.py」を実行することで以下の処理を自動的に行う。<br>

	「ログID・日時・経度・緯度」の4要素で構成されたデータ1万行をTSVファイル(※)として100個出力する。

※Tab Separated Values : 文字や文字列の間にタブ記号を挿入してデータを区切り管理するファイル。<br>
　　生成されるファイル名は「No.〇text.tsv」。(〇はファイル生成数。)<br>

## [仕様]<h2>
「TSV_generate100.py」を実行することで上記のプログラムが実行される。<br>
具体的な仕様は以下の通り。<br>
	
*・タグ(ログID・日時・経度・緯度を表示した行)を含め10001行のデータとなる。<br>
・100個のファイルの生成場所は「TSV_generate100.py」を保存したディレクトリと同じ場所になる。<br>
・1つ1つのデータはすべてランダムな要素で構成されており、他のデータと重複する可能性は低い。*<br>

#### ログID<h4>

*・計32文字のランダムな文字列で構成されている。<br>
・32文字はそれぞれ8,4,4,4,12文字で区切られ、それぞれの区切りを”‐”で表現している。<br>
・その32文字は大文字半角英字(A～Z)と半角数字(0～9)で構成されている。*<br>
	
	例：J9RD08ND-4BVF-VZTL-EVCW-8I8SOQL4UMME

#### 日時<h4>
	
*・年月日と時間分秒までを2000年1月1日～2019年1月1日までの範囲の中でランダムに表示する。<br>
・年月日に関してはそれぞれ”‐”で区切る。<br>
・時間分秒に関してはそれぞれ”：”で区切る。*<br>

	例2006-05-11T19:56:25Z
       
#### 経度・緯度<h4>

*・それぞれ以下の範囲内でランダムに表示される。<br>
・経度：34.5～35.5、緯度：134～139 <br>
・小数点以下に関しては6桁目まで表示される。*<br>

	例　経度35.487487		緯度137.919052

## [制約事項]<h2>
TSVファイルの制約事項は以下の通り。<br>

*・プログラムのwhile文内の「ファイルを何個作成するか」を書き換えない限り100個以上のファイルの作成はできない。ファイル名に「作成したファイル数」要素を盛り込んでいる為、同じプログラムを作成しようとする場合はまたNo.1～100の作成することになり上書きという形になってしまう。<br>
・同一ファイル内外でデータが重複してしまう可能性がある。<br>
・データ日付、経度、緯度に関して上記の通り表示範囲に制限がある。変更は可能。*<br>

作成したTSVファイルをExelで表示する場合の制約事項は以下の通り。<br>

*・経度緯度に関して小数点以下が「0」で終了する場合、0を表示しないため桁数が統一でなくなる。*

