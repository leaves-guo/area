#coding=GBK
import csv
import os
import matplotlib.pyplot as plt

dir_name='../ʡ_��/'
csv_path='../mapdata/xian.csv'
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

sheng_dict={'34': '����', '82': '����', '11': '����', '35': '����', '62': '����', '44': '�㶫', '45': '����', '52': '����', '46': '����', '13': '�ӱ�', '41': '����', '23': '������', '42': '����', '43': '����', '22': '����', '32': '����', '36': '����', '21': '����', '15': '���ɹ�', '64': '����', '63': '�ຣ', '37': 'ɽ��', '14': 'ɽ��', '61': '����', '31': '�Ϻ�', '51': '�Ĵ�', '71': '̨��', '12': '���', '54': '����', '81': '���', '65': '�½�', '53': '����', '33': '�㽭', '50': '����'}

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
        # plt.rcParams['savefig.dpi'] = 600  # ͼƬ����
        # plt.rcParams['figure.dpi'] = 600  # �ֱ���
        plt.plot(lons,lats,linewidth=0.5)

    try:
        if sheng_code!=data_lists[index_num+1][2][:2]:
            plt.savefig(dir_name + area_name)
            plt.close()
    except:
        plt.savefig(dir_name + area_name)
        plt.close()

