#include <iostream>
#include <string>
using namespace std;

class star
{
    public:
    void triangle()
    {
        for(int i=5; i>0; i--)
        {   
            for(int j=0; j<i; j++)
            {
                cout << "* ";
            }
            cout << "\n";
        }
    }
    void triangle1()
    {
        for(int i=0; i<=5; i++)
        {   
            for(int j=0; j<i; j++)
            {
                cout << "* ";
            }
            cout << "\n";
        }

    }
};
int main()
{
    star a;
    a.triangle();
    a.triangle1();
}