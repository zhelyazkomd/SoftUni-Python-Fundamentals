data = input()
coins = [int(x) for x in data.split(", ")]

beggars_number = int(input())
beggars_coins = [0 for _ in range(beggars_number)]

i = 0
while i < len(coins):
    for j in range(beggars_number):
        beggars_coins[j] += coins[i]
        i += 1
        if i == len(coins):
            break

print (beggars_coins)