import glob 
import os
import random
lst = glob.glob('/kaggle/input/various-pokemon-image-dataset/ani/*.gif')
random_select = random.choices(lst, k=50)
for link in random_select:
    with open(link, 'rb') as r:
        with open(link.split('/')[-1],'wb') as w:
            w.write(r.read())
            


html = '<table>'

for idx, link in enumerate(random_select):
    if idx%10 == 0: 
        html += '<tr> '
    link = link.split('/')[-1]
    html += f'<td><img src=\'./{link}\'></td>'
    if idx%10 == 9:
        html += ' </tr>'

HTML(html)
