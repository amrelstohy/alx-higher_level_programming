#include "hash_tables.h"
/**
 * hash_table_create - function
 *@size: size
 *Return: pointer to the newly created hash table
 */
hash_table_t *hash_table_create(unsigned long int size)
{
	hash_table_t *table = calloc(size, sizeof(hash_table_t));

	if (table == NULL)
		return (NULL);
	return (table);
}
