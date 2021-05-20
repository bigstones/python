SyntaxError: Non-ASCII character '\xec' in file make_data.py on line 14, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details

라는 에러가 떠서 찾아보니 한글 인코딩이 안돼서 문제가 생긴것...


해결방법

		# -*- coding: utf-8 -*-
        
        
        
        
라는 문구를 한글 사용하기 이전에 넣어주면 문제 없이 돌아간다


혹시나 euc-kr 를 사용한다면 다음 코드를 넣어주면 된다

		# -*- coding: euc-kr -*-