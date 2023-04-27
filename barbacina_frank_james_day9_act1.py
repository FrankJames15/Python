'''
1. Create a Record Keeping App It will display the following options
  a.Add Record
  b.View Records
  c.Clear All Records
  d.Exit
3. If A: The user will input thefollowing information (name, email, address)
4. The app will save theinformation in a text file.
5. If B, display the saved records
6. If C, clear the text file anddisplay “No records found.”
7. If D, display “Thank you”
8. Save your file as lastname_firstname_day9_act1.py 
'''

def add_record():
    name = input("Enter name: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    with open("records.txt", "a") as records:
        records.write(name + "," + email + "," + address + "\n")

def view_records():
    with open("records.txt", "r") as records:
        # check if file is empty
        if records.read() == '':
            print("No records found.")
        else:
            # read from the beginning of the file
            records.seek(0)
            print(records.read())


def clear_records():
    with open("records.txt", "w") as records:
        records.write('')

def exit_program():
    print("Thank you.")

def main():
    while True:
        print("\nRecord Keeping App")
        print(" a. Add Record")
        print(" b. View Records")
        print(" c. Clear All Records")
        print(" d. Exit")

        choice = input("Enter choice: ")

        if choice == "a":
            add_record()
        elif choice == "b":
            view_records()
        elif choice == "c":
            clear_records()
        elif choice == "d":
            exit_program()
            break # exit the loop
        else:
            print("Invalid choice.")

        input("Press enter to continue...")

main()