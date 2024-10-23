import random

class Game():
    def __init__(self):
        pass

    def menu(self):
        while True:
            try:
                self.num_rounds = int(input('''--- Rock Paper Scissors ---
 How many rounds would you like to play? '''))
                break
            except ValueError:
                print("Please enter a valid number of rounds.")
        self.play(self.num_rounds)

    def play(self, num_rounds):
        for i in range(num_rounds):
            human_rps = human.decide()
            computer_rps = computer.decide()
            print('You: ', human_rps, ' | ', 'Computer: ', computer_rps)
            self.winner(human_rps, computer_rps)

        self.show_score()

    def winner(self, human_rps, computer_rps):
        results = {
                  ('r', 'r'): 'tie',
                  ('r', 'p'): 'lost',
                  ('r', 's'): 'won',
                  ('s', 's'): 'tie',
                  ('s', 'p'): 'won',
                  ('s', 'r'): 'lost',
                  ('p', 'p'): 'tie',
                  ('p', 'r'): 'won',
                  ('p', 's'): 'lost',
        }
        if results[(human_rps, computer_rps)] == 'tie':
            print('It\'s a tie') 
        elif results[(human_rps, computer_rps)] == 'lost':
            print('You won') 
            human.update_score(human)
        else: 
            print('You lost')
            computer.update_score(computer)

    def show_score(self):
            print('Your points: ', human.score, ' | ', 'Computer points: ', computer.score)
            if human.score > computer.score:
                print('You win!')
            elif computer.score > human.score:
                print('You lose!')
            else: 
                print('It\'s a tie')

class Player():
    def __init__(self, score = 0):
        self.score = score

    def update_score(self, player):
        player.score += 1
        return player.score


class HumanPlayer(Player):
    def decide(self):
        while True:
            rps = input('Rock, Paper, or Scissors [r/p/s]?')
            if rps in ['r', 'p', 's']:
                self.rps = rps
                return self.rps
            else:
                print('Please enter a valid option')


class ComputerPlayer(Player):

    def decide(self):
        self.rps = random.choice(['r', 'p', 's'])
        return self.rps

if __name__ == "__main__":
    human = HumanPlayer()
    computer = ComputerPlayer()
    game = Game()
    game.menu()


