from quiz_model import QuizModel
from quiz_view import QuizView
from quiz_controller import QuizController

if __name__ == "__main__":
    model = QuizModel()
    view = QuizView()
    controller = QuizController(model, view)
    controller.run_quiz()