#-*-coding: UTF-8-*-
# 0から10000までの素数の配列を返す
i=1
sosu=[2]	#素数のリスト
c=0
while i <5000:	#奇数だけ考えるので5000
	for j in sosu:
		if (2*i+1) % j != 0:	#i番目の奇数がそれより小さい素数で割り切れるか
			c += 1				#それらの素数で割り切れなかった回数をカウント
		else:
			break				#割り切れたものが一つでもあれば素数じゃない
	if c == len(sosu):			#素数なら割れなかった回数とリストの要素数が同じ
		sosu.append(2*i+1)	#リストに追加
	i += 1
	c = 0
print sosu