import xlrd
import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import os
import mpl_toolkits.mplot3d as p3d
import seaborn as sns

# 从excel文件中读取数据
def read(file):
    wb = xlrd.open_workbook(filename=file)  # 打开文件
    sheet = wb.sheet_by_index(0)  # 通过索引获取表格
    rows = sheet.nrows  # 获取行数
    all_content = []  # 存放读取的数据
    for j in range(0, 5):  # 取第1~第12列的数据
        temp = []
        for i in range(1, rows):
            cell = sheet.cell_value(i, j)  # 获取数据
            temp.append(float(cell))
        all_content.append(temp)  # 按列添加到结果集中
        temp = []
    return np.array(all_content)


datas = read('E:/Zequn Wang/Paper-亲疏水蒸发/画图/Fig7/工作簿1.xlsx')
# 方法选择person相关性
corre = np.corrcoef(datas)
np.set_printoptions(precision=4)  # 设置矩阵元素保留位数
print(corre)


plt.rcParams['figure.dpi'] = 300  # plt.show显示分辨率
font = {'family': 'serif',
        'serif': 'Times New Roman',
        'weight': 'bold',
        'size': 10}
plt.rc('font', **font)


fig = plt.figure(figsize=(12, 6))
ax = sns.heatmap(corre, cmap='PRGn', annot=True, vmin=-1,vmax=1)

plt.xticks([0.5,1.5,2.5,3.5,4.5],['Thickness','Coverage','Hydrophilic','Hydrophobic','Molecules'])
plt.yticks([0.5,1.5,2.5,3.5,4.5],['Thickness','Coverage','Hydrophilic','Hydrophobic','Molecules'])
plt.title("Pearson's correlation coefficient matrix",fontweight='bold',fontsize = 14)

plt.savefig('E:/Pycharm Project/pearson`s correlation coefficient/PRGn.png',dpi=600)
plt.show()
