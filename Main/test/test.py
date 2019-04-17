import matplotlib.pyplot as plt
path1 = 'E:/GraduationProject/EPSFFiveRevise/global/NGC_2168_001.txt'
path2 = 'E:/GraduationProject/EPSFFiveRevise/global/NGC_2168_002.txt'
f_read1 = open(path1, 'r')
data1 = f_read1.readlines()
f_read1.close()
f_read2 = open(path2, 'r')
data2 = f_read2.readlines()
f_read2.close()
x=[]
y=[]
for line1 in data1:
    datas1 = line1.split(' ')
    for line2 in data2:
        datas2 = line2.split(' ')
        if(datas1[0] == datas2[0]):
            print(datas1[0]+" "+datas2[0])
            # if abs(float(datas1[4])-float(datas2[4]))>0.05:
            #     continue
            x.append((float(datas1[5])+float(datas2[5]))/2)
            y.append(float(datas1[5])-float(datas2[5]))
            break
# plt.ylim(ymax=0.25)
plt.plot(x, y, 'ro')
plt.show()
