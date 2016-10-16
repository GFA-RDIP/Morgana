
# coding: utf-8

# In[1]:

import pandas, numpy, os
from IPython.display import display, HTML
import plotly
import plotly.graph_objs as go
plotly.offline.init_notebook_mode()

get_ipython().magic(u'load_ext rpy2.ipython')


# In[4]:

data = pandas.read_csv("../HealthHack2016_Morgana_Data_permuted.csv", sep=",", index_col=0)
print data.shape
display(data.head())
print '\n'.join(data.columns)


# In[82]:

def plotProportion(target, columns):

    # create subset and split rows by values of splitCol
    targetValues = set(data[target])
    traces = []

    for value in targetValues:
        if pandas.isnull(value): continue
        columns.append(target)
        
        # calculate proportion of non-zeros against selected column
        indices = data[data[target]==value].index
        
        df = data.loc[indices,columns].dropna(how='all')
        values = []
        for col in columns:
            if col==target: continue
            values.append([len([item for item in df.loc[indices,col] if item>0])*1.0/len(df), col])
        values = sorted(values, reverse=True)

        #cols = ['eczema_diagnosis_1y','egg_allergy_1y']
        traces.append(go.Bar(x=[item[1] for item in values], 
                              y=[item[0] for item in values],
                              name="%s=%s" % (target,value)))
        
    layout = go.Layout(title="proportion of %s by other factors" % target, barmode="group")
    fig = go.Figure(data=traces, layout=layout)
    plot_url = plotly.offline.iplot(fig)    
    
plotProportion('peanut_allergy_1y',['eczema_diagnosis_1y','dog','sex','egg_allergy_1y'])


# In[59]:

def plotHeatmap(df):
    get_ipython().magic(u'R -i df -w 900 -h 900    library(pheatmap);    pheatmap(df)')


# In[69]:

def showHeatmap():
    allegyCols = ['eczema_diagnosis_1y', 'egg_SPT_1y', 'peanut_SPT_1y', 'sesame_SPT_1y', 'eggwh_ige_1y', 
                  'peanut_ige_1y', 'sesame_ige_1y', 'egg_allergy_1y', 'peanut_allergy_1y', 'sesame_allergy_1y', 
                  'any_foodal_1y', 'eczema_diagnosis_4y', 'egg_SPT_4y', 'peanut_SPT_4y', 'sesame_SPT_4y', 
                  'totalige_4y', 'eggwh_ige_4y', 'peanut_ige_4y', 'sesame_ige_4y', 'egg_allergy_4y', 
                  'peanut_allergy_4y', 'sesame_allergy_4y', 'any_foodal_4y']
    
    plotHeatmap(data[['dog','egg_allergy_1y','peanut_allergy_1y','eczema_diagnosis_1y','sex']].fillna(-1))
    #plotHeatmap(data.drop(['dob','FLG_combined'], axis=1).fillna(-1))
    
showHeatmap()

