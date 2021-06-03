
class QuizBrain():
    def __init__(self,QL):
        self.qn=0
        self.ql=QL
        self.score=0

    def still_has_questions(self):
        return self.qn < len(self.ql)


    def nq(self):
        cq = self.ql[self.qn]
        self.qn +=1
        guess = input(f"Q.{self.qn}:{cq.q} (true or false) : ")
        self.check(guess,cq.a)

    def check(self,guess,answer):
        self.a=guess
        self.b=answer
        if self.a.lower() == self.b.lower():
            print("You are correct")
            self.score +=1
        else:
            print("You are wrong")
        print(f"The correct answer was : {answer}.")
        print(f"Your current score is {self.score}/{self.qn}.\n")



