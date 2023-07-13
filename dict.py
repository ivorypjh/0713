# dict 생성
"""
dic = {}
# dict에 데이터 추가(upsert)
dic["name"] = "lee"
dic["age"] = "12"
dic["address"] = "si"
print(dic)
print(dic["name"])
print(dic.get("age", "199"))
# print(dic["score", '0']) 존재하지 않는 key이므로 에러
# 존재하지 않는 key를 사용했으므로 대신 2번째 매개변수를 리턴
print(dic.get("score", "0")) 
for key in dic: # dict 순회하기
    print(key, dic[key]) # 순회에 key 를 사용
"""


# 2차원 배열 대신 dict 활용하기
t1 = ["park", "lee"]
t2 = ["sa", "sin"]

league = [t1, t2] # list 의 list
# list 는 index를 이용해 접근하고 tuple 은 key 를 이용해서 접근

# enumerate 는 인덱스와 데이터를 튜플로 리턴
# 
# index를 활용하기에 league에 팀이 늘어나면 대응을 하지 못함.
for index, team in enumerate(league):
    print(index)
    print(team)

# 2차원 배열 대신 dict 사용
t1 = ["park", "lee"]
t2 = ["sa", "sin"]

league = [{"team" : "첫번째", "data" : t1}, {"team" : "두번째", "data" : t2}]

for dic in league:
    print(dic.get("team"), end=" : ")
    for name in dic.get("data"):
        print(name, end="\t")
    print()