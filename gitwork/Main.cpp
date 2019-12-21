#pragma once
#include "person.h"
#include "student.h"
#include "employee.h"

int Main(){
    int sizeOfarray;
    char choice;
    printf("Enter number of persons: ");
    scanf("%d", &sizeOfarray);
    Person *arr = new Person[sizeOfarray];
    for(int i=0 ; i<sizeOfarray ; i++){
        printf("Enter [E]mployee or [S]tudent: ");
        scanf("%c", &choice);
        if ((choice == 'E')||(choice == 'e')){
            
        }
        if ((choice == 'S')||(choice == 's')){
            
        }
    }
    return 0;
}
