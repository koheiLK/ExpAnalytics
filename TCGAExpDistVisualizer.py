#TCGAのデータを読み込み,希望するある１つの遺伝子についての発現を正常と癌で二群に分けてboxplotで表示するプログラム

print('Please wait...')
import pandas as pd
df=pd.read_csv('genomicMatrix',delimiter='\t',index_col=0)
tdf=df.T
genelist=list(df.index)
print('Please enter your gene of interest.')
genename=input('>>')
if not genename in genelist:
	print('your GOI is not found')
	exit()
gdf=tdf[genename]
cdata=pd.read_csv('clinical_data',delimiter='\t',index_col=0)
tdf=cdata['sample_type']
fdf=pd.concat([tdf,gdf],axis=1,join='inner')

import matplotlib as mpl
import matplotlib.pyplot as plt

fig=plt.figure()
ax=fig.add_subplot(111)
bp=fdf.boxplot(column=genename,by='sample_type')
plt.show()

