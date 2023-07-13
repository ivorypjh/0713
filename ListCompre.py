li = list(range(13))
# li의 모든 데이터를 제곱한 list를 생성

result = []
# 일반적인 반복문을 사용하는 방식
for index in li:
    result.append(index * index)
print(result)

# map 함수를 이용하는 방법
# li에서 데이터를 가져와서 lamda 부분에 변환 함수를 적용
# map 함수를 사용하면 sequential 타입이기 때문에 list로 만듦
result = list(map(lambda x : x * x, li))
print(result)

# list comprehension 이용
# [연산식 순회할문장] 형식
result = [i*i for i in li]
print(result)

# for 2개 사용하기(for가 여러개여도 작동)
li1 = ["1", "2", "3"]
li2 = ["a", "b", "c"]
result = [x + y for x in li1 for y in li2]
print(result)

# for 와 if 사용 가능 - filtering
name = ["asdf", "lee", "gi", "x"]
# 글자 수가 홀수인 데이터만 추출
result = list(filter(lambda x : len(x) % 2 == 1, name)) # 필터 안에 조건 작성
print(result) # lee, x
# 함수인 filter 를 사용하지 않았기 때문에 더 빠름
result = [x for x in name if len(x) % 2 == 1] # list 내부에 조건 작성
print(result) 
result = [x for x in name if len(x) % 2 == 1 and len(x) > 2]
# result = [x for x in name if len(x) % 2 == 1 if len(x) > 2] 위와 동일
print(result) # lee
# 길이가 짝수이면 2번 출력
# if 와 else 를 사용할 때는 if가 앞으로 감
result = [x if len(x) % 2 == 1 else x + " " + x for x in name]
print(result)