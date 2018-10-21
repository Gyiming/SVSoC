#include <fstream>  

#include <iostream>  

#include <string>

using namespace std;  

int main()  

{  

　　const int len=200;  
    int i;
	char str[200];  
	int length[200];
    ifstream OpenFile("bounding_box_ori.txt");  

　　if (OpenFile.fail())  

    {  

        cout<<"fail"<<endl;  

        exit(0);  

    }  
    
    	OpenFile.getline(str,200);  

    	cout<<str<<endl;  

    	OpenFile.close();  

    //system("pause");  

    return 0;
}  