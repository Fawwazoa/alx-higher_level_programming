#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - find loop in linked list
 * @list: first element of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *sl = list;
	listint_t *fa = list;

	if (list == NULL)
		return (0);
	while (sl && fa && fa->next)
	{
		sl = sl->next;
		fa = fa->next->next;
		if (sl == fa)
		{
			while (1)
			{
				sl = fa;
				while (fa->next != slow && fa->next != list)
					fa = fa->next;
				if (fa->next == list)
					break;
				list = list->next;
			}
			return (1);
		}

	}
	return (0);

}
