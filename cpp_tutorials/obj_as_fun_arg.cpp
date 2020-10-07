#include <iostream>
#include <string>
using namespace std;

class weight
{
    int kilogram;
    int gram;

    public:
    void getdata();
    void putdata();
    void sum_weight(weight, weight);
};
void weight::getdata()
{
    cout<<"Kilograms: ";
    cin>>kilogram;
    cout<<"Grams: ";
    cin>>gram;
}
void weight::sum_weight(weight w1, weight w2)
{
    gram = w1.gram + w2.gram;
    kilogram = gram/1000;
    gram = gram%1000;
    kilogram = w1.kilogram + w2.kilogram;
    
}
void weight::putdata()
{
    cout<<kilogram<<"kgs and "<<gram<<"grams"<<endl;
}

int main()
{
    weight w1, w2, w3;
    cout<<"enter weight #1"<<endl;
    w1.getdata();
    cout<<endl<<"enter weight #2"<<endl;
    w2.getdata();
    w3.sum_weight(w1, w2);
    
    cout<<endl<<"weight #1=";
    w1.putdata();
    cout<<"weight #2=";
    w2.putdata();
    cout<<endl<<"total weight = ";
    w3.putdata();
    return 0;
}

