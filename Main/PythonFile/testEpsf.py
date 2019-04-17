from astropy.io import fits
import warnings
import math
from photutils import find_peaks
from astropy.table import Table
from astropy.stats import sigma_clipped_stats
from astropy.nddata import NDData
from photutils.psf import extract_stars
from photutils import DAOStarFinder
from photutils import EPSFBuilder
import numpy
hdu1 = fits.open('M35_2-I_001-2.fits')
data = hdu1[0].data[0]
#使用find_peaks查找星星中心
warnings.filterwarnings("ignore")
peaks_tbl = find_peaks(data, threshold=500.)
peaks_tbl['peak_value'].info.format='%.8g'
mean_val, median_val, std_val = sigma_clipped_stats(data, sigma=2)
daofind = DAOStarFinder(fwhm=3.0, threshold=5.*std_val)
sources = daofind(data-median_val)
#print(peaks_tbl)
stars_tbl = Table()
stars_tbl['x'] = sources['xcentroid']
stars_tbl['y'] = sources['ycentroid']
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
for star in fitted_stars:
    print(star.flux)
