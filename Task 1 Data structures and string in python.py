''' 
1. create a dictionary where a student names are keys and their marks are value
2. Asks the user to inputs a students name
3. Retrieves and displays the corresponding marks
4. If the students name is not found, display an appropriate message
'''

students = {"Kundan" : 98,
            "Alice" : 85}

name = input("Enter the student's name: ")

if name in students:
    print(f"{name}'s marks : {students[name]}")
else:
    print("student not found")