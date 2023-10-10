guess_history = []
class GuessingGame():
    

    def __init__(self, answer=42):
        self.answer = answer
          
    
    def guess(self, user_guess):

        if user_guess == self.answer:
            guess_history.append(True)
            return f"{user_guess} is correct"

        elif user_guess > self.answer:
            guess_history.append(False)
            return f"{user_guess} is too high"

        elif user_guess < self.answer:
            guess_history.append(False)
            return f"{user_guess} is too low"
    
    def check_recent()