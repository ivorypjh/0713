from collections import Counter

data = [1, 3, 1, 5, 2, 3, 6, 4, 7, 2, 3, 6, 4, 6, 3, 1, 2, 8, 3, 9]
# 데이터를 가지고 데이터의 갯수 파악
cnt = Counter(data)
# dict로 변환해서 전체 데이터의 갯수 파악
print(dict(cnt))
# 1가지 데이터를 선택해서 파악
print(cnt[3]) # 5
# 상위 3개만 추출
print(cnt.most_common(3))

# 튜플 목록
data = [("가", 2), ("나", 3), ("가", 5), ("다", 1), ("다", 3), ("다", 1)]
count = Counter()
# 데이터의 합계 구하기
for name, cnt in data:
    count[name] += cnt
print(count)

# 데이터가 등장한 횟수 구하기
count = Counter()
for name, cnt in data:
    count[name] += 1
print(count)