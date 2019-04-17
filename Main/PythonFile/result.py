import loadImage
import matplotlib.pyplot as plt
data_path = 'E:/GraduationProject/EPSFFive/std'
# data_path = 'E:/GraduationProject/EPSFExtrat=15fwhm=7/std'
file_path = loadImage.file_path(data_path)
file_name = loadImage.file_name(data_path)
x = []
y = []
for i in range(len(file_path)):
    f_read = open(file_path[i])
    datas = f_read.readline().split()
    x_data = float(datas[0])
    y_data = float(datas[1])
    if y_data>0.1:
        continue
    x.append(x_data)
    y.append(y_data)
plt.plot(x, y, 'ro')
plt.show()
