import sympy # sympy is used to solve linear equations
import pandas as pd

points_to_check = pd.read_csv('input_question_6_points', sep=' ', header=None)
polygon_points = pd.read_csv('input_question_6_polygon', sep=' ', header=None).to_numpy().tolist()
points_to_check_list = points_to_check.to_numpy().tolist()
results = []

x,y = sympy.symbols('x,y')

# points_to_check = [(3,3), (7,5), (5,6), (0,3), (0,5)]
# polygon_points = [(1,1), (1,5), (10,5), (10,1)]
polygon_lines = []
y_ranges = []
x_ranges = []
for i in range(len(polygon_points)):    
    if i == len(polygon_points) - 1: # last point:
        x1 = polygon_points[i]
        x2 = polygon_points[0]
    else:
        x1 = polygon_points[i]
        x2 = polygon_points[i+1]
        
    if x2[0] == x1[0]: # if x coordinates are the same
        polygon_lines.append(sympy.Eq(x,x1[0]))
        y_ranges.append((x1[1], x2[1]))
        x_ranges.append((x1[0], x2[0]))
    elif x2[1] == x1[1]: # if y coordinates are the same
        polygon_lines.append(sympy.Eq(y,x1[1]))
        y_ranges.append((x1[1], x2[1]))
        x_ranges.append((x1[0], x2[0]))
    else:
        gradient = (x2[1] - x1[1])/(x2[0] - x1[0])
        y_intercept = x1[1] - gradient*x1[0]
        polygon_lines.append(sympy.Eq(y, gradient*x + y_intercept))
        y_ranges.append((x1[1], x2[1]))
        x_ranges.append((x1[0], x2[0]))

# points_to_check_list = [(10,14)]
for point in points_to_check_list:
    num_intersections = []
    point_line = sympy.Eq(y, point[1])
    # print("Point line: {}".format(point_line))
    for i in range(len(polygon_lines)):
        line = polygon_lines[i]
        y_range = y_ranges[i]
        x_range = x_ranges[i]
        result = sympy.solve([point_line, line], (x,y))
#         print("Line to compare: {}".format(line))
#         print("Result: {}\n".format(result))
#         print(x_range)
#         print(y_range)
        if x in result:
            if result[x] >=  point[0] and (result[y] <= max(y_range) and result[y] >= min(y_range)):
                if result not in num_intersections:
                    num_intersections.append(result)
#                 print("intersect")
#                 print(point_line)
#                 print(line)
#                 print("Result: {}\n".format(result))
        elif y in result:
            if point[0] <= max(x_range) and point[0] >= min(x_range):
                if result not in num_intersections:
                    num_intersections.append(result)
#                 print("intersect")
#                 print(point_line)
#                 print(line)
#                 print("Result: {}\n".format(result))
    if len(num_intersections)%2 == 1: # odd number of intersections
        print("Point {} lies {} the polygon ({} intersections)".format(point, 'inside', num_intersections))
        results.append('inside')
    else:
        print("Point {} lies {} the polygon ({} intersections)".format(point, 'outside', num_intersections))
        results.append('outside')

points_to_check['results'] = results
print(points_to_check)
points_to_check.to_csv('output_question_6', sep=' ', index=False, header=False)