#3. Write program to find length of list

def list_length(lst):
    count = 0
    for _ in lst:
        count += 1
    return count

example_list = [12, 35, 9, 56, 24]
length = list_length(example_list)
print("Length of the list:", length)
