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
    for i in range(len(hands)):
        if i < len(hands)-1 and hands[i][1] == hands[i+1][1]:
            first, second = tie_break(hands[i], hands[i+1])
            hands[i] = first
            hands[i+1] = second
    return hands


def tie_break(hand1, hand2):
    card_types = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

    if find_strength(hand1) > find_strength(hand2):
        hand2 = (hand2[0], int(hand2[1]) - 0.5, hand2[2])
        return hand1, hand2
    elif find_strength(hand1) < find_strength(hand2):
        hand1 = (hand1[0], int(hand1[1]) - 0.5, hand1[2])
        return hand1, hand2
    else:
        for card1, card2 in zip(hand1[0], hand2[0]):
            if card_types.index(card1) > card_types.index(card2):
                return 


def calculate_winnings(ranked_hands):
    total = 0
    for hand in ranked_hands:
        idx = ranked_hands.index(hand)+1
        sum = idx * int(hand[2])
        total += sum
    return total


def main():
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

    hands_powers = sorted(zip(hands, powers, bids))
    ranked_hands = rank_hands(hands_powers)
    print(ranked_hands)
    #winnings = calculate_winnings(ranked_hands)


if __name__ == "__main__":
    main()

