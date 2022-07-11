import random

coin = 0


def flip():
    global coin

    if coin == 0:
        coin = 1
    else:
        coin = 0


# wins[0] = Q's wins wins[1] = P's wins
wins = [0, 0]

print("enter P's probability to flip the coin(1-100): ")
p = int(input())

print("enter Q's probability to flip the coin in the first turn(1-100): ")
q1 = int(input())

print("enter Q's probability to flip the coin in the second turn(1-100): ")
q2 = int(input())

print("How many times do you want to run the simulation: ")
rounds_num = int(input())

for i in range(rounds_num):
    # first turn
    if q1 <= random.randint(1, 100):
        flip()
    # second turn
    if p <= random.randint(1, 100):
        flip()
    # third turn
    if q2 <= random.randint(1, 100):
        flip()

    # find the winner and update wins list
    if coin == 0:
        wins[0] += 1
    else:
        wins[1] += 1

print("Q won {} times and P won {} times out of {} rounds".format(
    wins[0], wins[1], rounds_num))
