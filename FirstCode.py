name = ["김민서", "이건호", "김용수", "배민경"]

word = "파이팅"
mbti = ["ENFJ", "ENTP", "INTP", "ENTJ"]
birth = [1998, 1994, 1998, 2000]


for i in name:
    print(i + " " + word)


def user_info(name):
    name = input("이름을 입력하세요: ")
    print("이름: ", name)
    index = name.index(name)
    print("MBTI: ", mbti[index])
    print("생년월일: ", birth[index])
