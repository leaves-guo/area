#coding=GBK
import csv
import os
import matplotlib.pyplot as plt

dir_name='../市_县/'
csv_path='../mapdata/xian.csv'
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

sheng_dict={'34': '安徽', '82': '澳门', '11': '北京', '35': '福建', '62': '甘肃', '44': '广东', '45': '广西', '52': '贵州', '46': '海南', '13': '河北', '41': '河南', '23': '黑龙江', '42': '湖北', '43': '湖南', '22': '吉林', '32': '江苏', '36': '江西', '21': '辽宁', '15': '内蒙古', '64': '宁夏', '63': '青海', '37': '山东', '14': '山西', '61': '陕西', '31': '上海', '51': '四川', '71': '台湾', '12': '天津', '54': '西藏', '81': '香港', '65': '新疆', '53': '云南', '33': '浙江', '50': '重庆'}
shi_dict={'3408': '安庆', '3403': '蚌埠', '3416': '亳州', '3417': '池州', '3411': '滁州', '3412': '阜阳', '3401': '合肥', '3406': '淮北', '3404': '淮南', '3410': '黄山', '3415': '六安', '3405': '马鞍山', '3407': '铜陵', '3402': '芜湖', '3413': '宿州', '3418': '宣城', '8200': '澳门', '1101': '北京', '3501': '福州', '3508': '龙岩', '3507': '南平', '3509': '宁德', '3503': '莆田', '3505': '泉州', '3504': '三明', '3502': '厦门', '3506': '漳州', '6204': '白银', '6211': '定西', '6230': '甘南', '6202': '嘉峪关', '6203': '金昌', '6209': '酒泉', '6201': '兰州', '6229': '临夏', '6212': '陇南', '6208': '平凉', '6210': '庆阳', '6205': '天水', '6206': '武威', '6207': '张掖', '4451': '潮州', '4419': '东莞', '4406': '佛山', '4401': '广州', '4416': '河源', '4413': '惠州', '4407': '江门', '4452': '揭阳', '4409': '茂名', '4414': '梅州', '4418': '清远', '4405': '汕头', '4415': '汕尾', '4402': '韶关', '4403': '深圳', '4417': '阳江', '4453': '云浮', '4408': '湛江', '4412': '肇庆', '4420': '中山', '4404': '珠海', '4510': '百色', '4505': '北海', '4514': '崇左', '4506': '防城港', '4508': '贵港', '4503': '桂林', '4512': '河池', '4511': '贺州', '4513': '来宾', '4502': '柳州', '4501': '南宁', '4507': '钦州', '4504': '梧州', '4509': '玉林', '5204': '安顺', '5205': '毕节', '5201': '贵阳', '5202': '六盘水', '5226': '黔东南', '5227': '黔南', '5223': '黔西南', '5206': '铜仁', '5203': '遵义', '4690': '省直辖县级行政区划', '4604': '儋州', '4601': '海口', '4603': '三沙', '4602': '三亚', '1306': '保定', '1309': '沧州', '1308': '承德', '1304': '邯郸', '1311': '衡水', '1310': '廊坊', '1303': '秦皇岛', '1301': '石家庄', '1302': '唐山', '1305': '邢台', '1307': '张家口', '4105': '安阳', '4106': '鹤壁', '4190': '省直辖县级行政区划', '4108': '焦作', '4102': '开封', '4103': '洛阳', '4111': '漯河', '4113': '南阳', '4104': '平顶山', '4109': '濮阳', '4112': '三门峡', '4114': '商丘', '4107': '新乡', '4115': '信阳', '4110': '许昌', '4101': '郑州', '4116': '周口', '4117': '驻马店', '2306': '大庆', '2327': '大兴安岭', '2301': '哈尔滨', '2304': '鹤岗', '2311': '黑河', '2303': '鸡西', '2308': '佳木斯', '2310': '牡丹江', '2309': '七台河', '2302': '齐齐哈尔', '2305': '双鸭山', '2312': '绥化', '2307': '伊春', '4207': '鄂州', '4228': '恩施', '4211': '黄冈', '4202': '黄石', '4208': '荆门', '4210': '荆州', '4290': '省直辖县级行政区划', '4203': '十堰', '4213': '随州', '4201': '武汉', '4212': '咸宁', '4206': '襄阳', '4209': '孝感', '4205': '宜昌', '4307': '常德', '4310': '郴州', '4304': '衡阳', '4312': '怀化', '4313': '娄底', '4305': '邵阳', '4303': '湘潭', '4331': '湘西', '4309': '益阳', '4311': '永州', '4306': '岳阳', '4308': '张家界', '4301': '长沙', '4302': '株洲', '2208': '白城', '2206': '白山', '2202': '吉林', '2204': '辽源', '2203': '四平', '2207': '松原', '2205': '通化', '2224': '延边', '2201': '长春', '3204': '常州', '3208': '淮安', '3207': '连云港', '3201': '南京', '3206': '南通', '3205': '苏州', '3212': '泰州', '3202': '无锡', '3213': '宿迁', '3203': '徐州', '3209': '盐城', '3210': '扬州', '3211': '镇江', '3610': '抚州', '3607': '赣州', '3608': '吉安', '3602': '景德镇', '3604': '九江', '3601': '南昌', '3603': '萍乡', '3611': '上饶', '3605': '新余', '3609': '宜春', '3606': '鹰潭', '2103': '鞍山', '2105': '本溪', '2113': '朝阳', '2102': '大连', '2106': '丹东', '2104': '抚顺', '2109': '阜新', '2114': '葫芦岛', '2107': '锦州', '2110': '辽阳', '2111': '盘锦', '2101': '沈阳', '2112': '铁岭', '2108': '营口', '1529': '阿拉善', '1508': '巴彦淖尔', '1502': '包头', '1504': '赤峰', '1506': '鄂尔多斯', '1501': '呼和浩特', '1507': '呼伦贝尔', '1505': '通辽', '1503': '乌海', '1509': '乌兰察布', '1525': '锡林郭勒', '1522': '兴安盟', '6404': '固原', '6402': '石嘴山', '6403': '吴忠', '6401': '银川', '6405': '中卫', '6326': '果洛', '6322': '海北', '6302': '海东', '6325': '海南', '6328': '海西', '6323': '黄南', '6301': '西宁', '6327': '玉树', '3716': '滨州', '3714': '德州', '3705': '东营', '3717': '菏泽', '3701': '济南', '3708': '济宁', '3712': '莱芜', '3715': '聊城', '3713': '临沂', '3702': '青岛', '3711': '日照', '3709': '泰安', '3710': '威海', '3707': '潍坊', '3706': '烟台', '3704': '枣庄', '3703': '淄博', '1402': '大同', '1405': '晋城', '1407': '晋中', '1410': '临汾', '1411': '吕梁', '1406': '朔州', '1401': '太原', '1409': '忻州', '1403': '阳泉', '1408': '运城', '1404': '长治', '6109': '安康', '6103': '宝鸡', '6107': '汉中', '6110': '商洛', '6102': '铜川', '6105': '渭南', '6101': '西安', '6104': '咸阳', '6106': '延安', '6108': '榆林', '3101': '上海', '5132': '阿坝', '5119': '巴中', '5101': '成都', '5117': '达州', '5106': '德阳', '5133': '甘孜', '5116': '广安', '5108': '广元', '5111': '乐山', '5134': '凉山', '5105': '泸州', '5114': '眉山', '5107': '绵阳', '5113': '南充', '5110': '内江', '5104': '攀枝花', '5109': '遂宁', '5118': '雅安', '5115': '宜宾', '5120': '资阳', '5103': '自贡', '1201': '天津', '5425': '阿里', '5403': '昌都', '5401': '拉萨', '5404': '林芝', '5406': '那曲', '5402': '日喀则', '5405': '山南', '8100': '香港', '6529': '阿克苏', '6590': '自治区直辖县级行政区划', '6543': '阿勒泰', '6528': '巴音郭楞', '6527': '博尔塔拉', '6523': '昌吉', '6505': '哈密', '6532': '和田', '6531': '喀什', '6502': '克拉玛依', '6530': '克孜勒苏', '6542': '塔城', '6504': '吐鲁番', '6501': '乌鲁木齐', '6540': '伊犁', '5305': '保山', '5323': '楚雄', '5329': '大理', '5331': '德宏', '5334': '迪庆', '5325': '红河', '5301': '昆明', '5307': '丽江', '5309': '临沧', '5333': '怒江', '5308': '普洱', '5303': '曲靖', '5326': '文山', '5328': '西双版纳', '5304': '玉溪', '5306': '昭通', '3301': '杭州', '3305': '湖州', '3304': '嘉兴', '3307': '金华', '3311': '丽水', '3302': '宁波', '3308': '衢州', '3306': '绍兴', '3310': '台州', '3303': '温州', '3309': '舟山', '5001': '重庆'}

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
    shi_code=data[2][:4]
    area_name = shi_code
    if shi_code in shi_dict:
        area_name+="_" +shi_dict[shi_code]
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
        if shi_code!=data_lists[index_num+1][2][:4]:
            plt.savefig(dir_name + area_name)
            plt.close()
    except:
        plt.savefig(dir_name + area_name)
        plt.close()

