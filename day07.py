# relative ranking
# tie breaker
# multiplying total winnings

def find_strength(hand: str = '23456') -> int:
    reps = []
    prev_cards = [] 
    for card in hand: 
        if card not in prev_cards:
            reps.append(hand.count(card))
        prev_cards.append(card)

    if len(reps) == 1:
        return 7
    elif len(reps) == 2:
        return 6 if max(reps) == 4 else 5
    elif len(reps) == 3:
        return 4 if max(reps) == 3 else 3
    elif len(reps) == 4:
        return 2
    else:
        return 1


def rank_hands(hands):
    prev_hand = []
    for hand in hands:
        if hand[1] == prev_hand:
            tie_break(hand[0], prev_hand[0])
        else:
            prev_hand = hand[1]


def tie_break(hand1, hand2):
    print(hand1)
    print(hand2)



with open('input', 'r') as f:
    lines = f.readlines()


hands = []
bids = []

for line in lines:
    hand, bid = line.split(' ')
    bid = bid.replace('\n', '')
    hands.append(hand)
    bids.append(bid)

powers = [] 
for hand in hands:
    powers.append(find_strength(hand))

hands_powers = sorted(zip(hands, powers))
rank_hands(hands_powers)





#def break_tie(hands: str):
#def calculate_winnings(hand: str, bid: int):
