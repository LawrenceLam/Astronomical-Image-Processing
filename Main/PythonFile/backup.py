#确定星星的中心并且去除天空背景，进行孔径测光
import numpy as np
hdu = Fits.open('M35_2-I_001-2.FITS')
image = hdu[0].data[0].astype(float)
image -= np.median(image)

from photutils import DAOStarFinder
from astropy.stats import mad_std
bkg_sigma = mad_std(image)
daofind = DAOStarFinder(fwhm=4., threshold=3*bkg_sigma)
sources = daofind(image)
for col in sources.colnames:
    sources[col].info.format = '%.8g'
print(sources)
#检查背景和噪音
from astropy.stats import sigma_clipped_stats
from photutils import datasets
hdu = datasets.load_star_image()
data = hdu.data[0:401, 0:401]
print(data)
mean, median , std = sigma_clipped_stats(data,sigma=3.0)
print((mean, median, std))

from photutils import DAOStarFinder
daofind = DAOStarFinder(fwhm=3.0, threshold=5*std)
sources = daofind(data-median)
for col in sources.colnames:
    sources[col].info.format = '%.8g'
print(sources)

#绘制图像并且标注星星中心的位置
import matplotlib.pyplot as plt
from astropy.visualization import SqrtStretch
from astropy.visualization.mpl_normalize import ImageNormalize
from photutils import CircularAperture
positionns = (sources['xcentroid'], sources['ycentroid'])
apertures = CircularAperture(positionns, r=4)
norm = ImageNormalize(stretch=SqrtStretch())
plt.imshow(data, cmap='Greys', origin='lower', norm=norm)
apertures.plot(color='blue', lw=1.5, alpha=0.5)
plt.waitforbuttonpress()
