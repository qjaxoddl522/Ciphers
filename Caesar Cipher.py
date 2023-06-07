def maketable(key): #테이블 생성기
    #알파뱃 수보다 많은경우 나머지로 계산
    while key>=26:
        key = key//26
        
    #키값을 적용한 숫자테이블
    keytable = tuple(map(lambda x: (x+key if x+key<26 else x+key-26), range(26)))

    #숫자테이블 토대로 대문자와 소문자 치환 딕셔너리 생성
    keydict = dict(map(lambda x: (chr(x+65), chr(keytable[x]+65)), range(26)))
    keydict.update(dict(map(lambda x: (chr(x+97), chr(keytable[x]+97)), range(26))))
 
    return keydict

def caesar(msg, key, mode): #모드: 0암호화, 1복호화
    key2index = maketable(key)
    result = ""
    
    if mode == 0: #암호화
        for i in msg: #한 글자씩 검사
            #암호화 대상이면 바꾸고 아닐 시 그대로 저장
            if i in key2index.keys(): 
                result += key2index.get(i)
            else:
                result += i
        return result

    if mode == 1: #복호화
        #뒤집기
        index2key = {j:i for i,j in key2index.items()}
        for i in msg:
            if i in index2key.keys():
                result += index2key.get(i)
            else:
                result += i
        return result

original = "Do you like python3?"
key = 4

print(f"원 문장: {original}")
encoded = caesar(original, key, 0)
print(f"암호화 문장: {encoded}")
decoded = caesar(encoded, key, 1)
print(f"복호화 문장: {decoded}")
