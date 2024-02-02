# Exercise #22: Rock, Paper, Scissor

def rpsWinner(player1: str, player2: str) -> str:
    """Return the winner of a rock, scissor, paper game.
    
    Key arguments:
    player1 -- player 1 move;
    player2 -- player 2 move
    """
    moves = {'player1': player1, 'player2': player2}
    if not all(x in ['rock', 'paper','scissors'] for x in [player1, player2]):
        return 'Not a valide move. Please play again.'
    elif moves['player1'] == moves['player2']:
        return 'tie'
    elif (moves['player1'] == 'rock') and (moves['player2'] == 'scissors'):
        return 'player one'
    elif (moves['player1'] == 'scissors') and (moves['player2'] == 'paper'):
        return 'player one'
    elif (moves['player1'] == 'paper') and (moves['player2'] == 'rock'):
        return 'player one'
    else:
        return 'player two'

# Testing functions
assert rpsWinner('rock', 'paper') == 'player two'
assert rpsWinner('rock', 'scissors') == 'player one'
assert rpsWinner('paper', 'scissors') == 'player two'
assert rpsWinner('paper', 'rock') == 'player one'
assert rpsWinner('scissors', 'rock') == 'player two'
assert rpsWinner('scissors', 'paper') == 'player one'
assert rpsWinner('rock', 'rock') == 'tie'
assert rpsWinner('paper', 'paper') == 'tie'
assert rpsWinner('scissors', 'scissors') == 'tie'
