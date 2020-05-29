# 7.1 Part (b), Part(1)
L1 = 50
L2 = 57
with open('input_coordinates_7_1.txt') as f:
    coordinates = f.read()

coordinates = coordinates.strip().split("\n")
coordinates.pop(0)
results = ['index']
for coord in coordinates:
    x1 = int(coord.split("\t")[0])
    x2 = int(coord.split("\t")[1])
    index = x2*L1 + x1
    results.append(str(index))

output = '\n'.join(results)
with open('output_index_7_1.txt', 'w') as f:
    f.write(output + "\n")

# 7.1 Part (b), Part(2)
L1 = 50
L2 = 57
with open('input_index_7_1.txt') as f:
    indices = f.read()

indices = indices.strip().split("\n")
indices.pop(0)
results = ['x1\tx2']
for index in indices:
    index = int(index)
    x1 = index % L1
    x2 = int(index/L1)
    coord = str(x1) + '\t' + str(x2)
    results.append(coord)

output = '\n'.join(results)
with open('output_coordinates_7_1.txt', 'w') as f:
    f.write(output + "\n")