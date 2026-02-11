#ex 4

def grading(score):
    if 7 <= score <= 8.9 :
        print ( f"Score {score} -> B")
    elif 5 <= score <= 6.9 :
        print ( f"Score {score} -> C")
    elif 3 <= score <= 4.9 :
        print ( f"Score {score} -> D")
    elif score <= 2.9 :
        print ( f"Score {score} -> F")
    elif score >= 9:
        print (f"Score {score} -> A")

n_1 = grading(9.5)
n_2 = grading(7.0)
n_3 = grading(5.5)
n_4 = grading(3.2)
n_5 = grading(1.0)
