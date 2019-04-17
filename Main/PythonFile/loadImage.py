from astropy.table import Table
import matplotlib.pyplot as plt
from astropy.io import fits as Fits
import os
#获取所有fits文件的绝对路径
def file_path(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            L.append(os.path.join(root, file))
    return L


#获取所有fits文件的名字
def file_name(file_dir):
    N = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            N.append(file)
    return N

relative_name = file_name('E:/GraduationProject/EPSFThird/txt_data/')
print(relative_name)
