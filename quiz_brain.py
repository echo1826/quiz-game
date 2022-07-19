class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.current_question = 0

    def next_question(self):
        while True:
            user_answer = input(f"Q.{self.current_question + 1}: {self.questions[self.current_question].question} (True/False)? ")
            if user_answer != 'True' and user_answer != 'False':
                print("Please answer either True or False.")
                continue
            else:
                self.current_question += 1                
                return user_answer
    
    def has_question(self):
        if self.current_question >= len(self.questions):
            return False
        return True
