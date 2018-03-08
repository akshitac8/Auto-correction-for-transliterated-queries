from __future__ import division
from __future__ import print_function
import auto_correct as auto

gt_array=[]
inp_array=[]
f=open('substx.txt','rb').readlines()
for i in range(len(f)):
    gt_array.append(f[i].split(',')[0].split("'")[1].replace("?",""))
    inp_array.append(f[i].split(',')[1].split("'")[1].replace("?",""))

model = auto.auto_correct()

#==============================================================================
# p=model.run(words="hav rexd")
# print(p)
# pred_array=[]
# [pred_array.append(i) for i in p[0].split()]
#==============================================================================

mapx=[]
x=0
for i in range(len(gt_array)):
    x+=1
#    if x==5:
#        break
    gtx=[]
    inpx=[]
    p=model.run(words=inp_array[i])
    pred=[]
    [pred.append(ii) for ii in p[0].split()]
    for j in range(len(gt_array[i].split())):
        gtx.append(gt_array[i].split()[j])
        inpx.append(inp_array[i].split()[j])
    cc=0
    ic=0
    j=max(len(gtx),len(pred))
    k=-1
    print(pred)
    if x==4:
        print("pred",pred)
        print("gtx",gtx)
        print("inpx",inpx)
         

    while k<=j:
        k+=1
        try:
            if pred[k] in gtx and pred[k] not in inpx:
                cc+=1
            if gtx[k] != inpx[k] and gtx[k] not in pred:
#                if x==4:
#                    print(gtx[k])
                ic+=1
        except:
            pass
    mapx.append(cc/(cc+ic))
print("MAP",sum(mapx)/len(mapx))

#==============================================================================
# for i in range(len(gt_array)):
#     x+=1
#     gtx=[]
#     inpx=[]
#     p=model.run(words=inp_array[i])
#     pred_array=[]
#     [pred_array.append(ii) for ii in p[0].split()]
#     #print(pred_array)
#     for j in range(len(gt_array[i].split())):
#         gtx.append(gt_array[i].split()[j])
#         inpx.append(inp_array[i].split()[j])
#     print(len(gtx)-len(inpx))
#     cc=0
#     ic=0
#     k=max(len(gtx),len(pred_array))
#     j=0
#     while j<=k:
#     for k in range(len(pred_array)):
#         if pred_array[k] in gtx and pred_array[k] not in inpx:
#             cc+=1
#         else:
#             try:
#                 if gtx[k] != inpx[k] and pred_array[k] in inpx:
#                     if x==4:
#                         print(inpx[k])
#                     ic+=1
#             except:
#                 pass
#     if x==4:
#         print("pred_array",pred_array)
#         print("gtx",gtx)
#         print("inpx",inpx)
#         print("cc",cc)
#         print("ic",ic)
#         print("map",(cc/(cc+ic)))
#         break
#     mapx.append(cc/(cc+ic))
# print("MAP",sum(mapx)/len(mapx))
# 
#==============================================================================













#==============================================================================
# x=0
# for i in range(len(gt_array)):
#     x+=1
#     if x==2:
#         break
#     gtx=[]
#     inpx=[]
#     p=model.run(words=inp_array[i])
#     pred_array=[]
#     [pred_array.append(ii) for ii in p[0].split()]
#     print(pred_array)
#     for j in range(len(gt_array[i].split())):
#         gtx.append(gt_array[i].split()[j])
#         inpx.append(inp_array[i].split()[j])
#     cc=0
#     ic=0
#     for k in range(len(pred_array)):
#         try:
#             p=gtx.index(pred_array[k])
#         except:
#             p=-1
#         print(p)
#         print(gtx[k])
#         if p>=0:
#             if pred_array[k] != inpx[p]:
#                 cc+=1
#         else:
#             try:
#                 if gtx[k] != inpx[k]:
#                     print(gtx[k])
#                     ic+=1
#             except:
#                 pass
# #    mdict[gt_array[i]]=inp_array[i]
#  
#==============================================================================
#==============================================================================
#code to pred    
#for i in range(len(gt_array)):
#    model = auto.auto_correct()
#    prediction = model.run(words=inp_array[i])
#    print("Predicted",prediction)
#    x=map(inp_array[i],gt_array[i],prediction)
#    print(x)



#==============================================================================
# 
# import random
# str1 = 'how are you'
# str2 = []
# for i in str1.split():
#     flag= random.randint(0,1)
#     if flag:
#         i=i.replace(i[random.randint(0,len(i)-1)],'')
#     str2.append(i)
# str1=" ".join(str2)
# print str1
# 
#==============================================================================




#==============================================================================
# from __future__ import division
# import sys
# import os
# sys.path.append(os.path.abspath("./saved_model"))
# import auto_correct as auto
# def map(inp,gt,predicted):
#     p=0
#     q=0
#     gt=gt.split()
#     predicted=predicted.split()
#     inp=inp.split()
#     changed_words=[]
#     for i in range(len(gt)):
#         if inp[i]!=predicted[i]:
#             changed_words.append(i)
# #            print changed_words
#     for i in changed_words:
#         if gt[i]==predicted[i]:
#             p+=1
# #            print p
#     for i in range(len(gt)):
#         if inp[i]==gt[i]:
#             q+=1
#             print q
#     return p/(p+q)
# 
# 
# 
# gt         ='i am a good boy'
# predicted  ='i m a gud boy'
# inp        ='i m a gud bo'
# #model = auto.auto_correct()
# #model.run()
# 
# x=map(inp,gt,predicted)
# print x
#==============================================================================