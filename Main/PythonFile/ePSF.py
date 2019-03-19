from astropy.io import fits
from photutils import find_peaks
from astropy.table import Table
from astropy.stats import sigma_clipped_stats
from astropy.nddata import NDData
from photutils.psf import extract_stars
from astropy.visualization.mpl_normalize import ImageNormalize
from astropy.visualization import SqrtStretch
import warnings
from astropy.visualization import simple_norm
import matplotlib.pyplot as plt
from photutils import EPSFBuilder

hdu1 = fits.open('M35_2-I_001-2.fits')
data = hdu1[0].data[0]
#使用find_peaks查找星星中心
warnings.filterwarnings("ignore")
peaks_tbl = find_peaks(data, threshold=500.)
peaks_tbl['peak_value'].info.format='%.8g'
#print(peaks_tbl)
stars_tbl = Table()
stars_tbl['x'] = peaks_tbl['x_peak']
stars_tbl['y'] = peaks_tbl['y_peak']
mean_val, median_val, std_val = sigma_clipped_stats(data, sigma=2)
#在数据中减去背景
data -= median_val
#创建星星形状的切口
nddata = NDData(data=data)
#提取像素为25*25的像素切口,提取星星
stars = extract_stars(nddata, stars_tbl, size=10)
# print(stars[0].data)
warnings.filterwarnings("ignore")
epsf_builder = EPSFBuilder(oversampling=4, maxiters=3, progress_bar=False)
epsf, fitted_stars = epsf_builder(stars)
print(fitted_stars.data[0])
datas=[]
for i in (0,len(fitted_stars)-1):
    datas.append(fitted_stars.data[i])
print(datas)
norm = ImageNormalize(stretch=SqrtStretch())
#使用图片显示
plt.imshow(datas, cmap='Greys', origin='lower', norm=norm)
plt.waitforbuttonpress()

