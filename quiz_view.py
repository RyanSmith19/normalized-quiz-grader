class QuizView:
    def display_question(self, question):
        print(question)

    def get_user_answer(self):
        return input("Your answer: ").strip().lower()

    def display_result(self, result_text):
        print(result_text)

    def update_view(self):
        print("\n")  # Add a new line for better readability
        question, _ = self.model.get_current_question()
        self.display_question(question)
        user_answer = self.get_user_answer()
        self.model.check_answer(user_answer)