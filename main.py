# Project quiz game
# By Yash Masane
# Date 23/06/2023

# importing all important modules
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# creating a list of objects from class Question
question_bank = []

# creating an object from class Question and appending it to a list question bank
for item in question_data:
    question = Question(item["text"], item["answer"])
    question_bank.append(question)

# creating an object from class QuizBrain
quiz = QuizBrain(question_bank)

# loop for all question
while quiz.still_has_question():
    quiz.next_question()

# printing final statement
print(f"You have completed the quiz\nYou're final score is {quiz.score}/{quiz.question_number}")
