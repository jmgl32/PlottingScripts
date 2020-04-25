#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 17:33:26 2020

@author: glin
"""

#import librarys
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

#import data and replace 
data = pd.read_csv('LFCvsSig.csv')
#data['non-sig'] = data['non-sig'].replace(0,np.nan)
genehits = pd.read_csv('genehits.csv')

#plotting using seaborn
#plot non-significant points as scatter
g = sns.scatterplot(x = 'LFC',
                y = 'non-sig',
                data = data,
                color = 'black',
                linewidth = 0,
                s = 5)

#plot significant points as scatter
g = sns.scatterplot(x = 'LFC',
                y = 'significant',
                data = data,
                color = 'blue',
                linewidth = 0,
                s = 5)

#plot gene hits as red/bigger
#PML
plt.scatter(x = -0.8237161,
            y = 2.11844417,
            color = 'red',
            s = 20)
#ATF7
plt.scatter(x = -0.6382497,
            y = 1.34414154,
            color = 'red',
            s = 20)

#NT5DC2
plt.scatter(x = -0.6383952,
            y = 1.59670786,
            color = 'red',
            s = 20)

#PARP8
plt.scatter(x = -0.4565472,
            y = 1.3073204,
            color = 'red',
            s = 20)
    

#plot horizontal line
horiz = 1.30102999566
g.axhline(y = horiz, 
          color = 'black', 
          linewidth = 1, 
          alpha = 0.5)

#Annotate 

g.annotate('PML', 
           xy = (-0.8237161,2.11844417), 
           xytext= (-0.45, 2.2),
           arrowprops= dict(facecolor = 'black', width = 3, headwidth = 3))

g.annotate('ATF7', 
           xy = (-0.6382497,1.34414154), 
           xytext= (-0.35, 1.47),
           arrowprops= dict(facecolor = 'black', width = 3, headwidth = 3))

g.annotate('NT5DC2', 
           xy = (-0.6383952,1.59670786), 
           xytext= (-0.34, 1.8),
           arrowprops= dict(facecolor = 'black', width = 3, headwidth = 3))

g.annotate('PARP8', 
           xy = (-0.4565472,1.3073204), 
           xytext= (-0.1, 1.0),
           arrowprops= dict(facecolor = 'black', width = 3, headwidth = 3))



#title,axes
plt.title('Significantly Depleted Genes')
plt.xlabel('LFC')
plt.ylabel('Adjusted p-value')

plt.savefig("DepletedGenes.jpg",
            transparent = True)
plt.savefig("DepletedGenes.pdf",
            transparent = True)
