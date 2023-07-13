import sys

print(sys.stdin.encoding) # utf-8
"""
message = "종호"
# 문자열을 바이트 코드로 변환
print(message.encode()) # b'\xec\xa2\x85\xed\x98\xb8'
print(message.encode().decode()) # 종호
print(ord("A"), ord("박")) # 65 48149
"""

message = 'abcde'
print(message[::])
print(message[:-1:]) # 가장 마지막을 제외하고 출력
print(message[::-1]) # 역순으로 출력. edcba.

print("message 는 %s"%message)
print(message.count("a", 0, -1)) # 1


problem = "GEADGGECGCCGDEGEGCCGCCGER"
# 문자열에서 GCCG 의 위치 전부 출력하기
# 1번 포함된 문자는 빼고 찾기(GCCGCCG 는 앞만 정답)
li = [0]
index = 0
cnt = 0

for index in range(len(problem)):
    subPosition = problem.find("GCCG", index, -1)
    if li[cnt] != subPosition:
        if subPosition - li[cnt] != 3:
            li.append(subPosition)
            cnt += 1        
print(li)

del(li[cnt])

if problem.find("GCCG") != 0:
    del(li[0])

print(li)