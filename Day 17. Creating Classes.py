# CREATING CLASSES
#
# class User:
#    def __init__(self, user_id, username):
#         self.username = username
#         self.follower = 0
#         self.following = 0


#     def follow(self, user):
#         user.follower += 1
#         self.following += 1
#
#
# user_1 = User("001", "phensic")
# user_2 = User("002", "oscar")
#
# user_1.follow(user_2)
#
# print(user_1.follower)
# print(user_1.following)
# print(user_2.follower)
# print(user_2.following)

# TRUE / FALSE GAME

question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {
        "text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home "
                "to eat.",
        "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.",
     "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]


# TODO 1. CREATE A QUESTION CLASS FROM SCRATCH
class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


# TODO 2. CREATE A QUESTION BANK OF  QUESTIONS AND ANSWERS

# import random
#
#
# class QuestionBank:
#
#     def __init__(self, question, answer):
#         choice = random.choice(question_data)
#         for texts in choice:
#             question = texts["text"]
#             answer = texts["answer"]
#
#
# print(QuestionBank.question)
# print(QuestionBank.question)

Question_bank = []
for questions in question_data:
    question_text = questions["text"]
    question_answer = questions["answer"]
    new_question = Question(question_text, question_answer)
    Question_bank.append(new_question)


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer is {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")


quiz = QuizBrain(Question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

# FINITE