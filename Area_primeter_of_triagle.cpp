#include <iostream.h>
#include <math.h>
using namespace std;
double length(double x,double y,double z);
int main()
{ 
	double x,y,z;
	double P,A;
	cout<<"enter 3 numbers: "<<endl;
	cin>>x>>y>>z;
 length(x,y,z);
		return 0;}

double length(double x,double y,double z)
{
	double P,A;
	if(x+y>z && z+y>x && z+x>y)
	{
		cout<<"There are create Triangle!"<<endl;
		P=x+y+z;
		double p=P/2;
		A=sqrt(p*(p-x)*(p-y)*(p-z));
		cout<<"The Perimeter: "<<P<<endl;
		cout<<"The Area: "<<A<<endl;
	}	
	else
	    cout<<"There aren't create Triangle!"<<endl;
	    return A;
	    return P;
}

