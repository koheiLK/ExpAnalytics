#-*- coding: utf-8 -*-
#TCGAのデータを読み込み,希望するある１つの遺伝子についての発現を正常と癌で二群に分けてboxplotで表示するプログラム

print('Please wait...')

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

def load(genomic_matrix,clinical_data):
    _gdata = pd.read_csv(genomic_matrix, delimiter='\t', index_col=0)
    _cdata = pd.read_csv(clinical_data, delimiter='\t', index_col=0)
    gdata = _gdata.T
    cdata = _cdata['sample_type']
    return gdata, cdata

def aligndata(gdata,genename):
    picked_gdata = gdata[genename]
    eval_df = pd.concat([cdata, picked_gdata], axis=1, join='inner')
    return eval_df

if __name__ == '__main__': 
    gdata, cdata = load("genomicMatrix","clinical_data")
    genelist = list(gdata.T.index)
    
    print('Please enter your gene of interest.')
    genename = input('>>')
    
    if not genename in genelist:
        print('your GOI is not found')
        exit()
    
    eval_df = aligndata(gdata, genename)
    
    bp = eval_df.boxplot(column=genename, by='sample_type')
    plt.show()
