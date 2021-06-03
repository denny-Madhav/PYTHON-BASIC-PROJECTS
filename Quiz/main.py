from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for i in question_data:
    qt=i["text"]
    at=i["answer"]
    newq=Question(qt,at)
    question_bank.append(newq)
quiz=QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.nq()

print("You have completed the quiz.")
print(f"Your final score is {quiz.score}/{quiz.qn}.\n")


