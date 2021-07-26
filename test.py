# 부모 클래스
class Item:
    # 생성자
    def __init__(self, name, price, weight, isdropable):
        self.name = name
        self.price = price
        self.weight = weight
        self.isdropable = isdropable
    # 파는 메서드
    def sale(self):
        print(f"{self.name}의 가격은{self.price}원 입니다.")
    
    # 버리는 메서드
    def discard(self):
        if self.isdropable:
            print(f"{self.name}을 버렸습니다.")
        else:
            print(f"{self.name}은 버리지 못합니다.")

# 장비 아이템(자식클래스)
class Wearableitem(Item):
    def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect
    
    def wear(self):
        print(f'{self.name}을 착용했습니다. {self.effect}')


# 소모품 아이템(자식 클래스)
class Usableitem(Item):
    def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect

    def use(self):
        print(f'{self.name} 사용 {self.effect}')

weapen = Wearableitem("웨펀무기", 10000, 1.5, True, "착")
weapen.wear()
weapen.sale()
weapen.discard()

hp_postion = Usableitem("HP포션", 1000, 0.1, True, "쓰읍")
hp_postion.use()
hp_postion.sale()
hp_postion.discard()