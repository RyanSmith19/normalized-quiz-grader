class QuizController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.update_view()