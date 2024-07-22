#4. Write program to check if element exists in list

def element_exists(lst, element):
    return element in lst

example_list = [12, 35, 9, 56, 24]
element_to_check = 350

if element_exists(example_list, element_to_check):
    print(f"{element_to_check} exists in the list.")
else:
    print(f"{element_to_check} does not exist in the list.")
