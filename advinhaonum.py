import random

def adv(x):
    random_number = random.randint(1, x)
    adv = 0
    while adv != random_number:
        adv = int(input(f'Chute um numero entre 1 e {x}: '))
        if adv < random_number:
            print('Tente novamente, o numero eh maior!')
        elif adv > random_number:
            print('Tente novamente, o numero eh menor!')

    print(f'Parabens! Voce acertou, o numero eh {random_number}!')

adv(100)