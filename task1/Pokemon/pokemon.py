import random

class Pokemon:
    def __init__(self,name,type,HP,attack,defence,dodge_rate):
        self.name = name
        self.HP = HP
        self.attack = attack
        self.defence = defence
        self.dodge_rate = dodge_rate
        self.type = type
    
    def dodge(self):
        dodge_number = random.randint(1,10)
        if dodge_number <= self.dodge_rate:
            print(f"{self.name}躲闪了这次攻击！")                       #这里要添加  把攻击躲闪的代码
                                                        
    def check_HP(self):
        if self.HP <= 0:
            print(f"{self.name}已昏厥！")

class GrassPokemon(Pokemon):
    def __init__(self,name,type,HP,attack,defence,dodge_rate):
        super().__init__(name,type,HP,attack,defence,dodge_rate)

class WaterPokemon(Pokemon):
    def __init__(self,name,type,HP,attack,defence,dodge_rate):
        super().__init__(name,type,HP,attack,defence,dodge_rate)

class FirePokemon(Pokemon):
    def __init__(self,name,type,HP,attack,defence,dodge_rate):
        super().__init__(name,type,HP,attack,defence,dodge_rate)

class ElectricPokemon(Pokemon):
    def __init__(self,name,type,HP,attack,defence,dodge_rate):
        super().__init__(name,type,HP,attack,defence,dodge_rate)
    
class Pikachu(ElectricPokemon):
    def __init__(self,name,type,HP,attack,defence,dodge_rate):
        super().__init__("Pikachu","Electric",80,35,5,3)
        

class Bulbasaur(GrassPokemon):
    def __init__(self,name,type,HP,attack,defence,dodge_rate):
        super().__init__("Bulbasaur","Grass",100,35,10,1)
        
class Squirtle(WaterPokemon):
    def __init__(self,name,type,HP,attack,defence,dodge_rate):
        super().__init__("Squirtle","Water",80,25,20,2)

class Charmander(FirePokemon):
    def __init__(self,name,type,HP,attack,defence,dodge_rate):
        super().__init__("Charmander","Fire",80,35,15,1)