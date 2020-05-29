# Depth first search (O(num_edges + num_vertices))
m = 9
n = 9
sum_targets = [65, 72, 90, 110]
def get_neighbours(path, current_sum):
    # path = 'RDRD'
    # current_sum = 5
    neighbours = []
    count_r = path.count('R') # 2
    count_d = path.count('D') # 2
    
    if count_r < n - 1: # max right range
        neighbours.append((path + 'R', current_sum + count_d + 1)) # right
    if count_d < m - 1: # max down range
        neighbours.append((path + 'D', current_sum + count_d + 2)) # down
    # neighbours = [('RDRDR', 8), ('RDRDD', 9)]
    return neighbours

def find_right_sum(sum_target):
    solutions = []
    to_explore = [('',1)]
    visited = set()
    while len(to_explore) > 0:
        current = to_explore.pop() # ('',1), to_explore = []
        if current[1] == sum_target and len(current[0]) == (m+n-2):
            solutions.append((sum_target, current[0]))
        if current not in visited:
            visited.add(current)
        neighbours = get_neighbours(current[0], current[1]) # [('R',1), ('DR',4), ('DD',5), ('DDR',7) ]
        for neighbour in neighbours:
            if neighbour not in visited:
                to_explore.append(neighbour)
                visited.add(neighbour)
    return solutions
                
with open('output_question_1', 'w') as fo:
    for sum_target in sum_targets:
        solutions = find_right_sum(sum_target)
        for sum_target, operations in solutions:
            fo.write('{} {}\n'.format(sum_target, operations))