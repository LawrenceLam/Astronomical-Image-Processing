import loadImage
#找出每一个文件中的数据在总文件里面的位置，以坐标为基准，坐标范围在2个像素差
total_data_path = 'E:/GraduationProject/EPSFFive/lsd/'
relative_path = 'E:/GraduationProject/EPSFFive/txt_data/'
#relative_path = 'E:/GraduationProject/ApertureThird/txt_data/'
relative_absolute_path = loadImage.file_path(relative_path)
relative_name = loadImage.file_name(relative_path)
global_path = 'E:/GraduationProject/EPSFFive/global/'
#global_path = 'E:/GraduationProject/ApertureThird/global'
for i in range(len(relative_absolute_path)):
    total_data = open(total_data_path+relative_name[i], 'r')
    read = total_data.readlines()
    temp_write = open(global_path+relative_name[i], 'w')
    total_data.close()
    temp_read = open(relative_absolute_path[i])
    data = temp_read.readlines()#获得单个文件里面的数据
    result_data = []
    for d in data:
        for temp in read:
            ds = d.split()
            temps = temp.split()
            x_temp = float(ds[1])
            y_temp = float(ds[2])
            x_global = float(temps[1])
            y_global = float(temps[2])
            if abs(x_temp-x_global) <= 2 and abs(y_temp-y_global) <= 2:
                temp_data = temps[5]
                temps[5] = ds[4]
                temps[6] = temp_data
                result_data.append(" ".join(temps))
                temp_write.write(" ".join(temps)+"\n")
                break
    temp_write.close()
