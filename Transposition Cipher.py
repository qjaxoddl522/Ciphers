def keyorder(key):
    key = key.upper()
    order = list(sorted(key))  # 키를 대문자로 변환하고 알파벳 순으로 정렬하여 순서를 구함
    return list(map(lambda x: order.index(x), key))  # 각 문자의 정렬된 순서를 리스트로 반환

# 모드 구별
ENC = 0  # 암호화 모드
DEC = 1  # 복호화 모드

def transposition(msg, key, mode):
    order = keyorder(key)  # 주어진 키에 대한 순서를 구함
    result = ""  # 결과를 저장할 변수 초기화

    if mode == ENC:  # 암호화 모드
        ls = ["" for _ in range(len(key))]  # 키의 길이만큼 빈 문자열로 초기화된 리스트 생성
        for i in range(len(key)):
            loc = i
            while loc < len(msg):  # 현재 위치가 평문 길이보다 작으면 저장
                ls[i] += msg[loc]  # 문자를 해당 위치의 문자열에 추가
                loc += len(key)  # 다음 위치로 이동
        for i in range(len(order)):  # 정해진 순서대로 쪼갠 문자열을 재배치하여 결과에 추가
            result += ls[order.index(i)]

    if mode == DEC:  # 복호화 모드
        block = len(msg) // len(key)  # 블록의 길이는 메시지 길이를 키의 길이로 나눈 몫
        m = len(msg) % len(key)  # 나머지는 m
        ls = ["" for _ in range(len(key))]  # 키의 길이만큼 빈 문자열로 초기화된 리스트 생성
        line = 0
        for i in range(len(key)):
            if order.index(i) < m:  # 나머지 길이보다 작은 순서의 경우
                ls[i] += msg[line:line+block+1]  # 블록의 길이 + 1 만큼 문자를 저장
                line += block + 1  # 다음 라인으로 이동
            else:
                ls[i] += msg[line:line+block]  # 블록의 길이만큼 문자를 저장
                line += block  # 다음 라인으로 이동

        for i in range(block+1):  # 블록의 길이 + 1 만큼 반복
            for j in order:
                if len(ls[j]) > i:  # 해당 위치의 문자열이 존재하는 경우
                    result += ls[j][i]  # 결과에 추가

    return result

original = "I_LIKE_PYTHON345"
key = "HACKERS"

print(f"원 문장: {original}")
encrypted = transposition(original, key, ENC)
print(f"암호화 문장: {encrypted}")
decrypted = transposition(encrypted, key, DEC)
print(f"복호화 문장: {decrypted}")
