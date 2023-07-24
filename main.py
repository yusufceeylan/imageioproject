import imageio.v3 as iio

im = iio.imread('karpuz.jpg')

im.shape

iio.imwrite('karpuz.gif', im)