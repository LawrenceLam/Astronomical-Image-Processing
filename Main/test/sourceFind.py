from astropy.stats import sigma_clipped_stats
from astropy.io import fits as Fits
import numpy as np
from photutils import DAOStarFinder
import matplotlib.pyplot as plt
from astropy.visualization import SqrtStretch
from astropy.visualization.mpl_normalize import ImageNormalize
from photutils import CircularAperture
from photutils import aperture_photometry
from astropy.table import Table
import math
import warnings
# path = 'E:/GraduationProject/newdata/NGC_2168_001.fits'
# hdu = Fits.open(path)
# image_data = hdu[0].data[0]
# warnings.filterwarnings('ignore')
# daofind = DAOStarFinder(fwhm=7.0, threshold=5.*100)
# sources = daofind(image_data)
# print(type(sources['xcentroid']))
# positions = (sources['xcentroid'],sources['ycentroid'])
path = 'E:/GraduationProject/lsd/NGC_2168_001.txt'
f_read = open(path, 'r')
x=[]
y=[]
datas = f_read.readlines()
for data in datas:
    ds = data.split()
    x.append(float(ds[1]))
    y.append(float(ds[2]))
source = Table([x, y], names=('xcentroid','ycentroid'))
positions = (source['xcentroid'],source['ycentroid'])
print(positions)
print(type(positions))
