#include <iostream>
#include <conio.h>

using namespace std;

class stack
{
    int stk[5];
    int top;
    public:
    void display();
    stack()
    {
        top=-1;
    }

    void push(int x)
    {
        if(top>4)
        {
            cout<<"Stack overflow";
            return;
        }
        stk[++top]=x;
        cout<<"Inserted: "<<x<<endl;
    }

    void pop()
    {
        if(top<0)
        {
            cout<<"Stack underflow";
            return;
        }
        cout<<"Deleted: "<<stk[top--]<<endl;
    }
};

void stack::display()
{
    if(top<0)
    {
        cout<<"Stack empty";
        return;
    }
    else
    {
        for(int i=top;i>=0;i--)
        {
            cout<<stk[i]<<" ";
        }
    }
}

int main()
{
    stack s;
    int ch, x;
    while(1)
    {
        cout<<"\n1. Insert \n2. Delete \n3. Display \n4. Exit \nEnter your choice: ";
        cin>>ch;
        switch(ch)
        {
            case 1:
                cout<<"Enter element: ";
                cin>>x;
                s.push(x);
                break;
            case 2:
                s.pop();
                break;
            case 3:
                s.display();
                break;
            case 4:
                exit(0);
            default:
                cout<<"Invalid choice";
        }
    }
    getch();
    return 0;
}
