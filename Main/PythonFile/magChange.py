import math
import loadImage
import numpy as np

# path = 'E:/GraduationProject/EPSFSecond/txt_data'
# mag_path = "E:/GraduationProject/EPSFSecond/ePSF_mag_data"
path = 'E:/GraduationProject/ApertureSecond/txt_data'
mag_path = "E:/GraduationProject/ApertureSecond/Aperture_mag_data"
data_paths = loadImage.file_path(path)
data_names = loadImage.file_name(path)
#开始弄所有数据
for i in range(len(data_paths)):
    f = open(data_paths[i], 'r')
    f_write = open(mag_path+"/"+data_names[i], 'w')
    print(mag_path+"/"+data_names[i])
    result = f.readline()
    while result:
        list = result.split(' ')
        print(list)
        id = list[0]
        num = float(list[3])
        print(num)
        mag = 25 - 2.5*math.log(num, 10)
        print(id+":"+str(mag))
        strs = id+" "+ str(mag)+"\n"
        f_write.writelines(strs)
        result = f.readline()
    f.close()
    f_write.close()
