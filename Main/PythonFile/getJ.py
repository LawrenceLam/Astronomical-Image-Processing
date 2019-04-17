import loadImage
# mag_path = 'E:/GraduationProject/EPSFSecond/ePSF_mag_data/'
# mean_path = 'E:/GraduationProject/EPSFSecond/mean_data'
mag_path = 'E:/GraduationProject/ApertureSecond/Aperture_mag_data'
mean_path = 'E:/GraduationProject/ApertureSecond/mean_data'
mag_path_datas = loadImage.file_path(mag_path)
mag_path_names = loadImage.file_name(mag_path)
for mag_path_data in mag_path_datas:
    f_read = open(mag_path_data)
    data_lists = []
    data_str = f_read.readline()
    while data_str:
        data_strs = data_str.split(' ')
        data_nums = []
        data_nums.append(int(data_strs[0]))
        data_nums.append(float(data_strs[1]))
        data_lists.append(data_nums)
        data_str = f_read.readline()
    f_read.close()
    print(data_lists)
    for i in range(0,len(data_lists)-1):
        sum = 0
        for j in range(0, len(data_lists)-1):
            if(j==i):
                continue
            sum += data_lists[j][1]
        mean = sum/(len(data_lists)-1)
        final_data = data_lists[i][1] - mean
        absolute_path = mean_path + '/' + str(i+1) + '.txt'
        print(str(i+1)+':'+str(final_data))
        f_write = open(absolute_path, 'a+')
        f_write.write(str(i+1) + ' ' + str(final_data)+"\n")
        f_write.close()
