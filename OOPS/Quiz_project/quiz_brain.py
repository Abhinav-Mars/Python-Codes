class QuizBrain:
    
    def __init__(self,question_list):
        
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        
    def print_next_question_and_compute_score(self):
        
        ans = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} (True/False)?:")
        if ans == self.question_list[self.question_number].answer:
            self.score += 1
            print("Good!!! You got it right\n")
        else:
            print("Nahh!!! That's wrong\n")
        self.question_number += 1
    
    def if_ques_remain(self):
    
        for i in range(len(self.question_list)):
            self.print_next_question_and_compute_score()
                 