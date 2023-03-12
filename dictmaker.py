"""
@author: sway
"""

import os

t1bg = os.listdir(f'C:/Users/<Your username>Desktop/blobs/generation/nfts/backgrounds/T1')
t2bg = os.listdir(f'C:/Users/<Your username>Desktop/blobs/generation/nfts/backgrounds/T2')

t1darkbases = os.listdir(f'C:/Users/<Your username>Desktop/blobs/generation/nfts/bases/Basic/T1/Dark')
t1brightbases = os.listdir(f'C:/Users/<Your username>Desktop/blobs/generation/nfts/bases/Basic/T1/Bright')

t2darkbases = os.listdir(f'C:/Users/<Your username>Desktop/blobs/generation/nfts/bases/Basic/T2/Dark')
t2brightbases = os.listdir(f'C:/Users/<Your username>Desktop/blobs/generation/nfts/bases/Basic/T2/Bright')

t3darkbases = os.listdir(f'C:/Users/<Your username>Desktop/blobs/generation/nfts/bases/Basic/T3/Dark')
t3brightbases = os.listdir(f'C:/Users/<Your username>Desktop/blobs/generation/nfts/bases/Basic/T3/Bright')


def Convert(lst):
    lst2 = []
    for name in lst:
        name = name.replace(".png", "")
        lst2.append(name)
    res_dct = {lst2[i]: 1 for i in range(0, len(lst2))}
    return res_dct

def Convert2(lst):
    lst2 = []
    for name in lst:
        name = name.replace(".png", "")
        lst2.append(name)
    return lst2

def ConvertRare(lst, rarities):
    lst2 = []
    for name in lst:
        name = name.replace(".png", "")
        lst2.append(name)
    res_dct = {lst2[i]: rarities[i%9] for i in range(0, len(lst2))}
    return res_dct

#print('t2bg = ', ConvertRare(t2bg, [0.5,1,1,1,0.5,0.8,0.8,0.8,0.8]), end='\n')
print(Convert2(t3darkbases),Convert2(t3brightbases), end='\n')



'''print('t1darkbases = ',Convert(t1darkbases), end='\n')
print('t1brightbases = ',Convert(t1brightbases), end='\n')
print('t2darkbases = ',Convert(t2darkbases), end='\n')
print('t2brightbases = ',Convert(t2brightbases), end='\n')
print('t3darkbases = ',Convert(t3darkbases), end='\n')
print('t3brightbases = ',Convert(t3brightbases), end='\n')'''
