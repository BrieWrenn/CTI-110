# P3HW1
# Wrenn
# CTI 110 - 0902
# 3/18/2022

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    
    
    score = float(input('Enter grade: '))

    if score >= A_score:
        print('Your grade is: A')
    else:
        if score >= B_score:
            print('Your grade is: B')
        else:
            if score >= C_score:
                print('Your grade is: C')
            else:
                if score >= D_score:
                    print('Your grade is: D') # TO DO: finish this
                else:
                    print('Your grade is: F')



# program start
main()

