#include <iostream>
#include <string>
using namespace std;
#define max 5

int a[max], top = -1;
void push();
void pop();
void disp();

void main()
{
    int ch;
    cout<<"1. push or insert"<<endl;
    cout<<"2. pop or delete"<<endl;
    cout<<"3. display"<<endl;
    cout<<"4. end programe"<<endl;

    while true
    {
        cout<<"enter choice";
        cin>>"%d",&ch;
        switch (ch)
        {
            case 1:
            {
                push();
                break;
            }

            case 2:
            {
                pop();
                break;
            }

            case 3:
            { 
                display();
                break;
            }
            case 4:
            {
                exit(0);
                break;
            }

            default:
            {
                cout<<"Wrong choice";
            }
        }
    }
}
void push()
{
    int data;
    if (top == max-1)
    {
        cout<<"\n stack is full or overflow";
    }
    else
    {
        cout<<"enter element to be pushed";
        cin>>"%d",data;
        top++;
        a[top]=data;
    }
    
}
void pop()
{
    int data;
    if (top == -1)
    {
        cout<<"\n stack is empty or underflow";
    }
    else
    {
        cout<<"enter element to be poped";
        cin>>"%d",a[top];
        top--;
    }
}
void display()
{
    int i;
    if (top >= 0)
    {
        cout<<"elements";
        for(i=top; i>=0; i--)
        {
            cout<<"%d",a[i];
        }
    }
    else
    {
        cout<<"stack is empty";
    }
}    