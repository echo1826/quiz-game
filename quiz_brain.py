class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.current_question = 0
        self.score = 0

    def next_question(self):
            current = self.questions[self.current_question]
            user_answer = input(f"Q.{self.current_question + 1}: {current.question} (True/False)? ")             
            self.current_question += 1
            self.check_answer(user_answer, current.answer)
    
    def has_question(self):
        if self.current_question >= len(self.questions):
            return False
        return True

    def check_answer(self, input, answer):
        if input.lower() == answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer was {answer}")
        print(f"Your current score is: {self.score}/{self.current_question}")

