# -*- coding: utf-8 -*-
"""
Created on Fri May 15 20:25:03 2020

@author: rohit
"""


from ISR.models import RDN
import numpy as np
from PIL import Image

img = Image.open('0_0_0.jpg')
lr_img = np.array(img)

model = RDN(weights='psnr-large')
sr_img = model.predict(lr_img)
a = Image.fromarray(sr_img)
a.save('new2.jpg')