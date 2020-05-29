from sympy.utilities.iterables import multiset_permutations
import pandas as pd

def calc_penalty(lst):
    total_pen = 0
    for i, x in enumerate(lst):
        if i == 0: # top left
            down = lst[i+L]
            right = lst[i+1]
            if down == x:
                total_pen += 1
            if right == x:
                total_pen += 1
        elif i == (L-1): # top right
            down = lst[i+L]
            left = lst[i-1]
            if down == x:
                total_pen += 1
            if left == x:
                total_pen += 1
        elif i == (L*L - L): # bottom left
            up = lst[i-L]
            right = lst[i+1]
            if up == x:
                total_pen += 1
            if right == x:
                total_pen += 1
        elif i == (L*L - 1): # bottom right
            left = lst[i-1]
            up = lst[i-L]
            if up == x:
                total_pen += 1
            if left == x:
                total_pen += 1
        elif i < L: # top
            down = lst[i+L]
            left = lst[i-1]
            right = lst[i+1]
            if down == x:
                total_pen += 1
            if left == x:
                total_pen += 1
            if right == x:
                total_pen += 1
        elif i%L == 0: # left
            down = lst[i+L]
            up = lst[i-L]
            right = lst[i+1]
            if down == x:
                total_pen += 1
            if up == x:
                total_pen += 1
            if right == x:
                total_pen += 1
            
        elif i%L == (L-1): # right
            down = lst[i+L]
            up = lst[i-L]
            left = lst[i-1]
            if down == x:
                total_pen += 1
            if up == x:
                total_pen += 1
            if left == x:
                total_pen += 1
        elif i > (L*L-L): # bottom
            right = lst[i+1]
            up = lst[i-L]
            left = lst[i-1]
            if right == x:
                total_pen += 1
            if up == x:
                total_pen += 1
            if left == x:
                total_pen += 1
        else: # middle
            right = lst[i+1]
            up = lst[i-L]
            left = lst[i-1]
            down = lst[i+L]            
            if right == x:
                total_pen += 1
            if up == x:
                total_pen += 1
            if left == x:
                total_pen += 1
            if down == x:
                total_pen += 1
    return total_pen

colors = ['R']*13 + ['B']*12
L = 5

combi_list = multiset_permutations(colors, L*L)
best_combi, best_penalty = None, L*L*4
for combi in combi_list:
    pen = calc_penalty(combi)
    if pen < best_penalty:
        best_combi = combi
        best_penalty = pen
        print("Best: {}, pen: {}".format(best_combi, best_penalty))
        if best_penalty == 0:
            break

square_grid = pd.DataFrame('-', index=list(range(L)), columns=list(range(L)))
for i in range(len(best_combi)):
    color = best_combi[i]
    col = i%L
    row = int(i/L)
    square_grid.at[row, col] = color
print(square_grid)
square_grid.to_csv('output_question_5_1', sep=' ', header=False, index=False)