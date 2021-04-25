import random

name = input("이름을 입력하세요. : ")
print(name, "님 반갑습니다. {0}으로 팩맨게임을 시작합니다.".format(name))

selectList = ["1. 도망간다.", "2. 아이템사용.", "3. 싸운다."]

item = {"hpPotion" : 1, "spdBoost" : 10}
itemNameList = list(item.keys())

def behaviorSelect(num):
    if num == 1:
        if round(random.random() * 10) > 5:
            print("도망 치지 못했습니다.")
        else:
            print("도망쳤습니다.")

    if num == 2:
        while True:
            print("사용 할 아이템 선택 : hpPotion : ", item["hpPotion"], "개// spdBoost : ", item["spdBoost"], "개")
            print("아이템 번호 입력 // 1 : ", itemNameList[0], "2 : ", itemNameList[1])
            itemNumber = input()
            itemNumber = int(itemNumber) - 1
            itemName = itemNameList[itemNumber]
            if  item[itemName] > 0:
                item[itemName] -= 1
                print(itemNameList[itemNumber], "사욛. 남은 갯수", item[itemName])
                break
            
            elif item[itemName] is 0:
                print("아이템이 모자랍니다.")

            else:
                print("아이템 번호를 잘못 입력하셨습니다.")
        return "아이템 사용"

    if num == 3:
        print("싸운다")


for i in range(1, 6):
    print(i, "유령이 나타났다")

    for a in range(len(selectList)):
        print(selectList[a])
    
    print("숫자를 입력하세요: ")

    selectNum = int(input())
        
    print("유저 입력값:", selectNum)
    behaviorSelect(selectNum)

    



    
