#7. create a file and perform to read() and write() function.  

with open('example.txt', 'w') as file:
    file.write("Hello, this is a test file.\n")
    file.write("This is the second line.")

with open('example.txt', 'r') as file:
    content = file.read()

print("File Content:")
print(content)
