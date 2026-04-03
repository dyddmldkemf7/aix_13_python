s="abc"
s2 = 'abc'
s3 = """abc"""
s4 = '''abc
강나루 건너서
밀밭길을 
구름에 달 가듯이 
가는 나그네
'''
print(s4)
#s2= 'Tom's Bear' 이렇게하면 오류
s2= "Tom's Bear" # 작은따옴표 중복으로 사용하면 오류로
print(s2)
s2='Tom\'s Bear' #왼쪽의 백슬러시는 오른쪽의 따옴표 무력화
print(s2)
s5 = "홍길동"
s6 = "안녕하세요"
print(s5+s6) # 두개의 변수를 이음
print(s5+" "+s6) # 두개의 변수를 이을대의 공백
#print(s5 + 5) #오류 이후코드 동작 안함, 문자열 + 숫자 X 
print("홍길동"*3)
print("홍길동 "*3)
print( "홍길동"[0]) # 홍 , 0은 왼쪽에서 첫번째
print( "홍길동"[1]) # 길
print( "홍길동"[2]) # 동
print(s5[0]) # 홍 
print(s5[1]) # 길
print(s5[2]) # 동
print(s5[-1]) # 동 , -는 오른쪽 끝에서 첫번째
print(s5[-2]) # 길
print(s5[-3]) # 홍

