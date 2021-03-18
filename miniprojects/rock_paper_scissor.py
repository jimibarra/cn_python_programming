import random

def get_hand(hand):
    # 0 = scissor, 1 = rock, 2 = paper
    # for example if the variable hand is 0, it should return the string "scissor"
    if hand == 0:
        item = 'scissor'
    elif hand == 1:
        item = 'rock'
    elif hand == 2:
        item = 'paper'
    else:
        item = 'unknown'
    return item

def determine_winner(user_val, computer_val):
    winner_dict = {'rs':'u', 'rr':'t', 'rp':'c', 'ps':'c', 'pr':'u', 'pp':'t', 'ss':'t', 'sr':'c', 'sp':'u'}
    winner = winner_dict[str(user_val + computer_val)]
    return winner

# Get number 0-2 from user to represent their hand
# Call function get_hand to get string representation of user's hand
user_input = int(input('Enter a number 0 1 or 2: '))
user_hand = get_hand(user_input)

# Randomly generate a hand 0-2 for computer's hand
# Call function get_hand to get string representation of computer's hand
computer_input = random.randint(0,2)
computer_hand = get_hand(computer_input)

# Call function determine_winner to figure out who won
hand_winner = determine_winner(user_hand[0], computer_hand[0])

# Print out the user hand and computer hand
print(f"The user's hand is {user_hand}")
print(f"The computer's hand is {computer_hand}")

# Print of the winner
if hand_winner == 'u': win = 'user'
elif hand_winner == 'c': win = 'computer'
else: win = 'stalemate'
print(f'The winner is {win}')
