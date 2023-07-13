set1 = {"name", "jung", "gang", "name"}
# set 은 데이터의 순서와 상관없이 저장되므로 출력 순서도 알 수 없음
# 2번 입력한 name은 1번만 출력됨
print(set1) 
set1.add("plan")
for data in set1: # set 을 순회
    print(data)