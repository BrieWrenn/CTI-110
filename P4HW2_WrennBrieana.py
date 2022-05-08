# CTI-110
# P4HW2 - Pizza Order
# Brieana Wrenn 
# 4/5/2022
#
def main():

        # Ask user to enter number of students she/he would like to order pizza for
        students = int(input('How many students to order pizza for? '))
        # Ask user for number of people that will be sharing each pizza ( 1.5, 2 or 3)
        people = float(input('Enter number of people per pizza (1.5, 2 or 3): '))
        # while loop
        while people != 1.5 and people != 2 and people != 3:
                print("INVALID ENTRY!!")
 
                print("Should have entered 1.5, 2 or 3")
 
                print()
 
                people = float(input("Enter number of people per pizza again. (1.5, 2 or 3): "))

                
        # If user enters a correct value ( 1.5, 2, or 3)
        if people == 1.5 or people == 2 or people ==3:
                whole_pizzas = students / people
                price = whole_pizzas * 5
                price = price + (price * 0.06)
                # WHAT DO I DO HERE TO MAKE IT ROUND EVENLY?
        print('----Pizza Order-------')
        print('Number of Students: ', students)
        print('Pizzas Needed: ', whole_pizzas)
        print('Price: $', price)
        print('-----------------------')
 # ask user if they want to run the program again and to answer by entering N or Y
        print('Would you like to run program again type (Y for yes)')
        # Program only terminates if user chooses NOT to run program again. (HOW?)
main()

