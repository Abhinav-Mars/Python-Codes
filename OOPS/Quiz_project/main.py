from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []

for ques in question_data:
    question_bank.append(Question(ques["text"],ques["answer"]))
    
start_quiz = QuizBrain(question_bank)

start_quiz.if_ques_remain()

print(f"Your score is = {start_quiz.score}/{len(question_bank)}")