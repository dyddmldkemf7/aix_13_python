print(range(3))
import os
old_name = "04-3.py"
new_name = "04-3-test.py"
print(list(range(3)))
print(range(1,46))
# print(list(range(1,46)))
print(list(range(1,46,5))) # 5씩 증가
print(list(range(5,1,-1))) #[5,4,3,2]
#3단구구단출력
# 3*1=3
# 3*2=3

print(list(range(3,7,3))) 

dan=4

for i in range(1,10):
    print(f'{dan}*{i}={dan*i}')
### 구구단
# 2*1=2
  
# 3*1=3

# 9*1=9
# for i in range(2,10):
#     for j in range(1,10):
#         print(f'{i}*{j}={i*j}')
# i=0
# while i <3: #i가 3보다작은동안 실행
#     print(f'i={i}')
#     # i+=1/#생략하면 무한반복 crt1+c로 종료
#     print(f'while end i={i}')
#     print('end')
# i=0
# while i<10: # 0~9
#     print(f"i={i}")
#     i+=1
#     if i==2:
#         break

ns=[5,15,6,20,7,25]

for n in ns:
    if n < 10:
        continue #참일경우 밑에를 무시하고 다음 숫자로 넘어가 
    print(n)

