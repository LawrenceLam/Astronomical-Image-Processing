import loadImage
import math
#找到参考星后，计算每一幅图中星星与参考星均值的差，并按id将星星分文件存储
reference = 'E:/GraduationProject/EPSFFive/reference.txt'
path = 'E:/GraduationProject/EPSFFive/global/'
result_path = 'E:/GraduationProject/EPSFFive/calRefer/'
f_read_reference = open(reference, 'r')
refs = f_read_reference.readlines()
ref_ids = []
for ref in refs:
    rs = ref.split()
    ref_ids.append(rs[0])
file_path = loadImage.file_path(path)
file_name = loadImage.file_name(path)
#用遍历的办法判断一个文件中的数据是否在其他数据中
for i in range(len(file_path)):#遍历每一个文件
    f_read = open(file_path[i])#读取文件内容
    lines = f_read.readlines()#用列表的形式，方便遍历每一行数据
    f_read.close()
    sum_reference = 0
    #先计算出参考星的均值
    for line in lines:#遍历列表中的数据
        datas = line.split(' ')
        if datas[0] in ref_ids:
            sum_reference += float(datas[4])
    mean_reference = sum_reference/3
    print(sum_reference)
    print(mean_reference)
    for line in lines:
        datas = line.split(' ')
        if datas[0] in ref_ids:
            continue
        num = float(datas[4])
        num = num - mean_reference
        datas[6] = str(num)
        f_write = open(result_path+datas[0]+'.txt', 'a+')
        f_write.write(" ".join(datas))
        f_write.write("\n")
        f_write.close()
