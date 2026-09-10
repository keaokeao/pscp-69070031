"""pai"""
card = input()
amount = len(card)
first = ""
last = ""
if amount == 2 :
    if card[0] in "aA" :
        first = "ace"
    elif card[0] in "jJ" :
        first = "jack"
    elif card[0] in "qQ" :
        first = "queen"
    elif card[0] in "kK" :
        first = "king"
    elif card[0] in "123467890" :
        first = card[0]
    if card[1] in "dD" :
        last = "diamonds"
    elif card[1] in "sS" :
        last = "spades"
    elif card[1] in "cC" :
        last = "clubs"
    elif card[1] in "hH" :
        last = "hearts"
elif amount == 3 :
    first = "10"
    if card[2] in "dD" :
        last = "diamonds"
    elif card[2] in "sS" :
        last = "spades"
    elif card[2] in "cC" :
        last = "clubs"
    elif card[2] in "hH" :
        last = "hearts"
print(first, "of", last)
