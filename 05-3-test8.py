with open('info.txt','r',encoding='utf8') as file:
    for line in file: # 한줄씩 읽기
        name,w,h=line.strip().split(',')
        bmi = int(w) / int(h)*int(h)
        result = ""
        if 25<= bmi:
            result='과체중'
        elif 18.5 <= bmi:
            result='정상체중'
        else:
            result='저체중'
        print(f'이름:{name} 몸무게:{w} 키:{h}')
        print(f'BMI:{round(bmi)} 결과:{result}')
