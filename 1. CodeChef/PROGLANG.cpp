#include<bits/stdc++.h>
using namespace std;

int main()
{

   int t, a, b, a1, b1, a2, b2;
   cin >>t;
   while (t--)
   {
       cin >> a >> b >> a1 >> b1 >>a2 >> b2;
       if(((a1 == a) || (a1 == b)) && ((b1 == a) || (b1 == b)))
       {
           cout << 1 << endl;
       }
       else if(((a2 == a) || (a2 == b)) && ((b2 == a) || (b2 == b)))
       {
           cout << 2 << endl;
       }
       else
       {
           cout << 0 << endl;
       }
   }


    system("pause>0");
}
