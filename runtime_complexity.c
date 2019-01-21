#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
//#include <windows.h>

//this program is wrong, it is just for calculate the time complexity.

int check(int i,int Ebudget,int Ea,int Eb,int Ec,int Ed)
{
	int a,b,c,d;
	if (((Ebudget-Ea)/Ea)<(10-i) && ((Ebudget-Ea)/Eb)<(10-i) && ((Ebudget-Ea)/Ec)<(10-i) && ((Ebudget-Ea)/Ed)<(10-i))
		a = 0;
	if (((Ebudget-Eb)/Ea)<(10-i) && ((Ebudget-Eb)/Eb)<(10-i) && ((Ebudget-Eb)/Ec)<(10-i) && ((Ebudget-Eb)/Ed)<(10-i))
		b = 0;
	if (((Ebudget-Ec)/Ea)<(10-i) && ((Ebudget-Ec)/Eb)<(10-i) && ((Ebudget-Ec)/Ec)<(10-i) && ((Ebudget-Ed)/Ed)<(10-i))
		c = 0;
	if (((Ebudget-Ed)/Ea)<(10-i) && ((Ebudget-Ed)/Ea)<(10-i) && ((Ebudget-Ed)/Ec)<(10-i) && ((Ebudget-Ed)/Ed)<(10-i))
		d = 0;
	return a+b+c+d;

}

int schedule(int i,int La,int Lb,int Lc,int Ld,int Ea,int Eb,int Ec,int Ed,int Ebudget)
{
	int ast,bst,cst,dst;
	int check_result;
	int small = 1000;
	int value;
	ast = 0;
	bst = 0;
	cst = 0;
	dst = 0;
	check_result = check(i,Ebudget,Ea,Eb,Ec,Ed);
	int result[4];
	for (i=0;i<4;i++)
	{
		result[i] = 0;
		if (result[i] < small)
			value = i;
	}

	return value;

}

int las(int Ebudget,int Ea,int Eb,int Ec,int Ed,int La,int Lb,int Lc,int Ld)
{
	int a[11],b[11],c[11],d[11];
	int ft[11];
	char pk[11];
	int aenable[11],benable[11],cenable[11],denable[11];
	float anum,bnum,cnum,dnum;
	int i,j;
	anum = Ebudget/Ea;
	bnum = Ebudget/Eb;
	cnum = Ebudget/Ec;
	dnum = Ebudget/Ed;
	int choice;
	if (anum<10)
		return 0;
	for (i=0;i<11;i++)
	{
		if (anum>0)
			aenable[i] = 1;
		if (bnum>0)
			benable[i] = 1;
		if (cnum>0)
			cenable[i] = 1;
		if (dnum>0)
			denable[i] = 1;
		choice = schedule(i,La,Lb,Lc,Ld,Ea,Eb,Ec,Ed,Ebudget);
		if (choice==0)
		{
			pk[i] = 'acc';
			ft[i] = La;
			for (j=i+1;j<11;j++)
			{
				a[j] = ft[i];
				b[j] = b[i];
				c[j] = c[i];
				d[j] = d[j];
			}
			Ebudget = Ebudget - Ea;
		}
		if (choice==1)
		{
			pk[i] = 'acc';
			ft[i] = Lb;
			for (j=i+1;j<11;j++)
			{
				a[j] = ft[i];
				b[j] = b[i];
				c[j] = c[i];
				d[j] = d[j];
			}
			Ebudget = Ebudget - Eb;
		}
		if (choice==2)
		{
			pk[i] = 'acc';
			ft[i] = Lc;
			for (j=i+1;j<11;j++)
			{
				a[j] = ft[i];
				b[j] = b[i];
				c[j] = c[i];
				d[j] = d[j];
			}
			Ebudget = Ebudget - Ec;
		}
		if (choice==3)
		{
			pk[i] = 'acc';
			ft[i] = Ld;
			for (j=i+1;j<11;j++)
			{
				a[j] = ft[i];
				b[j] = b[i];
				c[j] = c[i];
				d[j] = d[j];
			}
			Ebudget = Ebudget - Ed;
		}

	}

	return 0;

}


int main()
{
	double runtime;
	
	struct timespec start,finish;
	clock_gettime(CLOCK_MONOTONIC, &start);	
	las(1000,100,100,100,100,100,100,100,100);
	clock_gettime(CLOCK_MONOTONIC, &finish);
	runtime = (finish.tv_sec - start.tv_sec);
	runtime += (finish.tv_nsec - start.tv_nsec)/100000000.0;
	printf("\nrun_time：%f\n",runtime);


	return 0;
}
