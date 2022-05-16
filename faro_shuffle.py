cards_deck = input().split(' ')
number_of_shuffles = int(input())
print_deck = cards_deck

for _ in range(number_of_shuffles):
    top_half = print_deck[:len(print_deck)//2]
    bottom_half = print_deck[len(print_deck)//2:]
    print_deck.clear()
    for i in range(len(top_half)):
        print_deck.append(top_half[i])
        print_deck.append(bottom_half[i])

print(print_deck)