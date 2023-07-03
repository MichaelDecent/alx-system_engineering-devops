#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
/**
 * infinite_while - An infinite loop
 *
 * Return: 0
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}

	return (0);
}

/**
 * main - Entry point to the program
 *
 * Return: An infinite loop
 */
int main(void)
{
	pid_t zombie_pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		/*creating a child process*/
		zombie_pid = fork();
		/* suceesfully craeted a child process*/
		if (zombie_pid == 0)
			exit(0)
				/* returning the child's PID*/
		else
			printf("Zombie process created, PID: %d\n", zombie_pid);
	}
	return (infinite_while());
}
