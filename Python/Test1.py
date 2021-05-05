
cut=65   #세 과목 모두 넘어야 할 최소 점수
maximum=100  #최대 점수 
minimum=0   #최소 점수

num1=int(input('창사코: '))  #integer형의 창사코 점수를 입력받아 변수 num1에 저장
num2=int(input('선형대수: '))  #integer형의 선형대수 점수를 입력받아 변수 num2에 저장
num3=int(input('컴퓨터공학: '))  #integer형의 컴퓨터공학 점수를 입력받아 변수 num3에 저장

print(num1,num2,num3)  #num1, num2, num3 출력

 #만약 세 과목 점수 중 하나라도 maxinum 점수를 넘는다면
if num1>maximum or num2>maximum or num3>maximum: 
  print('잘못된 점수가 입력되었습니다.')  #잘못된 점수가 입력되었습니다 출력

#만약 세 과목 점수 중 하나라도 maxinum 점수를 넘는다면
elif num1<minimum or num2<minimum or num3<minimum: 
  print('잘못된 점수가 입력되었습니다.')  #잘못된 점수가 입력되었습니다 출력

#만약 세 과목 점수 모두 cut 점수를 넘는다면
elif num1>cut and num2>cut and num3>cut:
  print('합격')  #합격 출력

#세 과목 중 하나라도 cut 점수를 넘기지 못하면
else:
  print('불합격')  #불합격 출력