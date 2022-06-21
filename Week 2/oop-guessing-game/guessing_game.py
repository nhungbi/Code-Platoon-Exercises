import random 
class GuessingGame():
    def __init__(self,answer):
        self.answer = answer
        self.current_guess = None
    
    def guess(self, user_guess):
        """
        Given a user guess, return high if the guess is higher than answer,
        low if guess is lower, and correct if the guess is equal to answer.
        """
        self.current_guess = int(user_guess) 
        if self.current_guess  > self.answer:
            return 'high'
        elif self.current_guess  < self.answer:
            return 'low'
        elif self.current_guess  == self.answer:
            return 'correct'

    def solved(self):
        """
        Return True if user guessed the answer, False otherwise.
        """
        if self.current_guess != None and self.guess(self.current_guess) == 'correct':
            return True
        return False
    
##TESTING##

game = GuessingGame(random.randint(1,100))
last_guess  = None
last_result = None

while game.solved() == False:
  if last_guess != None: 
    print(f"Oops! Your last guess ({last_guess}) was {last_result}.")
    print("")

  last_guess  = input("Enter your guess: ")
  last_result = game.guess(last_guess)


print(f"{last_guess} was correct!")