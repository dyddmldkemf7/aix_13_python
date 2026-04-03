import datetime

now = datetime.datetime.now()
print(now)
print(f"{now.year}년")
print(f"{now.month}월")
print(f"{now.day}일")
print(f"{now.hour}시")
print(f"{now.minute}분")
print(f"{now.second}초")
print(f"{now.weekday()}요일") #0=월 1화2수3목4금5토6=일



###########
if now.hour < 12: 
    print(f"현재시간 {now.hour}시로 오전입니다")
else:
    print(f"현재시간 {now.hour}시로 오후입니다")
    
### 167P if...elif로 작성해보세요
if  3<=now.month<=5:
    print(f"이번 달은 {now.month}월로 봄입니다!")
elif 6<=now.month<=8:
    print(f"이번 달은 {now.month}월로 여름입니다!")
elif 9<=now.month<=11:
    print(f"이번 달은 {now.month}월로 가을입니다!")
else:
    print(f"이번 달은 {now.month}월로 겨울입니다!")


### 월을 입력받아 계절 출력하기 
month = input("월을 입력(1~12)")
month = int(month)
if  month<3:
    print(f"이번 달은 {month}월로 겨울입니다!")
elif month<=5:  
    print(f"이번 달은 {month}월로 봄입니다!")
elif month<=8:  
    print(f"이번 달은 {month}월로 여름입니다!")
elif month<=11:  
    print(f"이번 달은 {month}월로 가을입니다!")
else:
    print(f"이번 달은 {month}월로 겨울입니다!")
