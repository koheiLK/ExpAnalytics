#-*- coding: utf-8 -*-
#TCGAのデータを読み込み,希望するある１つの遺伝子についての発現を正常と癌で二群に分けてboxplotで表示するプログラム

print('Please wait...')

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


_gdata = pd.read_csv('genomicMatrix', delimiter='\t', index_col=0)
_cdata = pd.read_csv('clinical_data', delimiter='\t', index_col=0)

gdata = _gdata.T
cdata = _cdata['sample_type']
genelist = list(_gdata.index)

print('Please enter your gene of interest.')
genename = input('>>')
if not genename in genelist:
	print('your GOI is not found')
	exit()
picked_gdata = gdata[genename]
eval_df = pd.concat([cdata, picked_gdata], axis=1, join='inner')

fig = plt.figure()
ax = fig.add_subplot(111)
bp = eval_df.boxplot(column=genename, by='sample_type')
plt.show()


