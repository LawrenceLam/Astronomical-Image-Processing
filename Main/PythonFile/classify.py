import loadImage

#分类后的文件存储路径
classify_path = 'E:/GraduationProject/EPSFFive/classify/'
#已经得到的共有星星文件目录
common_path = 'E:/GraduationProject/EPSFFive/common/'
file_path = loadImage.file_path(common_path)
file_name = loadImage.file_name(common_path)
#读取所有公共星星
for path in file_path:
    #打开一个未处理的星星文件
    f_read = open(path, 'r')
    #读取一行后将结果写到分类的文件中
    line = f_read.readline()
    while line:
        #得到星星在总文件中的标号，作为文件名
        str = (line.split())[0]
        f_write = open(classify_path+str+'.txt', 'a+')
        f_write.write(line)
        f_write.close()
        line = f_read.readline()
    f_read.close()
