파이썬 내장함수 zip은 마치 옷의 zipper처럼 두 그룹의 데이터를 서로 엮어주는 파이썬의 내장함수입니다

함수는 iterable한 객체를 인자로 받고 각 객체가 담고 있는 원소를 튜플의 형태로 차례로 접근할 수 있는 iterator를 반환합니다

예를들면

	asdf = [a,s,d,f]
	qwer = [q,w,e,r]

	for pair in zip(asdf, qwer)
	    print(pair)
    
    

	('a','q')
	('s','w')
	('d','e')
	('f','r')

같이 나옵니다

zip 함수로 넘기는 인자의 길이가 다르면 가장 짧은 인자를 기준으로 데이터가 엮이고, 나머지는 버려지기 때문에 주의해야합니다


dict 함수와 함께 사용하는 방법도 있습니다

	dict(zip(asdf,qwer))

	{'a':'q', 's':'w', 'd':'e', 'f':'r'}
