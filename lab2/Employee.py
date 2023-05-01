import mysql.connector

try:

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database='northwind',

    )
except Exception as e:
    print(e)

cur = mydb.cursor()
cur.execute('''drop table if exists employees''')
cur.execute('''create table employees(
            ID int primary key not null,
            first_name text not null,
            last_name text not null,
            age int not null,
            department char(50) not null,
            salary int not null,
            managed_department char(50)
            );''')
mydb.commit()


class Employee:
    all_employees = []
    id = 0

    def __init__(self, first_name, last_name, age, department, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.department = department
        self.salary = salary
        Employee.id += 1
        self.id = Employee.id
        cur.execute(f'''Insert into employees(ID, first_name, last_name, age, department, salary)
             values({Employee.id}, '{self.first_name}', '{self.last_name}', {self.age}, '{self.department}', {self.salary})
             ''')
        mydb.commit()
        Employee.all_employees.append(self)

    def transfer(self, department):
        self.department = department
        cur.execute(
            f"Update employees set department='{department}' where first_name='{self.first_name}' and last_name='{self.last_name}'")
        mydb.commit()

    def fire(self):
        Employee.all_employees.remove(self)
        cur.execute(
            f"delete from employees  where first_name='{self.first_name}' and last_name='{self.last_name}' ")
        mydb.commit()

    def show(self):
        cur.execute(
            f"select * from employees where first_name='{self.first_name}' and last_name='{self.last_name}'")
        rows = cur.fetchone()
        print(rows[0], rows[1], rows[2], rows[3], rows[4])
        mydb.commit()

    @classmethod
    def list_employees(cls):
        for employee in Employee.all_employees:
            employee.show()
            print("\n")


class Manager(Employee):
    all_managers = []

    @classmethod
    def list_managers(cls):
        for manager in Manager.all_managers:
            manager.show()
            print("\n")

    def __init__(self, first_name, last_name, age, department, salary, managed_department):
        super().__init__(first_name, last_name, age, department, salary)
        self.managed_department = managed_department
        cur.execute(
            f"Update employees set managed_department='{self.managed_department}' where first_name='{self.first_name}' and last_name='{self.last_name}'")
        Manager.all_managers.append(self)
        mydb.commit()

    def show(self):
        print(f"""
        First Name:{self.first_name}
        Last Name:{self.last_name}
        Age:{self.age}
        Managed Department:{self.managed_department}
        Salary:Confidential""")

    def fire(self):
        Employee.all_employees.remove(self)
        Manager.all_managers.remove(self)
        cur.execute(
            f"Delete from employees where first_name='{self.first_name}' and last_name='{self.last_name}'")
        mydb.commit()


def input_data(type):
    first_name = input(f"\nEnter {type} first_name: ")
    last_name = input(f"\nEnter {type} last_name: ")
    age = int(input(f"\nEnter {type} age: "))
    department = input(f"\nEnter {type} department: ")
    salary = float(input(f"\nEnter {type} salary: "))
    if type == "employee":
        return [first_name, last_name, age, department, salary]
    else:
        managed_department = input(f"\nEnter {type} managed department: ")
        return [first_name, last_name, age, department, salary, managed_department]


while True:
    print("Please enter number of operation:")
    print("1- Add new employee")
    print("2- List all employees")
    print("3- List all managers")
    print("4- Exit program")
    key = eval(input())
    if key == 1:
        type = input(
            "Press (m) if employee is a manager\nPress (e) if an employee\n")
        if type == "m":
            data = input_data("manager")
            Manager(*data)
        else:
            data = input_data("employee")
            Employee(*data)
    elif key == 2:
        Employee.list_employees()
    elif key == 3:
        Manager.list_managers()
    elif key == 4:
        break
