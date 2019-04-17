from astropy.io import fits
from photutils import find_peaks
from astropy.table import Table
from astropy.stats import sigma_clipped_stats
from astropy.nddata import NDData
from photutils.psf import extract_stars
import numpy
from photutils import DAOStarFinder
import warnings
import math
import matplotlib.pyplot as plt
from photutils import EPSFBuilder
import sourceFind
png_absolute = 'E:/GraduationProject/EPSFFive/png_data'
txt_absolute = 'E:/GraduationProject/EPSFFive/txt_data'
#添加的读取准确x,y的路径
lsd_path = 'E:/GraduationProject/EPSFFive/lsd/'
def ePSF(file_path, file_name):
    hdu1 = fits.open(file_path)
    data = hdu1[0].data[0]
    #使用find_peaks查找星星中心
    warnings.filterwarnings("ignore")
    # peaks_tbl = find_peaks(data, threshold=500.)
    # peaks_tbl['peak_value'].info.format='%.8g'
    mean_val, median_val, std_val = sigma_clipped_stats(data, sigma=3.0)
    #daofind = DAOStarFinder(fwhm=7.0, threshold=5.*std_val)
    #sources = daofind(data-median_val)
    sources = sourceFind.getSource(lsd_path+file_name[:-5]+'.txt')
    stars_tbl = Table()
    stars_tbl['x'] = sources['xcentroid']
    stars_tbl['y'] = sources['ycentroid']
    #在数据中减去背景
    print(data)
    print(median_val)
    data = data - float(median_val)
    #创建星星形状的切口
    nddata = NDData(data=data)
    #提取像素为25*25的像素切口,提取星星
    stars = extract_stars(nddata, stars_tbl, size=15)
    # print(stars[0].data)
    warnings.filterwarnings("ignore")
    epsf_builder = EPSFBuilder(oversampling=4, maxiters=15, progress_bar=False)
    epsf, fitted_stars = epsf_builder(stars)
    x=[]
    y=[]
    m=len(fitted_stars)
    txt_path = txt_absolute + '/' + file_name[:-5] + '.txt'
    f_write = open(txt_path, 'w')
    id=1
    for i in range(m):
        # 将数据输入到文件里面
        flux = fitted_stars[i].estimate_flux()
        if(flux<0):
            continue
        string = ""
        mag = 26.5 - 2.5*math.log(flux, 10)
        xcentroid = fitted_stars[i].center[0]
        ycentroid = fitted_stars[i].center[1]
        string = string + str(id) + ' ' + str(xcentroid) + ' ' + str(ycentroid) + ' ' + str(flux) + ' ' + str(mag) + ' ' + str(median_val) + ' 0\n'
        f_write.write(string)
        x.append(fitted_stars[i].center[0])
        y.append(fitted_stars[i].center[1])
        id=id+1
    #使用图片显示
    color = "#4A4AFF"
    area = numpy.pi*2**1
    plt.scatter(x,y,s=area,c=color,alpha=0.5,lw=1.5)
    plt.savefig(png_absolute + '/' + file_name + '.png')
    plt.close()

