#Write program to interchange first and last elements in a list 
# Input : [12, 35, 9, 56, 24] 
# Output : [24, 35, 9, 56, 12]

def interchange_first_last(lst):
    if len(lst) < 2:
        return lst
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst


input_list = [12, 35, 9, 56, 24]
print(input_list)
output_list = interchange_first_last(input_list)
print(output_list)
