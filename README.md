com.crocro.inkscape.center
==========================

「Inkscape」用のエクステンションです。選択したオブジェクトの、X座標0の位置を基準にした、鏡像コピーを作成します。


## 使い方

1. 「Inkscape/share/extensions/」配下に、「～.inx」「～.py」のファイルをコピーします。
2. 「Inkscape」を起動している場合は、いったん終了してから再度起動します。
3. オブジェクトを選択します。
4. メニューの［エクステンション］→［CroCro］→［CroCro Center］を選択します。
5. X座標0の位置を基準にした、鏡像コピーが作成されます。


## 開発の背景

2014年夏コミ用（日曜日 西か-05b るてんのお部屋）のゲームのキャラクターを作成するために開発しました。初「Inkscape」エクステンション、初 Python でしたので、試行錯誤でコードを書いています。

キャラクターの部品を作成する際に、左右対象に配置するために作成しました。


## 「Inkscape」のエクステンションについて

「Inkscape」エクステンションについての日本語情報が少なかったので、ここに雑多な情報をまとめておきます。

基本的には「Inkscape/share/extensions/」配下の他のエクステンションを見ながら、真似をするとよいです。


## メニュー用エクステンションの仕組み

### 1. ファイル

ここでは、メニューに機能を追加するエクステンションについて書きます。

エクステンションを追加する場合は、「Inkscape/share/extensions/」配下に以下の2つのファイルを作成します。

* 「～.inx」
* 「～.py」

2つのファイルの名前は同じにしておいた方がよいです。たとえば「hoge.inx」「hoge.py」のような形にするとよいです。


### 2. 「～.inx」ファイル

「～.inx」が設定ファイルになります。この設定ファイルに書いた内容で、メニューのフォルダ名や、その中のサブメニュー名が決まります。また、実行時に読み込むファイルもここで指定します。

また、「～.inx」ファイルの書き方次第では、ダイアログを表示させることも可能です。ダイアログに入力した内容や、選択したメニューは、実行ファイルである「～.py」から読み取ることができます。

ダイアログの値を読み取る方法については、「Inkscape/share/extensions/」配下の他のエクステンションを見ながら、真似をするとよいです。


### 3. 「～.py」ファイル

「～.py」が実行ファイルになります。Python でプログラムを書きます。このファイルでは、「inkex.Effect」を継承したクラスを作ります。以下が、テンプレートです。

	class MyClass(inkex.Effect):
		def __init__(self):
			inkex.Effect.__init__(self)
	
		def effect(self):
			# ここに処理を書く
	
	e = MyClass()
	e.affect()	# 実行開始

「inkex」は、エクステンションのフォルダに入っている「inkex.py」です。この「inkex.Effect」が、「Inkscape」エクステンションの基本的なクラスになります。このクラスを継承することで、エクステンションとして実行可能な処理を書けます。

「__init__」では、クラスの初期化が行われます。ダイアログを表示して、各種設定を受け取る場合は、ここで値を取得して、変数に格納します。「Inkscpae」に付いているほとんどのエクステンションはダイアログを使っているので、適当なエクステンションを参考にするとよいでしょう。

「effect」が、実際に処理を行う関数です。ここに処理を書きます。この「effect」は、「affect」を実行した際に呼び出されます（「effect」と「affect」は違います。同じ関数ではありません）。

注意すべき点は、「Inkscpae」のエクステンションは「Inkscape」を直接操作するわけではないことです。

エクステンションを実行すると、「Inkscpae」は、SVGや選択中のオブジェクト、現在のレイヤーなどの情報をまとめたオブジェクトを生成します。そして、エクステンションを実行します。

エクステンション側では、このオブジェクト（selfから参照可能）を基にしてSVGを編集します。その処理が終わったあと、「Inkscape」は、編集中のSVGを書き換えます。

そのため、エクステンションから「Inkscpae」を直接操作することはできません。


### 4. 便利なツール

「Inkscpae」のエクステンションでは、SVGを直接編集すると書きました。しかし、それはかなり荷が重いです。そこで、「Inkscpae」のエクステンションには、SVGを編集するのに役立つモジュールが入っています。

* Python modules for extensions - Inkscape Wiki
	* <http://wiki.inkscape.org/wiki/index.php/Python_modules_for_extensions>
* Yusai Works | モジュール関連
	* <http://yworks.webcrow.jp/inkscape_extension/module.html>

以下、私が使ってみたモジュールを掲載します。

* simpletransform.py
	* マトリクスの変形関係を扱ってくれます。

また「inkex.Effect」を継承したクラス「PathModifier」が収録されている「pathmodifier.py」も強力です。

たとえば「expandGroups」では、グループがネストしていて、それぞれ変形マトリクスがあるような複雑なグループを、きれいに展開できます。


## 参考リンク

* Inkscape メモ - カビパン男と私
	* <http://www.kabipan.com/computer/inkscape/>
	* 日本語での「Inkscape」解説。エクステンションの仕組みが書いてあり、理解を助けてくれます。

* Yusai Works | モジュール関連
	* <http://yworks.webcrow.jp/inkscape_extension/module.html>
	* 「Inkscape」のエクステンション用モジュールの関数解説。日本語なので助かります。

* Category:Extensions - Inkscape Wiki
	* <http://wiki.inkscape.org/wiki/index.php/Category:Extensions>
	* 公式のエクステンション開発向けドキュメントです。
