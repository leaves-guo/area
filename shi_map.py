import csv
import os
import matplotlib.pyplot as plt

if not os.path.exists('./市'):
    os.mkdir('./市')

csv.field_size_limit(500 * 1024 * 1024)
data_list=csv.reader(open('../mapdata/shi.csv','r',encoding ='GB2312'))
data_lists=list(data_list)[1:]
for data in data_lists:
    area_name=data[2][:4]+ '_' +data[1]
    lonlats=data[0].replace('MULTIPOLYGON ','').split('),(')
    lonlats=[data.replace(')','').replace('(','') for data in lonlats]
    for lonlat in lonlats:
        lonlat_list=lonlat.split(',')
        lons=[float(i.split(' ')[0]) for i in lonlat_list]
        lats=[float(i.split(' ')[1]) for i in lonlat_list]
        # plt.rcParams['savefig.dpi'] = 600  # 图片像素
        # plt.rcParams['figure.dpi'] = 600  # 分辨率
        plt.plot(lons,lats,linewidth=0.5)
    plt.savefig('./市/{}.png'.format(area_name))
    plt.close()