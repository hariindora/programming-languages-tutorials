#include <iostream>
#include <string>
using namespace std;

class cal
{
    float x, y, z;
    public:
    void sum()
    {
        cout << "please enter first number" << endl;
        cin >> x;
        cout << "please enter second number" << endl;
        cin >> y;
        z = x+y;
        cout << "the sum of " << x << " and " << y << " is " << z <<endl;
    }
};

int main()
{
    cal a;
    a.sum();
}

