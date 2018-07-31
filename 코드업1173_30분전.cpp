// 10시 20분의 30분 전은 몇 시 몇 분일까요? 
// 예시) 12 35 -> 12 5 
//       12 10 -> 11 40
//       0 20 -> 23 50 
# include<stdio.h> 
main()
{
	int hour, minute;
	scanf("%d %d", &hour, &minute);
	minute = minute - 30;
	if(minute < 0)
	{
		hour = hour -1;
		minute = 60 + minute;
	}
	if(hour < 0)
		hour = 24 + hour;
	printf("%d %d", hour, minute);
}
