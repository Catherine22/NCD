import lzma as compressor
import sys

fileX = open(sys.argv[1], 'rb')
fileY = open(sys.argv[2], 'rb')
x = fileX.read()
y = fileY.read()
x_y = x + y
fileX.close()
fileY.close()

lenX = len(compressor.compress(x))
lenY = len(compressor.compress(y))
lenXY = len(compressor.compress(x_y))

ncd = (lenXY - min(lenX, lenY)) / max(lenX, lenY)
# print(file1, file2, ncd)

file1 = sys.argv[1].partition("x/")[2][:-4]
file2 = sys.argv[2].partition("y/")[2][:-4]
print('{0},{1},{2}'.format(file1, file2, ncd))