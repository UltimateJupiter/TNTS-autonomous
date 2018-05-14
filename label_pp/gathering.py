import json
import os
from tqdm import tqdm
from IPython import embed

assert os.getcwd() == "/home/thusn/zhuxingyu/TNTS-autonomous/label_pp", os.getcwd()

fl_ls = []
file_dests_1 = '/home/thusn/zhuxingyu/SN-Open-Space-Catalog/sne-2015-2019/'
for x in os.listdir(file_dests_1):
    if '.json' in x:
        fl_ls.append(file_dests_1 + x)

file_dests_2 = '/home/thusn/zhuxingyu/SN-Open-Space-Catalog/sne-2010-2014/'
for x in os.listdir(file_dests_2):
    if '.json' in x:
        fl_ls.append(file_dests_2 + x)

print(len(fl_ls))

def filter_from_name(i):
    o = i.split('/')[-1][:-5]
    return o

pendings = []
full_tags = []
for fl in tqdm(fl_ls):
    try:
        name = filter_from_name(fl)
        info = json.load(open(fl))
    
    except:
        continue
    
    assert name in info, (name,info)

    print(info.keys())
    if 'dec' in info[name] and 'ra' in info[name]:
        pendings.append(info[name])
    
    '''
    if full_tags == []:
        full_tags = set(list(info[name].keys()))
    full_tags = full_tags&set(list(info[name].keys()))
    print(full_tags)
    '''

# print(full_tags)
print(ra)
