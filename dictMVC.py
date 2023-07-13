# dict 를 이용한 MVC

# DTO 역할을 수행하는 클래스 생성 - 최근에 더 권장되는 방식
# 클래스 내에서 수정이 발생하면 출력하는 부분에도 영향을 미치는게 문제점
# 대신 dict 와 다르게 code sense 의 기능이 정상적으로 작동함.
class DTO:
    def __init__(self, name = "no", age = "0") -> None:
        self.name = name
        self.age = age
# 클래스를 활용한 DTO 데이터 목록 생성
dtoData = [DTO("lee", "12"), DTO("park", "15")]

# 이름과 나이 출력
for data in dtoData:
    print(data.name, data.age)

# dict 를 사용해서 목록 생성
# dict 내의 데이터를 수정해도 출력 부분은 수정이 필요하지 않음
dictData = [{"name" : "lee", "age" : "12"}, {"name" : "park", "age" :"15"}]
for data in dictData:
    for key in data:
        print(key, ":", data[key])