#include <iostream>
#include <string>

using namespace std;

class Student
{
    string name;
    int marks;
    public:
        void getname()
            {
                cin >> name;
            }
        void getmarkes()
            {
                cin >> marks;
            }
        void displayinfo()
            {
                cout << "name : " << name << endl;
                cout << "marks : " << marks <<endl << endl;
            }
};

// int main()
// {
//     Student st;
//     st.getname();
//     st.getmarkes();
//     st.displayinfo();
// }

int main()
{
    Student st[5];   
    for (int i=0; i<5; i++)
    {
        cout << "student" << i+1 << endl;
        cout << "Enter Name" << endl;
        st[i].getname();
        cout << "Enter Marks" << endl;
        st[i].getmarkes();
    }

    for (int i=0; i<5; i++)
    {
        cout << "student" << i+1 << endl;
        st[i].displayinfo();
    }
    return 0;
}