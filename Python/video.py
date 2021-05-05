movielist=[]
directorlist=[]
actorlist=[]

movies ={
    'MOV001':['인셉션',2012,'미국'],
    'MOV002':['어벤져스4',2019,'미국'],
    'MOV003':['기생충',2019,'한국']
}

for key in movies.keys():
    movielist.append(key)

directors = {
    'DIR001': ['MOV001', '크리스토퍼 놀란'],
    'DIR002': ['MOV002', '조 루소'],
    'DIR003': ['MOV002', '앤서니 루소'],
    'DIR004': ['MOV003', '봉준호']
}

for key in directors.keys():
    directorlist.append(key)

actors = {
    'ACT001': ['MOV001', '레오나르도 디카프리오', 46],
    'ACT002': ['MOV002', '로버트 다우니 주니어', 54],
    'ACT003': ['MOV003', '최우식', 32]
}

for key in actors.keys():
    actorlist.append(key)

    
def Numup(selectedlist):
    last=selectedlist[len(selectedlist)-1]
    lastnumup=int(last[3:])+1
    if(lastnumup<10):
        finalnum='00'+str(lastnumup)
    elif(lastnumup<100):
        finalnum='0'+str(lastnumup)
    elif(lastnumup<1000):
        finalnum=str(lastnumup)
    return finalnum   


def delete_(selectedlist,selecteddic):
    userinput=input('삭제할 고유 번호를 입력하세요 : ')
    for i in selectedlist:
        if(userinput==i):
            selecteddic.pop(userinput)
            selectedlist.remove(userinput)


while True:
    print()
    mainnum=int(input('입력(1)/조회(2)/삭제(3)/종료(4) : '))
    print()
    
    if(mainnum==1):
        print('데이터 입력을 시작하겠습니다.')
        print()
        name=input('영화 이름을 입력하시오 : ')
        year=int(input('영화 개봉년도를 입력하시오 : '))
        con=input('어느나라 영화인지 입력하시오 : ')
        movnum='MOV'+Numup(movielist)
        movies[movnum]=[name,year,con]
        movielist.append(movnum)

        while(True):
            print()
            userinput=input('감독 정보를 입력하시겠습니까?(o/x) : ')
            
            if(userinput=='o'):     
                name=input('감독 이름을 입력하시오 : ')
                dirnum='DIR'+Numup(directorlist)
                directors[dirnum]=[movnum,name]
                directorlist.append(dirnum)

            elif(userinput=='x'):
                while(True):
                    print()
                    userinput2=input('배우 정보를 입력하시겠습니까?(o/x) : ')
                    if(userinput2=='o'):
                        name=input('배우 이름을 입력하시오 : ')
                        age=int(input('배우 나이를 입력하시오 : '))
                        actnum='ACT'+Numup(actorlist)
                        actors[actnum]=[movnum,name,age]
                        actorlist.append(actnum)
                    elif(userinput2=='x'):
                        break
                    else:
                        print('다시 선택하세요')
                break
            else:
                print('다시 선택하세요')


    elif(mainnum==2):
        for item in movies.items():
            print(item)
        print()
        for item in directors.items():
            print(item)
        print()
        for item in actors.items():
            print(item)
        print()


    elif(mainnum==3):
        while(True):
            userinput=input('삭제할 정보를 선택하세요(감독(1)/배우(2)) : ')
            if(userinput=='1'):
                delete_(directorlist,directors)
                break

            elif(userinput=='2'):
                delete_(actorlist,actors)
                break

            else:
                print('다시 선택하세요')

    elif(mainnum==4):
        break
    
    else:
        print('다시 선택하세요')

