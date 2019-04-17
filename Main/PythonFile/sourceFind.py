from astropy.table import Table
def getSource(path):
    f_read = open(path, 'r')
    x = []
    y = []
    datas = f_read.readlines()
    for data in datas:
        ds = data.split()
        x.append(float(ds[1]))
        y.append(float(ds[2]))
    source = Table([x, y], names=('xcentroid', 'ycentroid'))
    return source
