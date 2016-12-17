#-*- coding: utf-8 -*-
#Making boxplot that describes the expression of your gene-of-interest in primary tumor and normal tissue from TCGA datasets.

import pandas as pd
import matplotlib.pyplot as plt

def load(genomic_matrix,clinical_data):
    _gdata = pd.read_csv(genomic_matrix, delimiter='\t', index_col=0)
    _cdata = pd.read_csv(clinical_data, delimiter='\t', index_col=0)
    gdata = _gdata.T
    cdata = _cdata['sample_type']
    return gdata, cdata

def aligndata(gdata,cdata,genename):
    picked_gdata = gdata[genename]
    eval_df = pd.concat([cdata, picked_gdata], axis=1, join='inner')
    return eval_df

if __name__ == '__main__': 
    print("Please wait...")
    gdata, cdata = load("genomicMatrix","clinical_data")
    genelist = list(gdata.T.index)
    
    print('Please enter your gene of interest.')
    genename = input('>>')
    
    if not genename in genelist:
        print('your GOI is not found')
        exit()
    
    eval_df = aligndata(gdata, cdata, genename)
    
    bp = eval_df.boxplot(column=genename, by='sample_type')
    plt.show()
