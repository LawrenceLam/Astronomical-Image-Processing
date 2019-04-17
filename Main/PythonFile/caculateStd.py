import loadImage
import math
reference = 'E:/GraduationProject/EPSFFive/calRefer/'
std_path = 'E:/GraduationProject/EPSFFive/std/'
file_path = loadImage.file_path(reference)
file_name = loadImage.file_name(reference)
for i in range(len(file_path)):
    f_read = open(file_path[i], 'r')
    data = f_read.readlines()
    if len(data) < 6:
        continue
    sum = 0
    data_float = []
    sum_mean = 0
    for d in data:
        ds = d.split()
        num = float(ds[6])
        data_float.append(num)
        sum += num
        sum_mean += float(ds[4])
    mean_result = sum/len(data)
    mean_mean = sum_mean/len(data)
    sum_result = 0
    for n in data_float:
        sum_result += math.pow(n-mean_result, 2)
    std = math.sqrt(sum_result/len(data_float))
    f_write = open(std_path+ds[0]+'.txt', 'w')
    f_write.write(str(mean_mean) + ' ' + str(std))
