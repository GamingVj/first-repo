// Write a C Program that implements the FIFO page_replacement algorithm.

#include <stdio.h>

int main()
{
    int reference_string[10],page_faults=0,m,s,n,pages=0,frames;

    printf("Enter Total Number of Pages:\t");
    scanf("%d",&frames); 

    printf("Enter values of Reference String:\n");
    for(m = 0; m<pages; m++)
    {
        printf("Value No. [%d]:\t",m+1);
        scanf("%d",&frames);
    }

    printf("\n Enter Total number of frames:\t");
    scanf("%d",&frames);

    int temp[frames];
    for(m=0;m<frames;m++)
    {
        temp[m]=-1;
    }

    for(m=0;m<pages;m++)
    {
        s=0;
        for(n=0;n<frames;n++)
        {
            if(reference_string[m]==temp[n])
            {
                s++;
                page_faults--;
            }
        }
        page_faults++;
        
        if((page_faults<=frames)&&(s==0))
        {
            temp[page_faults-1]=reference_string[m];
        }
        else if(s==0)
        {
            temp[(page_faults-1)%frames]=reference_string[m];
        }
        printf("\n");
        for(n=0;n<frames;n++)
        {
            printf("%d\t",temp[n]);
        }
    }
    printf("\n Total Page Faults:\t%d\n",page_faults);
    return 0;
}