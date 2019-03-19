from astropy.stats import sigma_clipped_stats
from astropy.io import fits as Fits
import numpy as np
from photutils import DAOStarFinder
import matplotlib.pyplot as plt
from astropy.visualization import SqrtStretch
from astropy.visualization.mpl_normalize import ImageNormalize
from photutils import CircularAperture
import os
#确定星星的中心
#加载单张图片
png_absolute = 'E:/GraduationProject/png_data'
txt_absolute = 'E:/GraduationProject/txt_data'


def Aperture(file_path, file_name):
    image_hdu = Fits.open(file_path)
    image_hdu.info()
    #print(len(image_hdu[1].data))
    #提取图片中的数据
    image_data = image_hdu[0].data[0]
    # image_data = image_hdu
    print(image_data)
    #开始计算图片中所有数据的中心
    #估计背景和背景噪声
    mean, median, std = sigma_clipped_stats(image_data, sigma=3.0)
    #输出平均，中位数，标准
    print((mean, median, std))

    #减去背景，使用DAOStarfinder查找图像中的恒星，恒星的fwhms大约为3像素，
    # 峰值大约比背景高5西格玛。生成一个包含星体探测器结果的天体表：
    daofind = DAOStarFinder(fwhm=3.0, threshold=5.*std)
    sources = daofind(image_data-median)
    #输出找到的所有星体信息
    print(sources)
    print(type(sources))
    #存储数据的文件的路径
    txt_path = txt_absolute+'/'+file_name+'.txt'
    #将数据输入到文件里面
    f_write = open(txt_path, 'w')
    for source in sources:
        string = ""
        id = np.int(source['id'])
        xcentroid = np.float(source['xcentroid'])
        ycentroid = np.float(source['ycentroid'])
        mag = np.float(source['mag'])
        string = string + str(id) + ' ' + str(xcentroid) + ' ' + str(ycentroid) + ' ' + str(mag) + ' ' + str(median) + ' 0\n'
        f_write.write(string)
    #在图中标记出星星的位置
    #找出星星在图片中的坐标
    positions = (sources['xcentroid'], sources['ycentroid'])#位置
    apertures = CircularAperture(positions, r=10.)#调用孔径测光方法
    norm = ImageNormalize(stretch=SqrtStretch())
    #使用图片显示
    plt.imshow(image_data, cmap='Greys', origin='lower', norm=norm)
    apertures.plot(color='blue', lw=1.5, alpha=0.5)
    plt.savefig(png_absolute+'/'+file_name+'.png')
    plt.close()
