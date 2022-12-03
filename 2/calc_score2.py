# X means you need to lose, 
# Y means you need to end the round in a draw, and 
# Z means you need to win

my_plays = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win'
}

shape_scores = {
    'rock': 1,
    'paper': 2,
    'scissors': 3
}

round_score = {
    'lose': 0,
    'draw': 3,
    'win': 6
}

win = {
    'rock': 'paper',
    'paper': 'scissors',
    'scissors': 'rock'
}

others_plays = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors'
}

def pick_my_play(others_play, round_goal):
    print(f'pick play: {my_plays[round_goal]}')
    if my_plays[round_goal] == 'draw':
        return others_play
    elif my_plays[round_goal] == 'win':
        return win[others_play]
    elif my_plays[round_goal] == 'lose':
        return list(win.keys())[list(win.values()).index(others_play)]

def calculate_round_score(my_play, others_play):
    if my_play == others_play:
        score = shape_scores[my_play] + round_score['draw']
        print(f'...Draw: {score}')
    elif (
        (my_play == 'rock' and others_play == 'scissors') or
        (my_play == 'paper' and others_play == 'rock') or
        (my_play == 'scissors' and others_play == 'paper')
    ):
        score = shape_scores[my_play] + round_score['win']
        print(f'...WIN: {score}')
    else:
        score = shape_scores[my_play] + round_score['lose']
        print(f'...LOSE: {score}')
    return score

strat_guide = open("input.txt").read().split('\n')
total_score = 0
for round in strat_guide:
    print("ROUND: " + round)
    others_play_encrypt, round_goal = round.split(' ')
    others_play = others_plays[others_play_encrypt]
    my_play = pick_my_play(others_play, round_goal)
    print(f'My Play: {my_play}, Others Play: {others_play}')
    
    total_score += calculate_round_score(my_play, others_play)

print('\n')
print(f'My final score: {total_score}')