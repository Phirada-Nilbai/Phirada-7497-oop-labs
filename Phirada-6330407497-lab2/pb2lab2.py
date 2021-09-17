#Phirada Nilbai 633040749-7
def get_student_id():
    id = int(input("Please enter your student ID: "))
    return id


def get_midterm_scores():
        try :
            midterm_exam = float(input("Please enter student's midterm exam mark(0-100): "))
            return midterm_exam
        except ValueError:
            print("Please enter a score as a decimal number")


def get_final_score():
        try :
            final_exam = float(input("Pleas enter student's final exam mark(0-100): "))
            return final_exam
        except ValueError:
            print("Please enter a score as a decimal number")



def compute_final_score(midterm_exam, final_exam):
    score = 0.4 * midterm_exam + 0.6 * final_exam
    return score




def get_letter_grade(finalized_score):
    if 80 <= finalized_score <= 100:
        letter_grade = 'A'
    elif 70 <= finalized_score <= 80:
        letter_grade = 'B'
    elif 60 <= finalized_score <= 70:
        letter_grade = 'C'
    elif 50 <= finalized_score <= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'
    return letter_grade


if __name__ == '__main__':
    student_id = get_student_id()
    mid = get_midterm_scores()
    fin = get_final_score()
    final_score = compute_final_score(mid,fin)
    grade = get_letter_grade(final_score)
    print("Student ID:",student_id,"has total score mark as "+str(final_score))
    print("has a grade as:" +str(grade))
