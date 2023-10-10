import random


class GuessingGame():
    

    def __init__(self, answer=42):
        self.answer = answer
        self.guess_history = []
          
    def __str__(self):
        return f"the answer is {self.answer}"
    
    
    def guess(self, user_guess):
        correct = user_guess == self.answer
        self.record_guess(user_guess, correct)
        
        if correct:
            return f"{user_guess} is correct"
        elif user_guess > self.answer:
            return f"{user_guess} is too high"
        else:
            return f"{user_guess} is too low"

    def record_guess(self, guess, correct):
        self.guess_history.append((guess, correct))

    def solved(self):
        if self.guess_history:
            _, correct = self.guess_history[-1]
            return correct
        return False


game = GuessingGame(random.randint(1,100))
last_guess  = None
last_result = None

while game.solved() == False:
  if last_guess != None: 
    print(f"Oops! Your last guess ({last_guess}) was {last_result}.")
    print("")

  last_guess  = int(input("Enter your guess: "))
  last_result = game.guess(last_guess)


print(f"{last_guess} was correct!")

    

