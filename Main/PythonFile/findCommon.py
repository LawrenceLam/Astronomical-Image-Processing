import loadImage
#找到总文件中在多个文件中都出现的共同星星，星等不同，标号标注他们
path = 'E:/GraduationProject/EPSFFive/global/'
common_path = 'E:/GraduationProject/EPSFFive/common/'
file_path = loadImage.file_path(path)
file_name = loadImage.file_name(path)
#用遍历的办法判断一个文件中的数据是否在其他数据中
for i in range(len(file_path)):#遍历每一个文件
    f_read = open(file_path[i])#读取文件内容
    lines = f_read.readlines()#用列表的形式，方便遍历每一行数据
    f_read.close()
    for line in lines:#遍历列表中的数据
        flag = True#一开始标志为TRUE，当在任意一个文件匹配不到时，标志为FALSE
        for j in range(len(file_path)):#遍历其他文件
            if i == j:#同一个文件则跳过
                continue
            else:#不同文件则开始读取该文件
                l = line.split()#将line中的一行数据切断，只要第一个
                f_check = open(file_path[j])
                st = f_check.read()#读取为字符串的形式
                f_check.close()
                if st.find(l[0])==-1:
                    flag = False#找不到该数据，flag为FALSE
                    break
        #遍历完所有其他的文件，若flag仍旧为TRUE，则说明数据在所有文件中都有
        if flag:
            f_write = open(common_path+file_name[i], 'a+')
            f_write.write(line)
            f_write.close()
