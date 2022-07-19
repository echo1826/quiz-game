import json
from question_model import Question
from quiz_brain import Quiz

file = open('./data.json')
data = json.load(file)

questions = []
# turning data into questions
for item in data:
    questions.append(Question(item["text"], item["answer"]))

quiz_game = Quiz(questions)
while quiz_game.has_question():
    quiz_game.next_question()