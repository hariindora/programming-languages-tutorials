#include <iostream>
#include <string>
using namespace std;

class laptop
{
    public:
        string name;
        float price;
        string cpu;
};

class gaiminglaptop: public laptop
{
    public:
        void getdata()
        {
            cout<<"Name : ";
            cin>>name;
            cout<<"Price : ";
            cin>>price;
            cout<<"CPU : ";
            cin>>cpu;
        }

        void putdata()
        {
            cout<<"Name: "<<name<<endl;
            cout<<"Price: "<<price<<endl;
            cout<<"CPU: "<<cpu<<endl;
        }
};
int main()
{
    gaiminglaptop lap1;
    lap1.getdata();
    lap1.putdata();
}