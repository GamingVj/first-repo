// Implement FCFS Scheduling algorithm in C.

#include <stdio.h>

int main ()
{
    int n, bt[20], wt[20], tat[20];
    int i, j;
    float avwt = 0, avtat = 0;
    printf("Enter Total Number of Processes (maximum 20): ");
    scanf("%d", &n);
    printf("\nEnter process Burst Time\n");
    
    for(i = 0; i < n; i++)
    {
        printf("P[%d]: ", i + 1);
        scanf("%d", &bt[i]);
    }

    wt[0] = 0;
    
    for(i = 1; i < n; i++)
    {
        wt[i] = 0;
        for(j = 0; j < i; j++)
        {
            wt[i] += bt[j];
        }
    }

    printf("\nProcess\t\tBurst Time\tWaiting Time\tTurn around Time");
    for(i = 0; i < n; i++)
    {
        tat[i] = bt[i] + wt[i];
        avwt += wt[i];
        avtat += tat[i];
        printf("\nP[%d]\t\t%d\t\t%d\t\t%d", i + 1, bt[i], wt[i], tat[i]);
    }

    avwt /= n;
    avtat /= n;
    printf("\n\nAverage Waiting Time: %.2f", avwt);
    printf("\nAverage Turn around Time: %.2f", avtat);
    return 0;
}