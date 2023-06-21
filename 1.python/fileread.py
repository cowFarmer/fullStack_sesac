with open("names.txt", "r") as file: # r = read, w = write, a = append
    lines = file.readlines()

names = []

for line in lines:
    names.append(line.strip())
    
print(names)