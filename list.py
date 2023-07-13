#list 의 메서드 활용
li1 = ["part", "park", "List", "lee", "ob"]
print(li1)

li1.sort() # 오름차순 정렬
print(li1)
li1.sort(reverse=True) # 내림차순 정렬
print(li1)
sortResult = sorted(li1) # 정렬한 결과를 리턴
print(sortResult)
li1.sort(key = str.upper) # 영어 대소문자 구분없이 정렬
print(li1)