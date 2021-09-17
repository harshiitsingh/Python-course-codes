# Write a program to find out the line number where python is present from ques 6

# content = ""
content = True
i = 1
with open("ques 6 log.txt") as f:
    while content:
        content = f.readline().lower()
        
        if 'python' in content:
            print(content)
            print(f"Yes python is present on line number {i}")
            # print(i)
        i += 1