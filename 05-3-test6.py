# file=open("basic.txt",'w')
# file.write("\n") #줄바꿈
# file.write("헬로 파이썬 프로그래밍 5")
# input('엔터키 누르세요')
# file.close()
# print('end')
with open("basic.txt",'w') as file:
    file.write("\n") #줄바꿈
    file.write("헬로 파이썬 프로그래밍 5")
    file.writelines()    
print('end')