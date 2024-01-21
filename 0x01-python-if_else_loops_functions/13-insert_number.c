0-Positive-or-negative.py

#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")

1-last_digit.py

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastdigit = number % -10
else:
    lastdigit = number % 10
if lastdigit > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, lastdigit))
elif lastdigit < 6 and lastdigit != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, lastdigit))
else:
    print("Last digit of {:d} is 0 and is 0".format(number))


2-print_alphabet.py

#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    print('{:c}'.format(i), end='')


3-print_alphabet.py

#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    if chr(i) != 'e' and chr(i) != 'q':
        print('{:c}'.format(i), end='')


4-print_hexa.py

#!/usr/bin/python3
for num in range(0, 99):
    print('{} = 0x{:x}'.format(num, num))


5-print_comb2.py

#!/usr/bin/python3
for num in range(0, 99):
    print('{:02d}, '.format(num), end='')
print('99')


6-print_comb3.py

#!/usr/bin/python3
for x in range(0, 10):
    for y in range(x + 1, 10):
        if x == 8 and y == 9:
            print('89')
        else:
            print('{}{}, '.format(x, y), end='')


7-islower.py

#!/usr/bin/python3
def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False


8-uppercase.py

#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
        print("{}".format(i), end="")
    print()


9-print_last_digit.py

#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        last_digit = number % -(10)
        print(-(last_digit), end='')
    else:
        last_digit = number % 10
        print(last_digit, end='')
    return abs(last_digit)


10-add.py

#!/usr/bin/python3
def add(a, b):
    return (a + b)


11-pow.py

#!/usr/bin/python3
def pow(a, b):
    return (a ** b)


12-fizzbuz.py

#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")


13-insert_number.c

#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 * Return: 0 If the function fails or pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}


100-print_tehbapla.py

#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 0:
        diff = 0
    else:
        diff = 32
    print('{}'.format(chr(i - diff)), end='')


101-revove_char_at.py

#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])


102-magic_calculation.py

#!/usr/bin/python3
def magic_calculation(a, b, c):
    if a < b:
        return (c)
    if c > b:
        return (a + b)
    return (a*b - c)
 
