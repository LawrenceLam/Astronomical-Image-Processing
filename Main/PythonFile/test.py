from astropy.io import fits
from astropy.stats import sigma_clipped_stats
from photutils import DAOStarFinder
from photutils import CircularAperture
from photutils import aperture_photometry

hdu = fits.open('M35_2-I_001-2.fits')
data = hdu[0].data[0]
mean, median, std = sigma_clipped_stats(data, sigma=3.0)
#输出平均，中位数，标准
print((mean, median, std))
#减去背景，使用DAOStarfinder查找图像中的恒星，恒星的fwhms大约为3像素，
# 峰值大约比背景高5西格玛。生成一个包含星体探测器结果的天体表：
daofind = DAOStarFinder(fwhm=3.0, threshold=5.*std)
sources = daofind(data-median)
#输出找到的所有星体信息
positions = (sources['xcentroid'], sources['ycentroid'])#位置
apertures = CircularAperture(positions, r=10.)#调用孔径测光方法
phot_table = aperture_photometry(data-median,apertures,method='subpixel',subpixels=10)
print(type(phot_table[0][3]))
