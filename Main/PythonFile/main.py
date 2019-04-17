import Aperture
import loadImage
import ePSF
#得到数据的绝对路径和名字
data_path = 'E:/GraduationProject/data/M35_20181113_flatted/'
# data_path = 'E:/GraduationProject/newdata/'
data_paths = loadImage.file_path(data_path)
data_names = loadImage.file_name(data_path)
#开始弄所有数据
for i in range(5):
    #Aperture.Aperture(data_paths[i], data_names[i])
    ePSF.ePSF(data_paths[i], data_names[i])
