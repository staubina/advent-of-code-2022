# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors

# A beats Z, B beats X, C beats Y
# X beats C, Y beats A, Z beats B

my_plays = {
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors'
}

shape_scores = {
    'rock': 1,
    'paper': 2,
    'scissors': 3
}

round_score = {
    'lost': 0,
    'draw': 3,
    'win': 6
}

others_plays = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors'
}

def calculate_round_score(round):
    print(round)
    others_play, my_play = round.split(' ')
    if my_plays[my_play] == others_plays[others_play]:
        score = shape_scores[my_plays[my_play]] + round_score['draw']
        print(f'...Draw: {score}')
    elif (
        (my_plays[my_play] == 'rock' and others_plays[others_play] == 'scissors') or
        (my_plays[my_play] == 'paper' and others_plays[others_play] == 'rock') or
        (my_plays[my_play] == 'scissors' and others_plays[others_play] == 'paper')
    ):
        score = shape_scores[my_plays[my_play]] + round_score['win']
        print(f'...WIN: {score}')
    else:
        score = shape_scores[my_plays[my_play]] + round_score['lost']
        print(f'...LOSE: {score}')
    return score

strat_guide = open("input.txt").read().split('\n')
total_score = 0
for round in strat_guide:
    total_score += calculate_round_score(round)

print('\n')
print(f'My final score: {total_score}')