import numpy as np
import pandas as pd
from scipy.ndimage.measurements import label

graph = pd.read_csv('input_question_4', sep='\t', header=None).to_numpy()

# graph = [
#     [0, 0, 1, 1],
#     [1, 1, 0, 0],
#     [0, 0, 0, 0],
#     [0, 1, 1, 0],
#     [0, 1, 1, 1]
# ]
# array = np.array(graph)
overlay = [ # 4-connectivity
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]
]
labeled, ncomponents = label(graph, overlay)
print(labeled)
output = pd.DataFrame(labeled)
output.to_csv('output_question_4', sep=' ', header=False, index=False)