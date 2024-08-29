#include <stdio.h>
#include <lpthread.h>

void* task(void* arg)
{
	long id = (long)arg;
	printf("Thread %Id is running\n",id);
	printf("Thread %Id finished its task\n",id);
	return NULL;
}

int main()
{
	int numberOfThreads=5;
	pthread_t threads[numberOfThreads];
	for(long i = 0;i<numberOfThreads;i++)
	{
		if(pthread_create(&threads[i],NULL,task,(void*)i)!=0)
		{
			perror("Failed to create thread");
			return 1;
		}
	}

	for(int i = 0;i<numberOfThreads;i++)
	{
		if(pthread_join(threads[i],NULL)!=0)
		{
			perror("Failed to join thread");
			return 1;
		}
	}

	printf("All threads have finished.\n")
	return 0;
}