import random



class Jokenpo():

    def __init__(self):

        self.choices = [

                'rock', 
                'paper', 
                'scissors'

        ]

        self.winnable_choices = [

            [self.choices[0], self.choices[2]],
            [self.choices[1], self.choices[0]],
            [self.choices[2], self.choices[1]]

        ]


        ## main worker loop
        while True:

            ## machine making its choice
            self.machine_choice = random.choice(self.choices)

            ## loop for player choice and if user enters an errorful choice
            while True:
                self.player_choice = str(input('\nRock, paper or scissors? ')).lower()

                if self.player_choice not in self.choices:
                    print('Enter a valid choice! ')
                    continue

                else:
                    self.arranged_choices = [self.player_choice, self.machine_choice]
                    break

            ## if it is a draw
            if self.player_choice == self.machine_choice:
                self.interface(" > It's a draw!")

            # if win
            elif self.arranged_choices in self.winnable_choices:
                self.interface(' > You won!')

            # if not any condition left (if lost)
            else:
                self.interface(' > You Lost!')
                
            self.retry = str(input('Wanna play again? Y/N '))

            if self.retry not in 'yY':
                break

    def interface(self, response):

        print(f"{response} \n   - Your choice: {self.arranged_choices[0]}\n   - Machines choice: {self.arranged_choices[1]}")


if __name__ == '__main__':
    Jokenpo()