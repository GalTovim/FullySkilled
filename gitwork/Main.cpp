/*
Gal Tovim 305484677
Yehonatan Binyamini 304817539
Tar Wolfson ***********
Yehuda Leh *************8
*/

#pragma once
#include "person.h"
#include "student.h"
#include "employee.h"
int main() {
	int sizeOfarray, choice;
	Person** arr;
	Student* Stud;
	Employee* Emp;
	string nameStudent, instituteStudent;
	int i, avgPerson, agePerson;
	long idPerson;
	float salaryEmployee;

	cout << "Enter number of Persons: ";
	cin >> sizeOfarray;
	arr = new Person * [sizeOfarray];
	for (i = 0; i < sizeOfarray; i++) {
		printf("Enter [1]Student or [2]Employee: ");
		cin >> choice;
		int flag = true;
		if ((choice != 1) && (choice != 2)) {
			flag = false;
			while (!flag) {
				cout << "Wrong Choice try again." << endl;
				cin >> choice;
				if ((choice == 1) || (choice == 2))
					flag = true;
			}
		}
			if (choice == 1) {
				cout << "Enter Student Name: ";
				cin >> nameStudent;
				cout << "Enter Student ID: ";
				cin >> idPerson;
				cout << "Enter Student Institute: ";
				cin >> instituteStudent;
				cout << "Enter Student Age: ";
				cin >> agePerson;
				cout << "Enter Student Averange: ";
				cin >> avgPerson;
				arr[i] = new Student(avgPerson, instituteStudent, agePerson, nameStudent, idPerson);
			}

			if (choice == 2) {
				cout << "Enter employee Name: ";
				cin >> nameStudent;
				cout << "Enter employee ID: ";
				cin >> idPerson;
				cout << "Enter employee Age: ";
				cin >> agePerson;
				cout << "Enter employee Salary: ";
				cin >> salaryEmployee;
				arr[i] = new Employee(salaryEmployee, agePerson, nameStudent, idPerson);
			}

			//working student is missing here

			
		}
	
		for (i = 0; i < sizeOfarray; i++) {
			cout << "arr[" << i << "] is ";
			arr[i]->WhoAmI();

		}
			/*if (typeid((arr[i])).name() == typeid(Student*).name())
				cout << "arr[" << i << "]Is Student" << endl;
			else if (typeid((arr[i])) == typeid(Employee*))
				cout << "arr[" << i << "] Is Employee" << endl;
			else cout << "error"<<endl;
			if(Emp = dynamic_cast<Employee*>(arr[i]);
			 (Emp) {  }
			Stud = dynamic_cast<Student*>(arr[i]);
			if (Stud) {  }
		*/
		
		return 0;
	
}