# 과일 채소 리스트 생성
fruit = ["사과", "오렌지", "포도", "파인애플"]
vegetable = ["당근", "호박", "양상추", "브로콜리"]

# 사용자가 입력할 카테고리&상품명 입력받기
cate = input("등록할 카테고리를 선택하세요(과일 / 채소): ")
name = input("상품명을 입력하세요: ")


if cate == "과일":  # 입력받은 카테고리가 과일일 경우
    if name in fruit:  # 이미 과일 리스트에 입력받은 상품명이 있을 경우
        print("이미 등록된 과일입니다.")
    else:  # 없을 경우 과일 리스트에 추가
        fruit.append(name)

elif cate == "채소":  # 입력받은 카테고리가 채소일 경우
    if name in vegetable:  # 이미 채소 리스트에 입력받은 상품명이 있을 경우
        print("이미 등록된 채소입니다.")
    else:  # 없을 경우 채소 리스트에 추가
        vegetable.append(name)

else:  # 잘못된 카테고리를 입력할 경우
    print("존재하지 않는 카테고리입니다.")


# 리스트 출력
print(fruit)
print(vegetable)
