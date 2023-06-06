#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - a function
 * @list: the link
 *
 * Return: Always 0.
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise;
	listint_t *hare1;
	listint_t *hare2;

	tortoise = list;
	hare1 = tortoise;

	while (tortoise && (hare2 = hare1->next) && (hare1 = hare2->next))
	{
		if (hare1 == tortoise || hare2 == tortoise)
		{
			return (1);
		}
		tortoise = tortoise->next;
	}

	return (0);
}
