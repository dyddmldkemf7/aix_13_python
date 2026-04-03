    # 지뢰찾기(빨리 터트리기)
    # 10x10 영역에 3개의 지뢰를 매설
    # 최소의 시도로 모두 터트리기
 # import는 가급적 코드 맨 위에서 한 번만 합니다.

#지뢰찾기(빨리 터트리기)
# 10x10 영역에 3개의 지뢰를 매설
# 최소의 시도로 모두 터트리기
# 실력대로 해보기(초급(5x5-2),중급(7x7-4),고급(10x10-7)
# 레벨을 선택하세요
# 1-초급(5x5), 지뢰 2개 
# 2-중급(7x7), 지뢰4개
# 3-고급(10x10), 지뢰 6개
# 선택 레벨>>
# 1. 상단에 레벨 선택 및 변수 설정 추가
level = input("1-초급(5x5,2), 2-중급(7x7,4), 3-고급(10x10,6) 선택>> ")
if level == '1': size, total_mines = 5, 2
elif level == '2': size, total_mines = 7, 4
else: size, total_mines = 10, 6

mines = [] #출력용
for i in range(size):
    mines.append(['+']*size)

nums = [] #계산용
for i in range(size):
    nums.append([0]*size)
# 임의의 지점에 지뢰 저장(3개)
mine_count = 0
while mine_count < total_mines:
    import random
    row = random.randint(0,size-1)
    col = random.randint(0,size-1)
    #폭탄이 같은 자리인 경우 배치취소
    if nums[row][col] >= 9: continue
    mine_count += 1 #배치폭탄 갯수 1 증가
    nums[row][col]=9
    # 이웃한 8개 방의 숫자를 1증가
    if row != 0 and col !=0 : nums[row-1][col-1] += 1
    if row != 0  : nums[row-1][col] += 1
    if row != 0 and col !=size-1 : nums[row-1][col+1] += 1
    if col != size-1 : nums[row][col+1] += 1
    if row != size-1 and col != size-1 : nums[row+1][col+1] += 1
    if row != size-1  : nums[row+1][col] += 1
    if row != size-1 and col != 0 : nums[row+1][col-1] += 1
    if col != 0 : nums[row][col-1] += 1

# # 확인
# for n in nums:
#     print( n )

remain_mine = mine_count #남은 폭탄갯수
while remain_mine != 0:
    msg = f'지뢰의 좌표를 입력하세요(0~{size-1},0~{size-1}) x,y >> '
    ans = input(msg)
    
    try:
        
        u_row, u_col = ans.split(',')
        u_row, u_col = int(u_row), int(u_col)
        
        
        if not (0 <= u_row < size and 0 <= u_col < size):
            print(f"0~{size-1} 사이의 숫자를 입력하세요!")
            continue

        if nums[u_row][u_col] >= 9: # 지뢰 찾으면
            mines[u_row][u_col] = "$"
            remain_mine -= 1  
        else:
            mines[u_row][u_col] = str(nums[u_row][u_col])
            
        # mines 리스트 출력
        for m in mines:
            print(" ".join(m))
            
        # 4. 남은 지뢰수 출력
        print(f"남은 지뢰 개수: {remain_mine}")
        print("-" * 20)
        
    except ValueError:
        # 에러가 났을 때 실행될 부분
        print("'숫자,숫자' 형식으로 입력해야 합니다! (예: 0,1)")
        continue

print("축하합니다! 모든 지뢰를 찾았습니다.")







