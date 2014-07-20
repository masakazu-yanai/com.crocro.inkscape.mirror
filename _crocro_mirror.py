#!/usr/bin/env python
# coding:utf-8

'''
Copyright (C) 2014 Masakazu yanai, yanai@crocro.com
http://crocro.com/

crocro_mirror.inx
「Inkscape」用のエクステンションです。選択したオブジェクトの、
X座標0の位置を基準にした、鏡像コピーを作成します。

本スクリプトは、「Inkscape」用の基本的なエクステンションを利用しています。
そのため、GPLライセンス下で公開されます。

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
'''

import inkex, simpletransform
from copy import deepcopy
_ = str

class CroCro_Mirror(inkex.Effect):
	def __init__(self):
		inkex.Effect.__init__(self)

	def effect(self):
		# 選択要素がなければ終了
		if len(self.selected) <= 0: return

		# 親ノード
		parentnode = self.current_layer

		# 選択要素を取得
		# グループ内のtransformを展開
		sel = self.selected
		# inkex.debug('>> ' + ' '.join(_(v) for v in sel))

		# 変形マトリクスの作成
		transformation = 'scale(-1, 1)'
		transform = simpletransform.parseTransform(transformation)

		# 複製と変形マトリクスの適用
		for id, node in sel.iteritems():
			childNode = deepcopy(node)
			parentnode.append(childNode)
			simpletransform.applyTransformToNode(transform, childNode)

# インスタンスの初期化と実行
if __name__ == '__main__':
	e = CroCro_Mirror()
	e.affect()

