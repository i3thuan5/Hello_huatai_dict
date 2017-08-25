import io
import csv
from 臺灣言語資料庫.資料模型 import 外語表
from 臺灣言語資料庫.資料模型 import 文本表
from 臺灣言語資料庫.資料模型 import 來源表
from 臺灣言語資料庫.資料模型 import 版權表
from 臺灣言語資料庫.關係模型 import 翻譯文本表
from django.forms.models import model_to_dict
 
def 新增外語詞(哪種外語, 外語文字):
    外語資料 = {
        '外語語言': 哪種外語,
        '外語資料': 外語文字.strip(),
    }
    其他欄位 = {
        '收錄者': 來源表.objects.get_or_create(名='麥克華斯基')[0].編號(),
        '來源': 來源表.objects.get_or_create(名='小小華台辭典')[0].編號(),
        '版權': 版權表.objects.get_or_create(版權='會使公開')[0].pk,
        '種類': '字詞',
        '語言腔口': '臺語',
        '著作所在地': '臺灣',
        '著作年': '2017',
    }
    # 將其他欄位合併到外語資料
    外語資料.update(其他欄位)
    # (外語表 API)存入外語表
    一指標 = 外語表.加資料(外語資料)
    return 一指標

def 新增母語詞(外語指標, 台語羅馬字, 台語漢字):
    文本資料 = {
        '文本資料': 台語漢字,
        '音標資料': 台語羅馬字,
    }
    其他欄位 = {
        '收錄者': 來源表.objects.get_or_create(名='麥克華斯基')[0].編號(),
        '來源': 來源表.objects.get_or_create(名='小小華台辭典')[0].編號(),
        '版權': 版權表.objects.get_or_create(版權='會使公開')[0].pk,
        '種類': '字詞',
        '語言腔口': '臺語',
        '著作所在地': '臺灣',
        '著作年': '2017',
    }
    # 將其他欄位合併到外語資料
    文本資料.update(其他欄位)
    # (外語表 API)將該外語詞對應的台語詞存入文本表
    外語指標.翻母語(文本資料)

def 顯示表格():
    print('===外語表===')
    for 一筆 in 外語表.objects.all():
        print(model_to_dict(一筆))
    print('===文本表===')
    for 一筆 in 文本表.objects.all():
        print(model_to_dict(一筆))
    print('===翻譯文本表===')
    for 一對應關係 in 翻譯文本表.objects.all():
        print(model_to_dict(一對應關係))


#
# 主要程式
#    
HuaTaiCsv = """ID,華語對譯,英文,台語羅馬字,台語漢字
1,曾祖父母,grandparents,a-chou2,阿祖
2,爺爺,grandfather,a-kong,阿公
3,媽媽,mother,a-bo2,阿母
"""
f = io.StringIO(HuaTaiCsv)
reader = csv.DictReader(f, delimiter=',')
for row in reader:
    # Step 1. 將華語詞和英語詞加到外語表
    華語指標 = 新增外語詞('華語', row['華語對譯'])
    英文指標 = 新增外語詞('英文', row['英文'])
    # Step 2. 將它們對應的台語詞加到文本表
    新增母語詞(華語指標, row['台語羅馬字'], row['台語漢字'])
    新增母語詞(英文指標, row['台語羅馬字'], row['台語漢字'])

顯示表格()
    