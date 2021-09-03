from PIL import Image
import numpy as np
import math as m

def remove_mutual_factors(x,y):
    smallest = min((x,y))
    sqrt = m.floor(smallest**0.5)
    for i in range(2,sqrt):
        while x % i == 0 and y % i == 0:
            x /= i
            y /= i
    return int(x),int(y)

def enlargened_pixelsize(x_size, y_size, steps, treshold_percentage):
    """Return size of subgrid to give picture lower resolution, while keeping
       the dimension of the photo"""
    ratio = x_size/y_size # 1.7777 for 16:9
    x, y = 1, 1
    if treshold_percentage == 0: # look for duplicates
        x,y = remove_mutual_factors(x_size,y_size)
        if x==x_size or y==y_size:
            return x,y
        i = 1
        while i <= steps and x*steps<=x_size and y*steps<=y_size:
            x *= steps
            y *= steps
            i += 1
        return x,y
    prev_x = x
    idx = 1
    while idx < steps and x < x_size and y < y_size:
        if x/y > ratio+ratio*treshold_percentage:
            y += 1
        elif x/y < ratio-ratio*treshold_percentage:
            x += 1
        elif prev_x != x:
            idx += 1
            prev_x = x
        else:
            x += 1

    return x,y



im = Image.open('sindre og forsvarssjef 20.10.2020.jpg')
x_len, y_len = im.size
print('Image size', x_len, y_len)
pix = np.asarray(im)
new_pix = np.zeros_like(pix)


SIZE = 3

# new pixel, dimentions
x, y = enlargened_pixelsize(x_len,y_len,3,0)
# Quadratic
# x,y = SIZE,SIZE

print('X and Y:',x,y)


x_rest = x_len%x
y_rest = y_len%y
print('Start')
for i in range(0, y_len-y_rest, y):
    for j in range(0, x_len-x_rest, x):
        r,g,b = 0,0,0
        for k in range(y):
            r += np.sum(pix[i+k][j:j+x], axis=0)[0]
            g += np.sum(pix[i+k][j:j+x], axis=0)[1]
            b += np.sum(pix[i+k][j:j+x], axis=0)[2]
        average_color = [round(val/(x*y)) for val in (r,g,b)]
        for k in range(y):
            new_pix[i+k][j:j+x] = average_color
print('x_rest')
if x_rest:
    for i in range(0, y_len-y_rest, y): # Right column
        r,g,b = 0,0,0
        for j in range(y):
            r += np.sum(pix[i+j][x_len-x_rest:], axis=0)[0]
            g += np.sum(pix[i+j][x_len-x_rest:], axis=0)[1]
            b += np.sum(pix[i+j][x_len-x_rest:], axis=0)[2]
        average_color = [round(val/(x_rest*y)) for val in (r,g,b)]
        for j in range(y):
            new_pix[i+j][x_len-x_rest:] = average_color
print('y_rest')
if y_rest:
    for i in range(0, x_len-x_rest, x): # Bottom Row
        r,g,b = 0,0,0
        for j in range(y_len-y_rest, y_len):
            r += np.sum(pix[j][i:i+x], axis=0)[0]
            g += np.sum(pix[j][i:i+x], axis=0)[1]
            b += np.sum(pix[j][i:i+x], axis=0)[2]
        average_color = [round(val/(x*y_rest)) for val in (r,g,b)]
        for j in range(y_len-y_rest, y_len):
            new_pix[j][i:i+x] = average_color
print('both')
if x_rest and y_rest:
    r,g,b = 0,0,0
    for i in range(y_len-y_rest, y_len): # Right botton cell
        r += np.sum(pix[i][x_len-x_rest:], axis=0)[0]
        g += np.sum(pix[i][x_len-x_rest:], axis=0)[1]
        b += np.sum(pix[i][x_len-x_rest:], axis=0)[2]
    average_color = [round(val/(x_rest*y_rest)) for val in (r,g,b)]
    for i in range(y_len-y_rest, y_len):
        new_pix[i][x_len-x_rest:] = average_color

new_image = Image.fromarray(new_pix, 'RGB')
#new_image.save()
new_image.show()
