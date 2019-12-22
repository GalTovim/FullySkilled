#include "person.h"
Person::Person() {
	Name = "";
	ID = NULL;
	Age = NULL;
}

Person::Person(const Person& p1)
{
	Name = p1.Name;
	ID = p1.ID;
	Age = p1.Age;
}

Person::Person(string Name, long ID, int Age)
{
	this->Name = Name;
	this->ID = ID;
	this->Age = Age;
}
Person::~Person()
{	cout << "**************************** P dtor" << endl;
}