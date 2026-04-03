'''
숫자맞추기게임(UpDown)
1~100사이 임의의 숫자를 컴퓨터가 정한것을
스무고개형식으로 맞추는 게임
출력예시)
1번째시도: 1~100사이 숫자 입력>> 70
 낮춰주세요
2번재시도:1~100사이 숫자 입력>> 60
높여주세요
3번재시도:1~100사이 숫자 입력>> 65
정답입니다

6번재시도:1~100사이 숫자 입력>> 65
정답입니다

정답은 XX
당신은 바보입니까?

'''
print("### 숫자맞추기게임 v0.1 ###")
#1~100사이 임의의 정수를 저장
import random
com = random.randint(1,100)
count = 0 #시도 횟수 저장할 변수 초기화
for count in range(1,7):
    count += 1
    user = input(f"{count}번째시도 1~100사이 숫자>> ")
    user = int(user) #글자를 숫자로 변환
    # 판정
    if com == user:
        break # 반복문 종료
    if com < user:
        r=list(range(user))
        print("낮춰주세요")
        print("후보숫자>>{r}")    
    else:
        print("높여주세요")

else: print(f"정답은 {user} 당신은 바보입니까")
