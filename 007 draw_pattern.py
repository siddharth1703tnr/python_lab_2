# 2. Draw pattern :
# 12345
# 1234
# 123
# 12
# 1

def draw_pattern(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

# Example usage:
draw_pattern(5)
