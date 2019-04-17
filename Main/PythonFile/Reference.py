import loadImage
#找到所有文件值得用来当做参考的星星，这种星星的特征是大概30个像素的范围内没有其他星星且星等在10-20
#先从已经选好的星星中挑选像素合适的点
path = 'E:/GraduationProject/EPSFFive/common/'
reference = 'E:/GraduationProject/EPSFFive/reference.txt'
#path = 'E:/GraduationProject/ApertureThird/common/M35_2-I_001-2.fits.txt'
#reference = 'E:/GraduationProject/ApertureThird/reference.txt'
file_path = loadImage.file_path(path)
path = file_path[0]
f_write = open(reference, 'w')
fit_star = []
f_read = open(path)
addi_stars = f_read.readlines()
for i in range(len(addi_stars)):
    flag = True
    i_list = addi_stars[i].split()
    for j in range(len(addi_stars)):
        if i == j:
            continue
        j_list = addi_stars[j].split()
        if abs(float(i_list[1])-float(j_list[1])) <= 4 or abs(float(i_list[2])-float(j_list[2])) <= 4:
            flag = False
            break
    if flag:
        fit_star.append(addi_stars[i])
        f_write.write("".join(addi_stars[i]))
