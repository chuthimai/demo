class QuizBrain:
    def __init__(self, list):
        self.question_number = 0
        self.question_list = list
        self.user_score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number +=1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)? ").lower()
        self.check_answer(user_answer, current_question.answer)

    def still_has_question(self):
        if self.question_number == len(self.question_list):
            return False
        else:
            return True

    def check_answer(self, user_answer, current_question_answer):
        if user_answer == current_question_answer.lower():
            print("You got it right!")
            self.user_score += 1
            print(f"Your current score: {self.user_score}/{self.question_number}\n")
        else:
            print("That's wrong.")
            print(f"Your current score: {self.user_score}/{self.question_number}\n")


