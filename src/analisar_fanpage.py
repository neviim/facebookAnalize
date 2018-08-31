''' Testando a plataforma: 

    (py37) C:\>jupyter notebook list
           Currently running servers:
           http://localhost:8888/?token=6031a497d4a65e264ea5874d47f49d2ac27b758dedc4d408 :: C:\Users\jorge.FCN
           http://localhost:8888/?token=f414b5de973f421c3317aabe88ea75b32bc957ae567918c7 :: C:\Users\jorge.FCN

    (py37) C:\>

    # --- instalar dependencias no ambiente virtual que esta sendo utilizado.

    (py37) C:\> pip install jieba
    (py37) C:\> pip install wordcloud  # https://github.com/amueller/word_cloud
    (py37) C:\> conda install -c conda-forge wordcloud

    # ---

    #%%
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    import numpy as np

    x = np.linspace(0, 20, 100)
    plt.plot(x, np.sin(x))
    plt.show() 

    referencias de trabalho:
        http://localhost:8888/notebooks/Documents/GitHub/_jupyter_codigo/Scatterplot.ipynb
        http://localhost:8888/notebooks/Documents/GitHub/_python_projetos/screping/referencia/facebook_fanpage_analysis/Facebook_fcn.ipynb

Autor: Neviim Jads '''

#%%
import sys
import os
import math
import datetime
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Defini a path do diretorio data, print(os.getcwd())
# C:\Users\jorge.FCN\Documents\GitHub\_python_projetos\facebookAnalize\data
path_proj = os.path.abspath(os.path.dirname("GitHub/_python_projetos/facebookAnalize/data/"))
pagina_id = "1-tri-Facebook.tw"
path_data = path_proj+'/'+pagina_id+'_post.csv'

# le o arquivo .csv e substitui NaN para 0
# print(df.notnull().all())
df_csv = pd.read_csv(path_data, encoding = 'utf8')
df = df_csv.fillna(0)

''' Renomear colunas
    df.rename(columns={"1":"V1Cont", "2":"V2Cont", "3":"V3Cont"}, inplace=True)
    df.head()

    print( df['link_permanente'][0] )
    print(df.notnull().all())
'''

df.rename(columns={"1":"V1Cont", "2":"V2Cont", "3":"V3Cont"}, inplace=True)

# Filtre e reindeixe novamente, porque o índice não é alterado quando o filtro é incorporado.
df = df[(df['total_publicacao']!=0) & (df['status_messagem'].notnull())].reindex()
df['datetime'] = df['status_publicado'].apply(lambda x: datetime.datetime.strptime(x,'%m/%d/%Y %H:%M:%S %p'))
df['weekday'] = df['datetime'].apply(lambda x: x.day_name())
df['hour'] = df['datetime'].apply(lambda x: x.hour)

print( df['weekday'].head() )

df.plot(x='datetime', y=['num_likes', 'num_other_cliks', 'num_link_clicks', 'num_photo_view', 'num_video_play', 'num_pub_corres'], figsize=(12,8))