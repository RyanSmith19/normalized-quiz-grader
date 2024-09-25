import string
import re

class QuestionAnswer:
    def __init__(self, question, answer):
        self.question = question
        self.answer = re.sub(r'[^\w\s]', '', answer.lower())

class QuizModel:
    def __init__(self):
        self.questions_and_answers = [
            QuestionAnswer("What is the capital of France?", "Paris"),
            QuestionAnswer("Who painted the Mona Lisa?", "Leonardo da Vinci"),
            # ... other questions and answers
        ]
        self.current_question_index = 0
        self.score = 0

    def get_current_question(self):
        return self.questions_and_answers[self.current_question_index]

    def check_answer(self, user_answer):
        user_answer = user_answer.lower().translate(str.maketrans('', '', string.punctuation))  # Normalize user answer
        correct_answer = self.questions_and_answers[self.current_question_index][1].lower()

        if user_answer == correct_answer:
            self.score += 1
        self.current_question_index += 1

    def is_quiz_over(self):
        return self.current_question_index >= len(self.questions_and_answers)

    def calculate_percentage_correct(self):
        total_questions = len(self.questions_and_answers)
        return (self.score / total_questions) * 100

    def did_user_pass(self, passing_percentage=80):
        return self.calculate_percentage_correct() >= passing_percentage