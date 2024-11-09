// File is created with given name & information is stored in that file / File Handling

#include <stdio.h>
#include <string.h>

int main()
{
	FILE* fptr;
	char name[20];
	int age;
	float salary;

	fptr=fopen("emp.txt","w");

	if(fptr==NULL)
	{
		printf("file does not exist in");
		return 1;
	}
	printf("Enter the name :- ");
	scanf("%s",name);
	fprintf(fptr,"name=%s\n",name);
	printf("Enter the age :- ");
	scanf("%d",&age);
	printf("Enter the Salary :- ");
	scanf("%f",&salary);
	fprintf(fptr,"Salary=%2f\n",salary);
	fclose(fptr);
	return 0;
}