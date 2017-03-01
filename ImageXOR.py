import matplotlib
import numpy as np
from PIL import Image

matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import scipy.misc

combine = np.zeros([2994,80,80], dtype=np.uint8)
sun = np.zeros([2994,160,160],dtype=np.uint8)
for i in range(2994):
    img_sun = np.array(Image.open('font_prepropress/output/hw_zs/' + str(i) + '.png').convert('L'))
    img_kai = np.array(Image.open('font_prepropress/output/simkai/' + str(i) + '.png').convert('L'))
    result = np.bitwise_xor(img_sun, img_kai)

    scipy.misc.imsave('outfile.jpg', result)
    im = Image.open('outfile.jpg')
    width, height = im.size
    im.thumbnail((width // 2, height // 2))
    im.save('font_prepropress/output/result/'+ str(i) + '.jpg', "jpeg")

    result = np.array(Image.open('font_prepropress/output/result/'+ str(i) + '.jpg'))
    combine[i,:,:] = result
    sun[i,:,:] = img_sun



#result = np.array(Image.open('outfile.jpg'))

# print(img_sun)
# print(img_sun.shape)
np.save('source.npy', sun)
np.save('target.npy', combine)
print(sun.shape)
print(combine.shape)
plt.figure("beauty")
plt.imshow(sun[0,:,:])
# plt.axis('off')
plt.show()
