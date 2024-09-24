import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="den"
)

cursor = db.cursor()

# Function to add a new patient
def add_patient(name, age, gender, contact, address):
    sql = "INSERT INTO patients (name, age, gender, contact, address) VALUES (%s, %s, %s, %s, %s)"
    val = (name, age, gender, contact, address)
    cursor.execute(sql, val)
    db.commit()
    print(f"Patient {name} added successfully.")

# Function to view all patients
def view_patients():
    cursor.execute("SELECT * FROM patients")
    result = cursor.fetchall()
    for row in result:
        print(row)

# Function to update patient information
def update_patient(id, name=None, age=None, gender=None, contact=None, address=None):
    sql = "UPDATE patients SET"
    params = []
    if name:
        sql += " name = %s,"
        params.append(name)
    if age:
        sql += " age = %s,"
        params.append(age)
    if gender:
        sql += " gender = %s,"
        params.append(gender)
    if contact:
        sql += " contact = %s,"
        params.append(contact)
    if address:
        sql += " address = %s,"
        params.append(address)
    
    sql = sql.rstrip(",") + " WHERE id = %s"
    params.append(id)
    
    cursor.execute(sql, params)
    db.commit()
    print(f"Patient ID {id} updated successfully.")

# Function to delete a patient
def delete_patient(id):
    sql = "DELETE FROM patients WHERE id = %s"
    cursor.execute(sql, (id,))
    db.commit()
    print(f"Patient ID {id} deleted successfully.")

# Main menu
def main():
    while True:
        print("\nDental Clinic Management System")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Update Patient")
        print("4. Delete Patient")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter patient name: ")
            age = int(input("Enter patient age: "))
            gender = input("Enter patient gender: ")
            contact = input("Enter patient contact number: ")
            address = input("Enter patient address: ")
            add_patient(name, age, gender, contact, address)
        
        elif choice == '2':
            view_patients()
        
        elif choice == '3':
            id = int(input("Enter patient ID to update: "))
            print("Enter new details (leave blank to keep current):")
            name = input("New name: ")
            age = input("New age: ")
            gender = input("New gender: ")
            contact = input("New contact number: ")
            address = input("New address: ")
            update_patient(id, name or None, age or None, gender or None, contact or None, address or None)
        
        elif choice == '4':
            id = int(input("Enter patient ID to delete: "))
            delete_patient(id)
        
        elif choice == '5':
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
1