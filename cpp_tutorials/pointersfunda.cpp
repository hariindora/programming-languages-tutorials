#include <iostream>
#include <string>
using namespace std;

class star
{
    public:
    int var = 15;
    int *p = &var;
};
int main()
{
    star a;
    cout << a.var << endl;
    cout << a.p << endl;
    cout << &a.p << endl;
    cout << *a.p;
}