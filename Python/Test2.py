
#dictionary 변수 선언
dicUser={}

#사용자 정보를 받는 함수 userinfo 정의
def userinfo(comment):  
    val=input(comment)
    return val

name=userinfo('이름: ') #userinfo 함수를 이용하여 name을 입력받음
age=userinfo('나이: ')  #userinfo 함수를 이용하여 age를 입력받음
phone=userinfo('연락처: ')  #userinfo 함수를 이용하여 phone을 입력받음

dicUser.update({'name':name,'age':age,'phone':phone}) #dictionary에 항목 추가

print(dicUser) 