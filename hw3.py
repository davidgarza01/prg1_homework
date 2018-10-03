
# The goal of this homework assignment is to flex your lists, strings, and string manipulation skills we are learning in class
# Avoid writing any loops (aside from the one I have provided for you).

print('''
Welcome to Saint John's Northwestern Military Academy!
This is your Academic Planner Program that will help you keep your assignments in line
''')

homework_to_do=[]
homework_due_dates=[]

tests_quizzes=[]
tests_quiz_dates=[]

while(True):
    '''
    problem 1)
    '''
    print('''
    1) Add Homework 
    2) Add quiz / test 
    3) Display all homework, quizzes, and tests 
    ''')
    choice = int(input("?"))

    if(choice == 1):
        homework = input("What is your homework?")
        hw_date = input("When is your homework due?")
        homework_to_do.append(homework)
        homework_due_dates.append(hw_date)
        print("Adding Homework")
    elif(choice == 2):
        quiz = input("What is your quiz/test?")
        quiz_date = input("When is your quiz/test due?")
        tests_quizzes.append(quiz)
        tests_quiz_dates.append(quiz_date)
        print("Adding quiz/test")
    elif(choice == 3):
        print(homework_to_do)
        print(homework_due_dates)
        print(tests_quizzes)
        print(tests_quiz_dates)
        
     

