import random
SUITS_TUPLE = ("Spades", 'Hearts',  "Clubs", "Diamonds")
RANK_TUPLE = ('Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', "kink")
LIFE = 3


def getCard(deckList: list[dict]):
    return deckList.pop()


def shuffle(dekList: list[dict]):
    deckListOut = dekList.copy()
    random.shuffle(deckListOut)
    return deckListOut


print('Welcome to Higher or Lower.')
print('You have to choose whether the next card to be shown will be higher or lower than the current card.')
print('Getting it right adds 20 points; get it wrong and you lose 15 points.')
print('You have 50 points to start.')
print()

DESK_LISTS = []
jo = list(zip(SUITS_TUPLE, RANK_TUPLE))
for suit in SUITS_TUPLE:
    for x, rank in enumerate(RANK_TUPLE):
        obj = {'suit': suit, 'rank': rank, 'value': x+1}
        DESK_LISTS.append(obj)

score = 50
