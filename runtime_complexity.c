#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
//#include <windows.h>

//this program is wrong, it is just for calculate the time complexity.

int check(int i,Ebudget,Ea,Eb,Ec,Ed)
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

int schedule(int i,La,Lb,Lc,Ld,Ea,Eb,Ec,Ed,Ebudget)
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

int las(int Ebudget,Ea,Eb,Ec,Ed,La,Lb,Lc,Ld)
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
	
	LARGE_INTEGER time_start;	//开始时间
	LARGE_INTEGER time_over;	//结束时间
	double dqFreq;		//计时器频率
	LARGE_INTEGER f;	//计时器频率
	QueryPerformanceFrequency(&f);
	dqFreq=(double)f.QuadPart;
	QueryPerformanceCounter(&time_start);	//计时开始
	las(1000,100,100,100,100,100,100,100,100);
	QueryPerformanceCounter(&time_over);	//计时结束
	runtime=1000000*(time_over.QuadPart-time_start.QuadPart)/dqFreq;
	//printf("\nrun_time：%fus\n",run_time);


	return 0;
}