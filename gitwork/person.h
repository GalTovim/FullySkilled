#ifndef PERSON_H
#define PERSON_H

#include <iostream>
#include <string>
using namespace std;

class Person
{
protected:
	string Name; //10 chars maximum
	long ID;
	int Age;

public:
	Person(const Person &p1);
	Person(string Name, long ID, int Age);
	~Person();
};
#endif // !PERSON_H
