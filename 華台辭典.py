import io
import csv
from 臺灣言語資料庫.資料模型 import 外語表
from django.forms.models import model_to_dict
 
def 顯示表格():
    for 一筆 in 外語表.objects.all():
        print(model_to_dict(一筆))

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
    print(row)
顯示表格()
    