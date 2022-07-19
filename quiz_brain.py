class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.current_question = 0

    def next_question(self):
        self.current_question += 1

    def ask_question(self):
        while True:
            user_answer = input(f"Q.{self.current_question + 1}: {self.questions[self.current_question]} (True/False)? ")
            if user_answer != 'True' or user_answer != 'False':
                print("Please answer either True, or False.")
                continue
            else:
                return user_answer