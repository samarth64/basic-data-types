
def list_operations():
    
    my_list = [10, 20, 30, 40]
    print("Original List:", my_list)
    
    my_list.append(50)
    print("List after adding an element:", my_list)
    
    my_list.remove(20)
    print("List after removing an element:", my_list)
    
    my_list[1] = 25
    print("List after modifying an element:", my_list)
    
    return my_list

def dict_operations():
    
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    print("\nOriginal Dictionary:", my_dict)
    
    my_dict['d'] = 4
    print("Dictionary after adding a key-value pair:", my_dict)
    
    del my_dict['b']
    print("Dictionary after removing a key-value pair:", my_dict)
    
    my_dict['c'] = 5
    print("Dictionary after modifying a value:", my_dict)
    
    return my_dict

def set_operations():
    
    my_set = {10, 20, 30}
    print("\nOriginal Set:", my_set)
    
    my_set.add(40)
    print("Set after adding an element:", my_set)
    
    my_set.remove(20)
    print("Set after removing an element:", my_set)
    
    return my_set

def main():
    list_result = list_operations()
    dict_result = dict_operations()
    set_result = set_operations()

    print("\nFinal List:", list_result)
    print("Final Dictionary:", dict_result)
    print("Final Set:", set_result)

if __name__ == "__main__":
    main()
