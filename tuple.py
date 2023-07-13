recordData = ("abcd", "park", "lee", 3) # 튜플 생성
print(recordData[0]) # 인덱싱 가능
print(recordData)
# 튜플을 수정하려 하므로 에러
# recordData[0] = "jung" 

'''
# list 와 tuple 인 unpacking 이 가능함
data1, data2, data3, data4 = recordData
print(data3) # lee

# * 을 사용하면 나머지 모두를 list로 생성함
# 나머지를 모두 가지게 되므로 * 은 1번만 사용해야 함
# 데이터가 1개일 때 * 을 사용하는 것에 주의. list 로 만들어버림
*etc, datas = recordData
print(etc) # ['abcd', 'park', 'lee']

# swap : 2개의 데이터 값을 교환
a = 1; b = 2
a, b = b, a
print(b, a) # 1, 2
'''

data = [("park", "019"), ("lee", "010")]
for row in data:
    # 출력을 위해서는 구조를 기억해줘야 함
    print(row[0]) # 이름만 출력하기

# column 에 이름을 사용하는 튜플
from collections import namedtuple
# 자료 구조를 생성해서 튜플의 각 컬럼에 이름을 만듦
# 컬럼에 name phone 이라는 이름을 붙임
 # 앞의 person 은 별 의미 없음. 뒤의 이름들이 중요
personData = namedtuple("person", "name phone") 
people = [personData("lee", "011"), personData("park", "010")]
for person in people:
    print(person.phone)
