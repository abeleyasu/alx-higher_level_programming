Hash Tables
This repository contains a simple implementation of hash tables in C. The code provides functions for creating a hash table, adding elements, retrieving values, printing the hash table, and deleting the hash table.

Table of Contents
Files
Compilation
Usage
Examples
Contributing
License
Files
0-hash_table_create.c: Function to create a hash table.
1-djb2.c: Implementation of the djb2 hash algorithm.
2-key_index.c: Function to get the index of a key in the hash table array.
3-hash_table_set.c: Function to add an element to the hash table.
4-hash_table_get.c: Function to retrieve a value associated with a key.
5-hash_table_print.c: Function to print the hash table.
6-hash_table_delete.c: Function to delete a hash table.
hash_tables.h: Header file containing struct definitions and function prototypes.
Compilation
Compile the code using the provided compilation commands for each test program. Make sure to include all necessary files, and use the appropriate compiler flags.

bash
Copy code
gcc -Wall -pedantic -Werror -Wextra -std=gnu89 <test_program.c> <implementation_files.c> -o <output_executable>
Usage
To use the hash table functions in your project, include the hash_tables.h header file and link against the compiled object files.

c
Copy code
#include "hash_tables.h"
Examples
c
Copy code
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "hash_tables.h"

int main(void)
{
    hash_table_t *ht;

    ht = hash_table_create(1024);
    hash_table_set(ht, "c", "fun");
    hash_table_set(ht, "python", "awesome");
    hash_table_set(ht, "Bob", "and Kris love asm");
    hash_table_set(ht, "N", "queens");
    hash_table_set(ht, "Asterix", "Obelix");
    hash_table_set(ht, "Betty", "Cool");
    hash_table_set(ht, "98", "Battery Street");
    hash_table_print(ht);
    hash_table_delete(ht);

    return (EXIT_SUCCESS);
}
Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Contributions are welcome!

License
This project is licensed under the MIT License - see the LICENSE file for details.
