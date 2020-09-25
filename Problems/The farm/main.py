# Input from the user, how much money the user has
money = int(input())

# How many animals the user can afford, if non = None
chicken = 23
goat = 678
pig = 1296
cow = 3848
sheep = 6769

if money >= sheep:
    buy_sheep = money // sheep
    print(buy_sheep, 'sheep')
elif money >= cow:
    buy_cow = money // cow
    print(buy_cow, 'cow' if buy_cow == 1 else 'cows')
elif money >= pig:
    buy_pig = money // pig
    print(buy_pig, 'pig' if buy_pig == 1 else 'pigs')
elif money >= goat:
    buy_goat = money // goat
    print(buy_goat, 'goat' if buy_goat == 1 else 'goats')
elif money >= chicken:
    buy_chicken = money // chicken
    print(buy_chicken, 'chicken' if buy_chicken == 1 else 'chickens')
else:
    print('None')
