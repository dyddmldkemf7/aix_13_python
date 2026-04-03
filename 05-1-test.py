# 인사말함수
def hello():
    print("안녕하세요")
def hello_ntimes(msg="안녕하세요",n=1): #함수이름 함수_이름 named,  n=1하면 매개변수 기본값 설정
        for i in range(n):
            print(msg)
# hello_ntimes("방가방가",3) # 가로안 매개변수 한다고 정의했는데 실행할때 없으면 에러
# gugudan(3) -> 3단 구구단 출력
# gugudan() -> 2단 구구단 출력




#3단부터 7단까지
def gugudan(n=3, n2=-1):
    if n2==-1:
        end = n
    else:
        end = n2
    for dan in range(n, end+1):
        for i in range(1,10):
            print(f'{dan}*{i}={dan*i}')
    
        print()

gugudan(3,7)