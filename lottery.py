import random


def randomizer():
    rand = random.randrange(1, 49)
    return rand


def randomloop():
    listy = []
    d = 0
    c = 10
    while d < c:
        t = randomizer()
        if listy.count(t):
            t = randomizer()
            listy.append(t)
        else:
            listy.append(t)
        d += 1

    print(listy)
    input("press any key to terminate")


def main():
    randomloop()

if __name__ == "__main__":
    main()
