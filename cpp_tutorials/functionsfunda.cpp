#include <iostream>
#include <string>
using namespace std;

class FunFunda
{
    // call by value & return by value
    public:
    int addition(int a, int b)
    {
        int c=a+b;
        return c;
    }

    // call by reference & return by reference
    // int& subtraction(int &a, int &b)
    // {
    //     int c=a+b;
    //     return c;
    // }
};
int main()
{
    int x, y, z;
    cout << "Enter 1st number" << endl;
    cin >> x;
    cout << "Enter 2nd number" << endl;
    cin >> y;

    FunFunda funfunda;

    z = funfunda.addition(x, y);
    cout << "The sum of " << x << " and " << y << " is " << z;

    // *z = funfunda.subtraction(x, y);
    // cout << "The sum of " << x << " and " << y << " is " << &z;
    // return 0;
}
