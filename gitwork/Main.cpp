/*
Gal Tovim 305484677
Yhonatan Binyamini **********
Tar Wolfson ***********
Yehuda Leh *************8
*/
#pragma once
#include "person.h"
#include "student.h"
#include "employee.h"

int Main(){
    int sizeOfarray,choice;
    Person** arr;
    Student* Stud;
    Employee* Emp;

    string nameStudent, instituteStudent;
    int i,avgPerson,agePerson;
    long idPerson;
    float salaryEmployee;

    cout<<"Enter number of Persons: ";
    cin >> sizeOfarray;
    arr = new Person*[sizeOfarray];
    
    for (i=0 ; i<sizeOfarray ; i++){
        printf("Enter [1[Employee or [2]Student: ");
        scanf("%d", &choice);
        if (choice == 1){
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
            arr[i]= new Student(avgPerson,instituteStudent,agePerson,nameStudent,idPerson);
        }
        if (choice == 2){
            cout << "Enter Student Name: ";
            cin >> nameStudent;
            cout << "Enter Student ID: ";
            cin >> idPerson;
            cout << "Enter Student Age: ";
            cin >> agePerson;
            cout << "Enter Employee Salary: ";
            cin >> salaryEmployee;
            arr[i]= new Employee(salaryEmployee,agePerson,nameStudent,idPerson);
        }
        int flag = true;
        if ((choice != 1)&&(choice != 2))
            while(flag){
                cout << "Wrong Choice try again." << endl;
                cin >> choice;
                if ((flag == 1)||(flag == 2))
                    flag = false;
            }
    }
    for (i = 0; i < sizeOfarray; i++){
        Emp = dynamic_cast <Employee*>(arr[i]);
		if (Emp){ cout << "arr[" << i << "] Is Employee" << endl; }
		Stud = dynamic_cast<Student*>(arr[i]);
		if (Stud){ cout << "arr[" << i << "]Is Student" << endl; }
	}
    return 0;
}
