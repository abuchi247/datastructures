Students = [
    ["abuchi", "20"],
    ["Tom", "50"],
    ["Jerry", "70"],
    ["abuchi", "80"],
    ["Goofy", "30"],
    ["Thomas", "70"]
]
student_table = {}

def get_average(scores):
    return sum_scores(scores) / len(scores)


def sum_scores(scores):
    total = 0
    for score in scores:
        total += score
    return total

for student in Students:
    name = student[0]
    score = int(student[1])
    if name in student_table:
        student_table[name].append(score)
    else:
        student_table[name] = [score]

max_score = -1
max_student_score = {}
for name in student_table:
    avg_score = get_average(student_table[name])
    if avg_score >= max_score:
        max_score = avg_score
        if avg_score in max_student_score:
            max_student_score[avg_score].append(name)
        else:
            max_student_score[avg_score] = [name]

print(f"Max score: {max_score}, students with that score: {max_student_score[max_score]}")
