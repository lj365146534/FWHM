# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 15:50:21 2022

@author: Ja
"""
from scipy.signal import find_peaks
import matplotlib.pyplot as plt
import numpy as np
data = np.loadtxt('data.csv',delimiter = ',',skiprows=1)
distance = data[:,0]
spot_crop = data[:,1]

plt.plot(data)
plt.xlabel("Distance")
plt.ylabel("Spot_crop")

peak_index,peak_heights = find_peaks(spot_crop,height=1000)
# print(peak_heights)
output = open('out.tsv','w')
output.write('Start\tEnd\tWide\tfwhm_distance_element\tfwhm_spot_crop_element\n')
# wave_up = []
# wave_down = []

# for i in range(len(spot_crop)):
#     if spot_crop[i] >= 1000:
#         if spot_crop[i+1]> spot_crop[i] > spot_crop[i-1]:
#             wave_up.append(spot_crop[i])
#         elif spot_crop[i+1]< spot_crop[i] < spot_crop[i-1]:
#             wave_down.append(spot_crop[i])
#         elif spot_crop[i+1]< spot_crop[i] > spot_crop[i-1]:
#             peak = spot_crop[i]
#             wave_up.append(spot_crop[i])
#         elif spot_crop[i+1]> spot_crop[i] < spot_crop[i-1]:
            


for i in range(len(peak_index)):
    # print(i-1,i)
    # print(peak_heights['peak_heights'][i])
    # print(peak_index[i])
    if i ==0:
        distance_filed = distance[:peak_index[i+1]]
        spot_crop_filed = spot_crop[:peak_index[i+1]]
        min_y = max([min(spot_crop_filed[:peak_index[i]]),min(spot_crop_filed[peak_index[i]:]),])
        wave = spot_crop_filed[list(spot_crop_filed).index(min(spot_crop_filed[:peak_index[i]])):peak_index[i]+list(spot_crop_filed[peak_index[i]:]).index(min(spot_crop_filed[peak_index[i]:]))]
        wave_distance = distance_filed[list(spot_crop_filed).index(min(spot_crop_filed[:peak_index[i]])):peak_index[i]+list(spot_crop_filed[peak_index[i]:]).index(min(spot_crop_filed[peak_index[i]:]))]
        print(list(spot_crop_filed).index(min(spot_crop_filed[:peak_index[i]])))
        print(peak_index[i]+list(spot_crop_filed[peak_index[i]:]).index(min(spot_crop_filed[peak_index[i]:])))
    elif i == len(peak_index)-1:
        distance_filed = distance[peak_index[i-1]:]
        spot_crop_filed = spot_crop[peak_index[i-1]:]
        min_y = max([min(spot_crop_filed[:peak_index[i]-peak_index[i-1]]),min(spot_crop_filed[peak_index[i]-peak_index[i-1]:]),])
        wave = spot_crop[peak_index[i-1]+list(spot_crop[peak_index[i-1]:peak_index[i]]).index(min(spot_crop[peak_index[i-1]:peak_index[i]])):]
        wave_distance = distance[peak_index[i-1]+list(spot_crop[peak_index[i-1]:peak_index[i]]).index(min(spot_crop[peak_index[i-1]:peak_index[i]])):]
        print(i,"\n",peak_index[i-1]+list(spot_crop[peak_index[i-1]:peak_index[i]]).index(min(spot_crop[peak_index[i-1]:peak_index[i]])))
        # print(peak_index[i]+list(spot_crop[peak_index[i]:peak_index[i+1]:]).index(min(spot_crop[peak_index[i]:peak_index[i+1]:])))
    else:
        distance_filed = distance[peak_index[i-1]:peak_index[i+1]]
        spot_crop_filed = spot_crop[peak_index[i-1]:peak_index[i+1]]
        min_y = max([min(spot_crop[peak_index[i-1]:peak_index[i]]),min(spot_crop[peak_index[i]:peak_index[i+1]:]),])
        wave = spot_crop[peak_index[i-1]+list(spot_crop[peak_index[i-1]:peak_index[i]]).index(min(spot_crop[peak_index[i-1]:peak_index[i]])):peak_index[i]+list(spot_crop[peak_index[i]:peak_index[i+1]:]).index(min(spot_crop[peak_index[i]:peak_index[i+1]:]))]
        wave_distance = distance[peak_index[i-1]+list(spot_crop[peak_index[i-1]:peak_index[i]]).index(min(spot_crop[peak_index[i-1]:peak_index[i]])):peak_index[i]+list(spot_crop[peak_index[i]:peak_index[i+1]:]).index(min(spot_crop[peak_index[i]:peak_index[i+1]:]))]
        print(i,"\n",peak_index[i-1]+list(spot_crop[peak_index[i-1]:peak_index[i]]).index(min(spot_crop[peak_index[i-1]:peak_index[i]])))
        print(peak_index[i]+list(spot_crop[peak_index[i]:peak_index[i+1]:]).index(min(spot_crop[peak_index[i]:peak_index[i+1]:])))
    tt = peak_index[i]-peak_index[i-1]
    ttt = spot_crop_filed[:peak_index[i]-peak_index[i-1]]
    # min_y = max([min(spot_crop_filed[:peak_index[i]-peak_index[i-1]]),min(spot_crop_filed[peak_index[i]-peak_index[i-1]:]),])
    max_y = spot_crop[peak_index[i]]
    xs = [x for x in range(len(wave)) if wave[x] >= (max_y-min_y)/2]
    fwhm_distance = [wave_distance[x] for x in range(len(wave)) if wave[x] >= (max_y-min_y)/2]
    fwhm_spot_crop = [wave[x] for x in range(len(wave)) if wave[x] >= (max_y-min_y)/2]
    print(fwhm_distance[-1]-fwhm_distance[0])
    start = fwhm_distance[0]
    end = fwhm_distance[-1]
    wide = end - start
    fwhm_distance_element = ','.join([str(i) for i in fwhm_distance])
    fwhm_spot_crop_element = ','.join([str(i) for i in fwhm_spot_crop])
#    xs = [x for x in  distance_filed if spot_crop_filed[]]
    # print(wave_filed)
    output.write('{}\t{}\t{}\t{}\t{}\n'.format(start,end,wide,fwhm_distance_element,fwhm_spot_crop_element))
    
output.close()
    
    


