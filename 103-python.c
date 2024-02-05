#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - prints information about Python lists
 * @p: pointer to a Python object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid List Object\n");
		fflush(stdout);
		return;
	}

	size = PyList_Size(p);
	printf("[*] Python list info\n[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
		else if (PyFloat_Check(item))
			print_python_float(item);
	}
}

/**
 * print_python_bytes - prints information about Python bytes
 * @p: pointer to a Python object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		fflush(stdout);
		return;
	}

	size = PyBytes_Size(p);
	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);

	str = PyBytes_AsString(p);
	printf("  trying string: %s\n", str ? str : "(error)");

	printf("  first %ld bytes: ", size < 10 ? size + 1 : 10);
	for (i = 0; i <= size && i < 10; i++)
		printf("%02x%c", (unsigned char)str[i], i == size || i == 9 ? '\n' : ' ');
}

/**
 * print_python_float - prints information about Python floats
 * @p: pointer to a Python object
 */
void print_python_float(PyObject *p)
{
	printf("[.] float object info\n");
	printf("  value: %f\n", ((PyFloatObject *)p)->ob_fval);
}

