#로또번호추출방법2
nums = list(range(1,46)) #1~45
print('nums',nums)
mylotto = [] #로또번호저장용
for a in [1,2,3,4,5,6]:
    #nums에서 임의의  위치를 지정,저장,삭제
    import random 
    r = random.randint(0,len(nums)-1) # 0번째부터 44번째까지 랜덤하게 1개 선택
    mylotto.append(nums[r]) #로또번호저장
    nums.pop(r) #저장한번호 삭제.중복선택불가
mylotto.sort()
print('mylotto',mylotto)

