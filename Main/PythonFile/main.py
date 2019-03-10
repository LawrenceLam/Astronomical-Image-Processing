import Aperture
import loadImage
#得到数据的绝对路径和名字
data_path = 'E:/GraduationProject/data/M35_20181113_flatted'
data_paths = loadImage.file_path(data_path)
data_names = loadImage.file_name(data_path)
#开始弄所有数据
for i in range(len(data_paths)):
    Aperture.Aperture(data_paths[0], data_names[0])
