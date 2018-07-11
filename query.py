import io
import os
import cv2
import urllib2
import requests
import PIL.Image
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread, imsave

#
# 7 x 13 grid (x and y)
#

url = 'https://lh3.ggpht.com/p/'

def GetContent(link):
    re = urllib2.Request(link)
    f = urllib2.urlopen(re)
    data = f.read()
    f.close()
    return data

def GetPano(ID):
    x_range = range(13)
    y_range = range(7)
    big = np.zeros([512*7, 512*13, 3], np.uint8)
    for x in x_range:
        for y in y_range:
            cur_url = '%s%s=x%d-y%d-z4'%(url, ID, x, y)
            data = GetContent(cur_url)
            picture_stream = io.BytesIO(data)
            pic = PIL.Image.open(picture_stream)
            img = np.asarray(pic)
            
            big[y*512:(y+1)*512, x*512:(x+1)*512, :] = img
    [h, w, _] = big.shape

    big = big[:w/2, :, :]
    return big

if __name__ == '__main__':
    
    finish = []
    lst = ['label1.txt', 'label2.txt']
    for one in lst:
        with open(one, 'r') as f:
            for line in f:
                panoid, angle = line[:-1].split(' ')
                if panoid not in finish:
                    print panoid
                    img = img = GetPano(panoid)
                    img = cv2.resize(img, (2048, 1024), cv2.INTER_AREA)
                    #img = cv2.resize(img, (1024, 512), cv2.INTER_AREA)
                    imsave('raw/%s.png'%panoid, img)
                    finish.append(panoid)
