#댄동회원관리 
names=['홍','김','박']
print(names[0]) # 홍
print(names[1:]) # 김 박
n=names[1:] #복사본 생성 n= 김 박
names[1] = '이' # 홍 이 박 
print(names)
print(names[1:][0]) #[이 박] -> 이
print(n[0]) # 김

# 파이썬은 배열없고 리스트만 있음
arr = [[1,2,3],[4,5,6]]
print(arr[0]) # [1,2,3]
print(arr[1]) # [4,5,6]
print(arr[0][1]) #2 앞에께 행 번호, 뒤에게 열 번호 행열

a = [10,20,30]
b = [40,50,60]
print(a+b)
print(a*3)
print(f"홍길동의길이={len("홍길동")}")
print(len(a+b))
print(len(a*3))
