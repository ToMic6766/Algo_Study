people_number, area = map(int,input().split())
assum_number = people_number * area

article_peope_number = list(map(int, input().split()))
for i in article_peope_number:
    print(i - assum_number, end=' ')