name = ["김민서", "이건호", "김용수", "배민경"]

word = "파이팅"
mbti = ["ENFJ", "ENTP", "INTP", "ENTJ"]
birth = [1998, 1994, 1998, 2000]


for i in name:
    print(i + " " + word)


def age():
    birth = int(input("태어난 년도를 입력해 주세요 : "))
    age = 2025 - birth
    print(f"2025년에 당신의 나이는 { age }입니다.")


def user_info(name):
    name = input("이름을 입력하세요: ")
    print("이름: ", name)
    index = name.index(name)
    print("MBTI: ", mbti[index])
    print("생년월일: ", birth[index])
