from AppendD import AppendData
import os
from random import *
file=[]
vehicle=[]
id=1
path = 'cabspottingdata'
file_list=os.listdir(path)
# print("lenfile_list",len(file_list),file_list[:10])
for f in file_list[:10]:
    f = path+'/'+f
    with open(f,'r') as rf:
        l = rf.readlines()
    v,road,time = AppendData(l).extract_vid()
    if len(road) >=4:
        vid = 'vid'+str(id)
        vehicle.append(vid)
        file.append(f)
        file.append('\n')
        id+=1
    if len(road) >= 4:
        print("file",f)
        print("road", list(reversed(road)))
        print("time", list(reversed(time)))
        vehicle.append(list(reversed(road)))
        vehicle.append(list(reversed(time)))
        print("++++++++++")

print("veh",vehicle)
with open("file.txt",'w') as f:
    for i in file:
        f.write(i)

#sample
# flist=['cabspottingdata/new_abboip.txt', 'cabspottingdata/new_abdremlu.txt']
#
# for i in flist:
#     print("i",i)
#     with open(i,'r') as f:
#         ff = f.readlines()
#     v = AppendData(ff).extract_vid()
#
#     if len(v) != 0:
#         file.append(i)
#         file.append('\n')
# print("file",file)
#
# with open("file.txt",'w') as f:
#     for i in file:
#         f.write(i)
#sample


# 10m/s(36km/h) ~ 최대 18m/s(65km/h)로
