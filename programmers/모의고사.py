def solution(answers):
    def check_ans(student, answers):
        correct = 0
        for i in range(len(answers)):
            if answers[i] == student[i % len(student)]:
                correct += 1
        
        return correct
    
    student1 = [1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5]
    scores = [0] * 3
    result = []
    
    for i, answer in enumerate(answers):
        if answer == student1[i % len(student1)]:
            scores[0] += 1
        if answer == student2[i % len(student2)]:
            scores[1] += 1
        if answer == student3[i % len(student3)]:
            scores[2] += 1

    for i, score in enumerate(scores):
        if score == max(scores):
            result.append(i+1)

    return result