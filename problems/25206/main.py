score = [list(map(str, input().split())) for _ in range(20)]
abs_score = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}
all_score = 0
all_grade = 0
one_score = 0
one_grade = 0
for a, b, c in score:
    if c == "P":
        pass
    else:
        one_grade = float(b)
        all_grade += one_grade
        one_score = abs_score[c]
        all_score += one_grade * one_score

# print(round(all_score / all_grade, 6))
print(f"{all_score/all_grade:.6f}")




