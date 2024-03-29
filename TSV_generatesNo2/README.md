#  TSV_generates100.py(以下Pythonプログラム)仕様　Windows版
##  目次

・必要な人

・必要条件

・具体的な仕様

・ダウンロード方法

・使い方

・制約条件

## 必要な人
このPythonプログラムを必要とする人は以下の通り。  

    ・1万個のサンプルデータが欲しい。  
    ・TSVファイルを100個複製したい。  
    ・Exelファイルを取得したい。

##  必要条件
このPythonプログラムを使用するにあたって必要なものは以下の通り。 

    ・Python3.7.4  
    ・Windows(Macの手法は記載していない)  
    ・78.2MBの空き容量  

##  具体的な仕様  
このPythonプログラムの具体的な仕様は以下のようになっている。  
*・タグ(ログID・日時・経度・緯度を表示した行)を含め10001行のデータとなる。  
・TSVファイル1つの大きさは782KB。100個生成すると78.2MBとなる。  
・1つ1つのデータはすべてランダムな要素で構成されており、他のデータと重複する可能性は低い。*  

#### ログID  

*・計32文字のランダムな文字列で構成されている。  
・32文字はそれぞれ8,4,4,4,12文字で区切られ、それぞれの区切りを”‐”で表現している。  
・その32文字は大文字半角英字(A～Z)と半角数字(0～9)で構成されている。*  
	
	例：J9RD08ND-4BVF-VZTL-EVCW-8I8SOQL4UMME

#### 日時  
	
*・年月日と時間分秒までを2000年1月1日～2019年1月1日までの範囲の中でランダムに表示する。  
・年月日に関してはそれぞれ”‐”で区切る。  
・時間分秒に関してはそれぞれ”：”で区切る。*  

	例：2006-05-11T19:56:25Z
       
#### 経度・緯度  

*・それぞれ以下の範囲内でランダムに表示される。  
・経度：34.5～35.5、緯度：134～139   
・小数点以下に関しては6桁目まで表示される。*  

	例：経度35.487487		緯度137.919052



##  ダウンロード方法
このPythonプログラムのダウンロード方法は以下の通り。  
・URL(https://github.com/824ty/job) をクリックでアクセスし、下図の手順でURLを取得する。  
<img src = "https://github.com/824ty/job/blob/master/TSV_generatesNo2/image/clone.png" width = 400px>  
・「Windows」キー　 + 「x」キーを同時に押すと下図のメニューが表示される。 
  その中の「コマンドプロンプト」をクリックし、起動する。  
<img src = "https://github.com/824ty/job/blob/master/TSV_generatesNo2/image/cmdimage.png" width = 200px>  
  
・「cd Desktop」と入力し続けて保存したいファイル場所まで移動する。以下は例である。  

    例　デスクトップからnewfile内に移動する。
    cd Desktop/newfile

(大量のファイルを生成するのでDesktop以外の場所を推奨する)  
・保存したい場所まで移動したら下記の順に入力する。  

    git init  
    git clone コピーしたURL   

・下図のような表記がされれば正常に入力したコマンドが作動している。  
<img src = "https://github.com/824ty/job/blob/master/TSV_generatesNo2/image/gitclone.png" width = 400px>  

・実際に下図のようにjobファイルがコピーされ、内部にPythonプログラムがあればダウンロード完了となる。  
<img src = "https://github.com/824ty/job/blob/master/TSV_generatesNo2/image/downloadfile.png" width = 400px>  


##  使い方
・コマンドプロンプトを起動し、上記の保存した場所まで移動したのち、下記を入力する。  

    Python TSV_generates100.py  

・下図のように保存したファイル内に「NO.○○text.tsv」が100個生成されていれば正常に動作している。  
<img src = "https://github.com/824ty/job/blob/master/TSV_generatesNo2/image/tsvfile.png" width = 400px>  

##  制約条件
このPythonプログラムの制約条件は以下の通り。  

        ・100個以上のファイルの作成はできない。※1  
        ・同一ファイル内外でデータが重複してしまう可能性がある。  
        ・データ日付、経度、緯度に関して上記の通り表示範囲に制限がある。※2   
        ・TSVファイルの保存場所を指定することはできない。※3  

作成したTSVファイルをExelで表示する(※4)場合の制約事項は以下の通り。  

        ・経度緯度に関して小数点以下が「0」で終了する場合、0を表示しないため桁数が統一でなくなる。※5  

※1　ファイル名に「作成したファイル数」要素を盛り込んでいる為、同じプログラムを作成しようとする場合はまたNo.1～100の作成することになり上書きという形になってしまう。プログラムのwhile文内の「ファイルを何個作成するか」を書き換えることで変更可能。  
※2　プログラムを書き換えることで変更は可能。  
※3　100個のTSVファイルの生成場所は「TSV_generate100.py」を保存したディレクトリと同じ場所になる。  
必ず100ファイル分78.2MBの空き容量があることを確認してから実行すること。不足の場合、正常にプログラムが動作しない可能性がある。  
※4　TSVファイルをExelで表示したい場合は、新しいExelファイルを立ち上げ、既存のTSVファイルを開かず、Exelのセル上にドラッグ&ドロップする。  
※5　小数点以下の桁数を統一したい場合は、1万行データを範囲選択し、[ホーム] → [数値] →[小数点以下の表示桁数を増やす(減らす)]で調節可能。  
