#coding=GBK
import csv
import os
import matplotlib.pyplot as plt

dir_name='../省_县/'
csv_path='../mapdata/xian.csv'
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

sheng_dict={'34': '安徽', '82': '澳门', '11': '北京', '35': '福建', '62': '甘肃', '44': '广东', '45': '广西', '52': '贵州', '46': '海南', '13': '河北', '41': '河南', '23': '黑龙江', '42': '湖北', '43': '湖南', '22': '吉林', '32': '江苏', '36': '江西', '21': '辽宁', '15': '内蒙古', '64': '宁夏', '63': '青海', '37': '山东', '14': '山西', '61': '陕西', '31': '上海', '51': '四川', '71': '台湾', '12': '天津', '54': '西藏', '81': '香港', '65': '新疆', '53': '云南', '33': '浙江', '50': '重庆'}

csv.field_size_limit(500 * 1024 * 1024)


def bubble_sort(num):
    for i in range(len(num)-1):
        for j in range(len(num)-1-i):
            if int(num[j][2])>int(num[j+1][2]):
                num[j],num[j+1]=num[j+1],num[j]
    return num


csv.field_size_limit(500 * 1024 * 1024)
data_lists_1=list(csv.reader(open(csv_path,'r',encoding ='GBK')))[1:-1]
for i in data_lists_1:
    print(i[1:])
data_lists=bubble_sort(data_lists_1)


for data in data_lists:
    index_num=data_lists.index(data)
    print(data[1:])
    sheng_code=data[2][:2]
    area_name = sheng_code
    if sheng_code in sheng_dict:
        area_name+="_" +sheng_dict[sheng_code]
    lonlats=data[0].replace('MULTIPOLYGON ','').split('),(')
    lonlats=[data.replace(')','').replace('(','') for data in lonlats]
    for lonlat in lonlats:
        lonlat_list=lonlat.split(',')
        lons=[float(i.split(' ')[0]) for i in lonlat_list]
        lats=[float(i.split(' ')[1]) for i in lonlat_list]
        # plt.rcParams['savefig.dpi'] = 600  # 图片像素
        # plt.rcParams['figure.dpi'] = 600  # 分辨率
        plt.plot(lons,lats,linewidth=0.5)

    try:
        if sheng_code!=data_lists[index_num+1][2][:2]:
            plt.savefig(dir_name + area_name)
            plt.close()
    except:
        plt.savefig(dir_name + area_name)
        plt.close()

