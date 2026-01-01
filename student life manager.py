'''name:FASIKA GASHAW'''  '''ID :BITS/UGR/0040/26'''
# Student Life Manager


def calculate_average(total, count):
    if count == 0:
        return 0
    else:
        return total / count
 
def evaluate_performance(average):
    if average >= 90:
        return "Excellent"
    elif 70 <= average < 90:
        return "Good"
    else:
        return "Needs Improvement"


def expense_checker(budget, cost):
    if budget >= cost:
        return True
    else:
        return False

def get_grades():
    total = 0
    count = 0
    while True:
        grade_input = input("Enter a grade (or type 'done' to finish): ")
        if grade_input == "done":
            break
        elif grade_input.replace('.', '', 1).isdigit():  
            grade = float(grade_input)
            total += grade
            count += 1
        else:
            print("Invalid input. Please enter a number or 'done'.")
    return total, count


def main():
    name = input("Enter your name: ")
    budget = float(input("Enter your monthly budget: "))

    total_grades, grade_count = get_grades()

    average = calculate_average(total_grades, grade_count)
    performance = evaluate_performance(average)

    celebration_cost = float(input("Enter celebration meal cost: "))
    affordable = expense_checker(budget, celebration_cost)


    
    print("STUDENT REPORT")
    print("Name:", name)
    print("Subjects:", grade_count)
    print("Average Grade:", round(average, 2))
    print("Performance:", performance)
    if affordable:
        print("Celebration: You can afford the meal")
    else:
        print("Celebration: You cannot afford the meal")

main()


