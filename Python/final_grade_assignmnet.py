def main():
    data = {
        'tests': [],
        'programs': [],
        'labs': [],
        'exercises': [],
        'attendance': []
    }

    while True:
        command = input("Enter command (type help to see all commands): ").lower()
        if command == 'help':
            print_help()
        elif command == 'enter':
            enter_data(data)
        elif command == 'average':
            calculate_average(data)
        elif command == 'grade':
            calculate_grade(data)
        elif command == 'exit':
            print("Exiting program ...")
            break
        else:
            print("Invalid command", command)

def print_help():
    help_text = '''Commands:
    help:    print this command list
    enter:   enter values for one type of assignment
    average: calculate/print average for one type of assignment
    grade:   calculate/print letter grade based on assignment scores
    exit:    exit program'''
    print(help_text)

def enter_data(data):
    category_limits = {
        'tests': 3,
        'programs': 7,
        'labs': 9,
        'exercises': 9,
        'attendance': 1
    }

    while True:
        category = input("Category to enter (tests, programs, labs, exercises, attendance): ").lower()
        if category in category_limits:
            break
        else:
            print("Invalid category", category)

    limit = category_limits[category]
    for i in range(limit):
        if category == 'attendance':
            score = int(input(f"Enter attendance score (0-5): "))
        else:
            score = int(input(f"Enter score {i+1} (0-100): "))
        data[category].append(score)

def calculate_average(data):
    while True:
        category = input("Enter category to average (programs, labs, exercises): ").lower()
        if category in ['programs', 'labs', 'exercises']:
            break
        else:
            print("Invalid category", category)
    try:
        total = sum(data[category])
        average = total / len(data[category])
        print(f"Average for {category}: {average:.2f}")
    except ZeroDivisionError:
        print("No scores entered for", category)
        
def calculate_grade(data):
    try:
        lab_avg = sum(data['labs']) / len(data['labs']) * 0.2
        program_avg = sum(data['programs']) / len(data['programs']) * 0.2
        exercise_avg = sum(data['exercises']) / len(data['exercises']) * 0.1
        attendance = data['attendance'][0] * 1
        sorted_tests = sorted(data['tests'], reverse=True)
        highest_test = sorted_tests[0] * 0.15
        other_tests = (sorted_tests[1] + sorted_tests[2]) * 0.1

        weighted_avg = lab_avg + program_avg + exercise_avg + attendance + highest_test + other_tests
        letter_grade = get_letter_grade(weighted_avg)

        print(f"Weighted average: {weighted_avg:.2f}")
        print(f"Letter grade: {letter_grade}")
    except ZeroDivisionError:
        print("enter scores for all assignments before calculating grade")

def get_letter_grade(average):
    try:
        rounded_average = round(average)
        if rounded_average >= 90:
            return 'A'
        elif rounded_average >= 80:
            return 'B'
        elif rounded_average >= 70:
            return 'C'
        elif rounded_average >= 60:
            return 'D'
        else:
            return 'F'
    except ZeroDivisionError:
        print("enter scores for all assignments before calculating grade")

if __name__ == "__main__":
    main()
