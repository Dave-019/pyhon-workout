import random

def guess_num():
    answer = random.randint(1, 100)
    attempts = 0
    while True:
        user = int(input("what's ur guess? "))
        if user == answer:
            print("congratulation!")
            break
        elif user > answer:
            print("too big")
        else:
            print("too small")
        attempts +=1
        if attempts > 3:
            print("you have exceeded No. of attempts")
            break
guess_num()
