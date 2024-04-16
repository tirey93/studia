# part 1
# We open file "input.txt". Second argument used to identify that we want to read file
# Note: if you want to write to the file use "w" as second argument
# f = open("input.txt", "r")

# for line in f.readlines():   # read lines
#     print(line)              # print each line
# f.close()                    # It's important to close the file to free up any system resources.


# Powtórzyć rozwiązanie z wykorzystaniem składni withopen("input.txt", "r") as file:
#     for line in file.readlines():
#         print(line)

# part 2
# f1 = open("input1.txt", "r")
#print only first line of f1
#pass

#print only first line of f1 again
#pass
#pass

#print only third line of f1 again
#pass
#pass

# f1.close()                  #do not forget to close file
# print()

# Powtórzyć rozwiązanie z wykorzystaniem składni with
with open("input1.txt", "r") as file:
    print(file.readline(),end='')
    file.seek(0)
    print(file.readline(),end='')
    file.readline()
    print(file.readline(),end='')
