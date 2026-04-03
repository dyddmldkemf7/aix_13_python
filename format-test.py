# 구구단 출력 -3단
# 3*1=3
# 3*2=6
dan =3
print("{}*{}={}".format(dan,1,dan*1))
print("{}*{:5d}={}".format(dan,1,dan*1))
print("{}*{:05d}={}".format(dan,1,dan*1))

print("헬로 python 프로그래밍".upper())
a = """
    헬로 파이썬 프로그래밍      
"""
print(a.strip()+"/") # .strip은 공백제거 +"/"은 양쪽 공백 제거 
print("안녕 123".isalnum()) # .isalnum 문자열이 알파벳과 숫자로만 구성하는 함수인데 안에 공백이 있어 False
print("abc abc programming".find("bc")) # 1 = 첫번째 BC는 1의 자리부터 시작한다는 뜻
print("abc abc programming".find("bc",2)) # 5 = 두번째 bc는 5의 자리부터 시작한다는 뜻
print("abc abc programming".find("bc",6)) # -1 = 찾을 숫자가 없다는 뜻임

a = "안녕하세요"
print("안녕" in a) # True
print("잘자" in a) # False



b = "홍,김,박,감".split(",")
print(b)
['홍', '김', '박', '감']
b = "100,200,300,200".split(",")
print(b)
['100', '200', '300', '200']
print(b[0])
100
print(int(b[0]))
      
print(int(b[0]))
      
100
print(int(b[0]) + int(b[1]))
      # 100 + 200 => 300
print((b[0])+b[1]) #'100' + '200' => '100200'
      
#합과 평균
total = 0
mean = 0
total = int(b[0])+int(b[1])+int(b[2])+int(b[3])
print("total{}= ".format(total))
print("Average{}=".format(total/4))
print("total="+str(total))

print(f"total={total}")
print(f"평균={total/4}") # 변수이름을 그대로 쓸수 있다. 
#구구단 3단 
print(f"{dan}*{1}= {dan*1}")
print(f"{dan}*{2}= {dan*2}")
print(f"{dan}*{3}= {dan*3}")

#생년을 입력받아 나이를 계산해서 출력하기 
# "태어난해 4자리를 입력하세요"
# "당신은 XX살입니다."
year=input("태어난해 4자리를 입력하세요")
age = 2026 - int(year)
print(f"당신은 {age}살 입니다")

