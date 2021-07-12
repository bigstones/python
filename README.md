# python
파이썬 메소드에 대해 설명하는 공간입니다.

## python 버전관리

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

버전이 안맞아서 라이브러리가 실행이 안될 때

레포지토리 추가

    sudo add-apt-repository ppa:deadsnakes/ppa
레포지토리 업데이트

    sudo apt-get update
python설치

    sudo apt-get install python[version]
    sudo apt install python3-pip
버전 설정 1단계

    sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python[version1] 1
    sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python[version2] 2
버전 설정
    
    sudo update-alternatives --config python3
</div>
</details>

## pip 버전관리

<details>
<summary>접기/펼치기</summary>
<div markdown="1">
    
pip 패키지 설치 리스트 조회

    pip list

pip 패키지 설치 리스트 requirements.txt 파일로 생성

    pip freeze > requirements.txt
    
</div>
</details>

## 주석

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

jupyter notebook에서 파이썬 라이브러리를 실행하다보면 정확하지 않은 메소드에 '?' 값을 붙여 실행했을 때 그 메소드의 설명을 볼 수 있다

우리가 함수를 만들 때도 그와같은 설정을 할 수 있는데 함수를 만들 때 다음과같이 선언하면 그런 설명을 붙일 수 있다.

    def sample_function(a):
        '''
        Args
          a: 매개변수 설명
        Returns
          반환값 설명
        '''

</div>
</details>

## string

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

string을 통해 검색기능을 구현하면서 필요했던 라이브러리들이다

    ''.strip()
    ''.replace(' ', '')

</div>
</details>

## numpy

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

[중복제거](https://github.com/bigstones/python/blob/master/code/numpy/%EC%A4%91%EB%B3%B5%EC%A0%9C%EA%B1%B0.py)
    
    import numpy as np
    np.unique([변수])

</div>
</details>
    
## pandas

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

    import pandas as pd
    pd.mean #평균
    pd.std #표준편차
    pd.median #중앙값
    pd.var #분산

</div>
</details>

## sqlalchemy

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

    or_() # or연산
    and_() # and연산

</div>
</details>

## Crypto

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

[암호화](https://github.com/bigstones/python/blob/master/%5B99%5D%EB%82%B4%EB%B6%80_pycryptodome.py)

pycryptodome이 설치돼있어야 합니당

pip install pycryptodome으로 설치할 수 있습니다

    import base64
    import hashlib

    from Crypto import Random 
    from Crypto.Cipher import AES
    from Crypto.Protocol.KDF import PBKDF2

    random = 'sample_random'
    salt = 'sample_salt'


    BS = 16
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
    unpad = lambda s: s[0:-s[-1]]
    key = PBKDF2(random, salt, 64, 1000)[:32]

    def get_private_key(random):
        kdf = PBKDF2(random, salt, 64, 1000)
        key = kdf[:32]
        return key

    def encrypt(raw, random):
        private_key = get_private_key(random)
        raw = pad(raw).encode('utf-8')
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(private_key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(enc, random):
        private_key = get_private_key(random)
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(private_key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(enc[16:]))

</div>
</details>

## 기타


[pip install 로 패키지 설치 후 인식이 안될 때](https://github.com/bigstones/python/blob/master/module%20%EC%9D%B8%EC%8B%9D%EC%9D%B4%20%EC%95%88%EB%90%A0%20%EB%95%8C)

[python 버전 수동설정](https://github.com/bigstones/python/blob/master/python%20%EB%B2%84%EC%A0%84%20%EC%98%A4%EB%A5%98%20%EB%82%AC%EC%9D%84%20%EB%95%8C)

[matplotlib 한글화](https://github.com/bigstones/python/blob/master/Matplotlib%20%ED%95%9C%EA%B8%80%ED%99%94.ipynb)

[DB에서 DB로 전송](https://github.com/bigstones/python/blob/master/db_to_db.py)
