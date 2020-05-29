# 7.2 Part (b), Part(1)
L_list = [4, 8, 5, 9, 6, 7]

with open('input_coordinates_7_2.txt') as f:
    coordinates = f.read()

coordinates = coordinates.strip().split("\n")
coordinates.pop(0)
results = ['index']
for coord in coordinates:
    x_list = coord.split("\t")
    for i in range(len(x_list)):
        x_list[i] = int(x_list[i])

    index = 0
    for i in range(len(x_list)):
        factorial = 1
        for j in range(i):
            factorial *= L_list[j]
        index += x_list[i]*factorial
    results.append(str(index))

output = '\n'.join(results)
with open('output_index_7_2.txt', 'w') as f:
    f.write(output + "\n")

# 7.1 Part (b), Part(2)
L_list = [4, 8, 5, 9, 6, 7]

with open('input_index_7_2.txt') as f:
    indices = f.read()
    
def multiplier(start, end):
    mul = 1
    for x in L_list[start:end+1]:
        mul *= x
    return mul

indices = indices.strip().split("\n")
indices.pop(0)
results = ['x1\tx2\tx3\tx4\tx5\tx6']
for index in indices:
    index = int(index)
    x_list = [str(index%L_list[0])]
    for i in range(1, len(L_list)):
        x = int((index % multiplier(0, i))/multiplier(0, i-1))
        x_list.append(str(x))
    x_list = '\t'.join(x_list)
    results.append(x_list)        

output = '\n'.join(results)
with open('output_coordinates_7_2.txt', 'w') as f:
    f.write(output + "\n")