"""Poker exercise"""

from re import match

def best_hands(hands):
    """Determines the best poker hands from a list of hands.
 
    :param list[str] hands: A list of poker hands.
    :raises ValueError: Raised when there is no input.
    :raises TypeError: Raised when the input is not a list.
    :raises TypeError: Raised when a hand is not a string.
    :raises ValueError: Raised when the hand string is invalid.
    :return list[str]: The list of best hands.
    """

    if hands is None or not hands:
        raise ValueError("No input.")
    if not isinstance(hands, list):
        raise TypeError("Input must be a list of strings.")

    regex_cards = r"([JQKA]|([2-9]|10)([2-9]|10)?)[SHDC] ([JQKA]|([2-9]|10)([2-9]|10)?)[SHDC] " +\
                  r"([JQKA]|([2-9]|10)([2-9]|10)?)[SHDC] ([JQKA]|([2-9]|10)([2-9]|10)?)[SHDC] " +\
                  r"([JQKA]|([2-9]|10)([2-9]|10)?)[SHDC]"

    for hand in hands:
        if not isinstance(hand, str):
            raise TypeError("Hand must be a string.")
        if not match(regex_cards, hand):
            raise ValueError("Invalid input.")

    def _high_card(hand):

        return sorted(hand)[-1][0]

    def _ranks(hand):

        return sum(10**(2*i) * c[0] for i, c in enumerate(sorted(hand)))

    def _flush(hand):

        hand = hand + []
        count_flush = 0
        for card in range(4):
            if hand[card][1] == hand[card+1][1]:
                count_flush += 1
            else:
                break
        return count_flush == 4

    def _straight(hand):

        hand = hand + []
        hand.sort(reverse=True, key=lambda i: i[0]%14)
        hand_royal = sorted(hand, reverse=True)
        count = 0
        count_royal = 0
        for card in range(4):
            if hand[card][0] == hand[card+1][0]%13+1:
                count += 1
            if hand_royal[card][0] == hand_royal[card+1][0]+1:
                count_royal += 1
        return (True, 5 if hand[0][0] == 14 else hand[0][0]) if count == 4 or count_royal == 4\
                else (False, hand[0][0])

    def _xoak(hand):

        hand = hand + []
        hand.sort(key=lambda i: i[0])
        counter = 0
        pairs = []
        trio = False
        while True:
            card = hand.pop()
            if card[0] == hand[-1][0]:
                counter += 1
            else:
                if counter == 1:
                    pairs.append(card[0])
                elif counter == 2:
                    trio = card[0]
                elif counter == 3:
                    return 7*10**14 + 10**12 * card[0] # 4 of a kind
                counter = 0
            if trio and pairs:
                return 6*10**14 + 10**12 * trio + 10**10 * pairs[0] # Full house
            if len(hand) == 1:
                if counter == 1:
                    pairs.append(card[0])
                elif counter == 2:
                    trio = card[0]
                elif counter == 3:
                    return 7*10**14 + 10**12 * card[0] # 4 of a kind
                if trio and pairs:
                    return 6*10**14 + 10**12 * trio + 10**10 * pairs[0] # Full house
                break
        if trio:
            return 3*10**14 + 10**12 * trio # Trio
        if len(pairs) == 2:
            return 2*10**14 + 10**12 * pairs[0] + 10**10 * pairs[1] # 2 pairs
        if pairs:
            return 1*10**14 + 10**12 * pairs[0] # 1 pair
        return 0
    cards = []
    for hand_no, hand in enumerate(hands):
        cards.append([])
        for c in hand.split():
            rank = c[:-1]
            if rank == "J":
                rank = 11
            elif rank == "Q":
                rank = 12
            elif rank == "K":
                rank = 13
            elif rank == "A":
                rank = 14
            else:
                rank = int(rank)
            cards[hand_no].append((rank, c[-1]))
        cards[hand_no].sort(reverse=True, key=lambda i: i[0]%13)
    scores = []
    for hand_no, hand in enumerate(cards):
        result_xoak = _xoak(hand)
        result_straight = _straight(hand)
        score = 0
        if result_xoak:
            score = result_xoak
        elif _flush(hand):
            if result_straight[0]:
                score = 8*10**14 + 10**12 * result_straight[1]
            else:
                score = 5*10**14 + 10**12 * _high_card(hand)
        elif result_straight[0]:
            score = 4*10**14 + 10**12 * result_straight[1]
        score += _ranks(hand)
        scores.append((score, hand_no))
    result = []
    for score in scores:
        if score[0] == max(scores)[0]:
            result.append(hands[score[1]])
    return result
