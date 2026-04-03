# a=[5,1,3]
# print(min(a))
# print(max(a))
# print(sum(a))
# print('avg=',sum(a)/len(a))

# a.sort()
# print('sorted',a)
# r=reversed(a) #iterator 반환
# for v in r:
#     print(v)

# a=[1,3,5]
# b=[i*10 for i in a]
# print(b)

#짝수만추출
# a= [i for i in range(10) if i%2==0]
# print(a)
# print(list("12345")) #['1','2','3','4','5']
# print("-".join(a)) # 1-2-3-4-5
# a=['1','2','3'] #ok
# a=[1,2,3] #오류
# a =[str(n)for n in a]
# print("-".join(a)) #1-2-3

# 짝수홀수 변환
a=range(5)
#[참일때 값 if 조건식 else 거짓일때값 for 변수 in 자료구조]
b=['짝'if n%2==0 else'홀' for n in a]
print(b)