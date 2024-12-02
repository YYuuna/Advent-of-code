with open("day-6-input.txt", "r") as puzzle_input:
    answred_questions_sum=0
    group_questions_sets =[[set(person_q) for person_q in group_q.split('\n')]
                           for group_q in puzzle_input.read().split('\n\n')]
    for group_questions in group_questions_sets:

        commun_answred_questions =group_questions[0]
        for answred_questions in group_questions[1:]:
            commun_answred_questions&=answred_questions
        answred_questions_sum+=len(commun_answred_questions)
    print(answred_questions_sum)



