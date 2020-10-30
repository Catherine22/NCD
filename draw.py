import numpy as np
import matplotlib.pyplot as plt

csv_file = np.genfromtxt("ncd_data.csv",
                         delimiter=",",
                         dtype=None,
                         skip_header=1
                         #names=('binary', 'class', 'ncd')
                        )

csv_file_to_list = csv_file.tolist()

# print(len(csv_file_to_list))

x_len = 28
y_len = 28
result = np.zeros((y_len, x_len))

for y_index in range(x_len):
    for x_index in range(y_len):
        # print((y_len * y_index) + x_index)
        result[x_index, y_index] = csv_file_to_list[(y_len * y_index) + x_index][2]

# print(result)
plt.figure('Malware Similarity Matrix')
plt.xlabel('X')
plt.xticks(np.arange(0, x_len, step=2))
plt.ylabel('Y')
plt.yticks(np.arange(0, y_len, step=2))
plt.imshow(result, interpolation='nearest', vmin=0, cmap='RdBu')
plt.colorbar()
plt.tight_layout()
plt.show()