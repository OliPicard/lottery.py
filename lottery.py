import random


def randomizer():
    rand = random.randrange(1, 49)
    return rand


def randomloop():
    listy = []
    for i in range(5):
        t = randomizer()
        if listy.count(t):
            t = randomizer()
            listy.append(t)
        else:
            listy.append(t)
    print(listy)
    input("press any key to terminate")


def main():
    randomloop()

if __name__ == "__main__":
    main()
