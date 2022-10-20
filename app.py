from quiz_class import Question

"""
questions goes here
"""
question_prompts = [
    "1. Who developed Python Programming Language?\n a) Wick van Rossum\nb) Rasmus Lerdorf\nc) Guido van Rossum\nd) Niene Stom\n\n" ,
    "2. Which type of Programming does Python support?\n a) object-oriented programming\n b) structured programming\n c) functional programming\n d) all of the mentioned\n\n" ,
    "3. Is Python case sensitive when dealing with identifiers?\n a) no\n b) yes\n c) machine dependent\n d) none of the mentioned\n\n " ,
]

"""
question_prompt called quiz_class
"""
questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "a"),
]

"""
function that execute question, take in answers and print the score
"""
def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + "  correct")

run_quiz(questions)