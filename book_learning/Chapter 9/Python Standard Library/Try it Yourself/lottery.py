### Try it Yourself: 9-14

### Task:
# Make a list or tuple containing a series of 10 numbers and
# five letters. Randomly select four numbers or letters from the list and print a
# message saying that any ticket matching these four numbers or letters wins a
# prize.

from random import choice

digit_number_bank = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "a", "b", "c", "d", "e"]

winning_lottery_ticket = []

for _ in range(0, 4):
    tmp = choice(digit_number_bank)
    winning_lottery_ticket.append(tmp)

print(
    f"The following digits/letters are the winning lottery ticket! Get all of them and you win!\n{winning_lottery_ticket}"
)

### Try it Yourself: 9-15

### Task:
# You can use a loop to see how hard it might be to win
# the kind of lottery you just modeled. Make a list or tuple called my_ticket.
# Write a loop that keeps pulling numbers until your ticket wins. Print a message
# reporting how many times the loop had to run to give you a winning ticket.

from collections import Counter

counter = 0
flag = True


def check_if_ticket_is_a_winner(my_ticket, winning_lottery_ticket):
    """
    Checks whether the two lists elements are equal, regardless of order.
    'Counter' creates a dictionary-like object that counts the occurrences of
    each element in each list.
    We then compare the 'Counter' of each list to see if they are equal.
    """
    status = Counter(my_ticket) == Counter(winning_lottery_ticket)

    return status


def generate_my_ticket(digit_number_bank):
    """Generates a list of 4 random elements from a static base list"""
    my_ticket = []

    for _ in range(0, 4):
        tmp = choice(digit_number_bank)
        my_ticket.append(tmp)

    return my_ticket


while flag:
    my_ticket = generate_my_ticket(digit_number_bank)

    outcome = check_if_ticket_is_a_winner(my_ticket, winning_lottery_ticket)

    counter += 1

    if outcome == True:
        flag = False
        print(f"It took you {counter} attempts to get a winning ticket")
        print(my_ticket, winning_lottery_ticket)
