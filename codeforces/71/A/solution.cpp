#include <iostream>
#include <string>
#include <vector>
using namespace std;
int main()
{
    string a;
    int n;
    cin >> n;
 
    while (n--)
    {
        cin >> a;
        int len = a.size();
        if (len > 10)
        {
            cout << a[0] << len - 2 << a[len - 1] << endl;
        }
        else
        {
            cout << a << endl;
        }
    }
}