import datetime
attendence={}
students={}
def Add_student():   
            print("Adding a new student.")
            name = input("Enter your Name: ").capitalize()
            roll_no = input("Enter your Roll Number: ").upper()
            date_added = datetime.datetime.now()
            students[name] = {'roll_no': roll_no, 'date_added': date_added}
    
            file= open("student.txt", "a")
            file.write(f"{name}, {roll_no}, {date_added}\n")
    
            print(f"Student {name} with Roll No {roll_no} added successfully.")
def mark_attendence():
    print("mark attendence.".capitalize())
    name = input("Enter your Name: ").capitalize()
    if name in students:
            status = input("Mark attendance (present/absent): ").lower()
            date = datetime.datetime.now().strftime("%Y-%m-%d")
        
    if name not in attendence:
            attendence[name] = []
        
    attendence[name].append({'date': date, 'status': status})
        
    file= open("attendance.txt", "a")
    file.write(f"{name}, {date}, {status}\n")       
    print(f"Attendance marked for {name} on {date} as {status}.")

def view_attendence():
    name = input("Enter student name: ").capitalize()
    if name in attendence:
            print(f"Attendance for {name}:")
            for record in attendence[name]:
                print(f"Date: {record['date']}, Status: {record['status']}")
    else:
                print(f"No attendance records found for {name}.")

def view_attendence_for_all_student():
        if attendence:
            for name, records in attendence.items():
               print(f"Attendance for {name}:")
            for record in records:
                print(f"  Date: {record['date']}, Status: {record['status']}")
            print()
        else:
            print("No attendance records available.")

print("Wellcome In our student management system.")
def studen_attendence_system():        
    while True:
        print("1. Adding a new student.")
        print("2. Marking attendance.")
        print("3. Viewing attendance for a specific student.")
        print("4. Viewing attendance for all students.")
        print("5. Exiting the system.")

        choice = int(input("Enter your choice(1-5):"))

        if choice==1:
              Add_student()
        elif choice==2:
              mark_attendence()
        elif choice==3:
              view_attendence()
        elif choice==4:
              view_attendence_for_all_student()
        elif choice==5:
                print("Exiting the system, Good Bye!")
                break
        else:
            print("invalid choice!")
studen_attendence_system ()
input("press enter to exit.......")



                    