init pygame

def attack (Hp, Ap):
    Hp-=5
    Ap+=1
    return Hp, Ap

def hard_slash(Hp, Ap):
    Hp-=15
    Ap-=2
    return Hp, Ap
