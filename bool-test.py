print(10==100) #False # 같다라는 뜻
print(10!=100) #True # 같지 않다라는 뜻
print(10<=100) #True 
print(10>=100) #False
a = "가방"
b = "하마"
print(a==b) # A와 B가 같냐 False
print(a<b) # 글자의 순서. True
print(a>b) # False
c=35
print(10<c<30) #True
print(10<c<20) #Falue

if not c < 30:
    print("c는 30보다 작음") # 탭하여 들여쓰기 한다음 트루일결우의 조건문
else:
    print("c는 30보다 큼")
    print("c는 30보다 큼")

print("END") # False일 경우 조건문 들여쓰기 X 
################
score = 78
grade = "" #비워둠
if score >=90:
    grade = "A"
elif score >=80:
    grade = "B"
elif score >=70:
    grade = "C"
else:
    grade = "F"
print(f"{score}의 학점은 {grade}")

score=78
grade=""
if score <=100 and score >=90:
    grade ="A"
elif score <=89 and score >=80:
    grade ="B"
else:
    grade="F"
print(f"{score}의 학점은 {grade}")

number=input("정수 입력>")
last_character = number[-1]

if last_character in "02468":
    print("짝수입니다")
else:
    print("홀수입니다")



