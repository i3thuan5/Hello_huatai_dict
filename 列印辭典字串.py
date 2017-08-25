import io
import csv

HuaTaiCsv = """ID,華語對譯,英文,台語羅馬字,台語漢字
1,曾祖父母,grandparents,a-chou2,阿祖
2,爺爺,grandfather,a-kong,阿公
3,媽媽,mother,a-bo2,阿母
"""
f = io.StringIO(HuaTaiCsv)
reader = csv.reader(f, delimiter=',')
for row in reader:
    print('\t'.join(row))