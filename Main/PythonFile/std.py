import loadImage
import math
path = 'E:/GraduationProject/EPSFFour/classify/'
#path = 'E:/GraduationProject/ApertureThird/classify/'
std_path = 'E:/GraduationProject/EPSFFour/std/'
#std_path = 'E:/GraduationProject/ApertureThird/std/'
ref_ids = [3426270784124418304, 3426270410463254400, 3426294114386810880]
print(type(ref_ids[0]))
ref_mags = [12.7746, 12.2546, 11.6186]
mean_sum = 0
for mag in ref_mags:
    mean_sum+=mag
mean = mean_sum/len(ref_mags)
print(mean)
file_path = loadImage.file_path(path)
file_name = loadImage.file_name(path)
for i in range(len(file_path)):
    print(file_name[i][:-4])
    if int(file_name[i][:-4]) in ref_ids:
        print('alert')
        continue
    f_read = open(file_path[i], 'r')
    data = f_read.readlines()
    sum = 0
    data_float = []
    for d in data:
        #print(d)
        if d =='\n':continue
        ds = d.split(' ')
        num = float(ds[5]) - mean
        data_float.append(num)
        sum += num
    print(sum)
    mean_result = sum/len(data)
    sum_result = 0
    for n in data_float:
        sum_result += math.pow(n-mean_result, 2)
    std = math.sqrt(sum_result/len(data_float))
    f_write = open(std_path+ds[0]+'.txt', 'w')
    f_write.write(str(ds[6]) + ' ' + str(std))
    print(str(mean_result)+' '+str(std))
