#pragma once
#include "person.h"
#include "student.h"
#include "employee.h"

int Main(){
    int sizeOfarray,choice;
    Person** arr;

    //student cin parameters
    string nameStudent, instituteStudent;
    int avgPerson,agePerson;
    long idPerson;

    cout<<"Enter number of Persons: ";
    cin >> sizeOfarray;
    arr = new Person*[sizeOfarray];
    
    for (int i=0 ; i<sizeOfarray ; i++){
        printf("Enter [1[Employee or [2]Student: ");
        scanf("%d", &choice);
        if (choice==1){
            cout << "Enter Student Name: ";
            cin >> nameStudent;
            cout << "Enter Student Institute: ";
            cin >> instituteStudent;
            
            arr[i]= new Student();
        }
    }
    return 0;
}
