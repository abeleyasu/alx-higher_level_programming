#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            division = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            division = 0
        except (TypeError, ValueError):
            print("wrong type")
            division = 0
        except IndexError:
            print("out of range")
            division = 0
        finally:
            result.append(division)
    return result

# Test cases
if __name__ == "__main__":
    my_l_1 = [10, 8, 4]
    my_l_2 = [2, 4, 4]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)

    print("--")

    my_l_1 = [10, 8, 4, 4]
    my_l_2 = [2, 0, "H", 2, 7]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)
