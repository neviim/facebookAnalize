# -*- coding: utf-8 -*-
#
__autor__ = "neviim jads"
__version__ = "1.0.0"

#%%
import sys
import os
import time
import math
import datetime
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class face_poster(object):
    '''[summary]
    
        Arguments:
            object {[type]} -- [description]
    '''
    def __init__(self, arquivo_id="1-tri-facebook.tw"):
        self.path_proj = os.path.expanduser("~/documents/github/_python_projetos/facebookAnalize")
        self.arquivo_id = arquivo_id
        self.path_arquivo_csv = ""
        self.itens = 0

    def ler_csv(self, path_projeto, arquivo):
        self.path_arquivo_csv = path_projeto+'/data/'+arquivo+'_post.csv'
        df_csv = pd.read_csv(self.path_arquivo_csv, encoding = 'utf8')
        df = df_csv.fillna(0)     # Substitui valores NaN por 0.      
        df = df.drop(df.index[0]) # elimina primeira linha do dataFrame
        self.itens = len(df)
        return df

    def renomea_colunas(self, dataframe):
        ''' Troca os nomes das colunas para facilitar o trabalho
                
            df.rename(
                columns={ "nome atual 1":"novo_nome_1",
                          "nome atual 2":"novo_nome_2",
                          "nome atual 3":"novo_nome_3"
                        }, 
                inplace=True
            )
            

            print( df.head() )
            print( df['link_name'][1] )
            print( df.notnull().all() )

            print( df['weekday'].head() )
            print( df['total_publicacao'] )
        '''
        dataframe.rename(
            columns={ "Número de identificação da publicação": "status_id",
                      "Link permanente": "link_name", 
                      "Publicar mensagem": "status_messagem",
                      "Tipo": "status_type",
                      "Publicado": "status_publicado",
                      "Vitalício: alcance total da publicação": "total_publicacao",
                      "Vitalício: consumidores de direcionamento do público com correspondência na publicação": "num_pub_corres",
                      "Vitalício: Falando sobre isso (publicação) por tipo de ação - like": "num_likes",
                      "Vitalício: Falando sobre isso (publicação) por tipo de ação - share": "num_shares",
                      "Vitalício: Falando sobre isso (publicação) por tipo de ação - comment": "num_comments",
                      "Consumos únicos de direcionamento para público de publicações vitalício por tipo - other clicks": "num_other_cliks",
                      "Consumos únicos de direcionamento para público de publicações vitalício por tipo - photo view": "num_photo_view",
                      "Consumos únicos de direcionamento para público de publicações vitalício por tipo - link clicks": "num_link_clicks",
                      "Consumos únicos de direcionamento para público de publicações vitalício por tipo - video play": "num_video_play"
                    }, 
            inplace=True)
        return dataframe

    def get_arquivo(self):
        return self.path_arquivo_csv

    def trimestre_periodo(self, todos=True, unico=1):
        """ Trimestre a ser gerado de 1 a 4 ou todos
        
            Arguments:
                todos {[logico]} -- [Verdadeiro = gera todos]
                unico {[int]}    -- [caso for trimestre unico, o seu numero]

            Retorno:
                Retorna parametro duplo, sendo eles:

                    tri_start {[Int]} -- [Trimesrte inicial]
                    trimestre {[Int]} -- [Trimestre final]
        """
        if todos:
            trimestre = 4
            tri_start = 0
        else:
            fun = lambda x: x > 4 and 4 or x
            trimestre = fun(unico)
            tri_start = trimestre-1
            
        return(tri_start, trimestre)

    def hora(self, dhora):
        list_key = range(1,23)
        list_value = []

        for one in list_key:
            if one in dhoras.keys():
                list_value.append(horas[one])
            else:
                list_value.append(0)

        v_df = pd.DataFrame(index = list_key, data = {'hour': list_value}).reset_index()
        return v_df      

    def filtra_reindexa(self, df, publicacao, menssagem):
        """ Esta é uma função que ira filtrar e reindexar o data freme 
        
            Arguments:
                datafreme  {[df]}     -- [datafreme, todos os campos estruturado do arquivo lido]
                publicacao {[string]} -- [contem o campo "total_prodicao" do arquivo lido.]
                menssagem  {[string]} -- [contem o campo "status_messagem" do arquivo lido ]

            Utilização:
                filtra_reindexa(df, "total_publicacao", "status_messagem")

            Retorna:
                estrutura em um formato datafreme
        """
        df = df[(df[publicacao]!=0) & (df[menssagem].notnull())].reindex()
        df['datetime'] = df['status_publicado'].apply(lambda x: datetime.datetime.strptime(x,"%m/%d/%Y %H:%M:%S %p"))
        df['weekday'] = df['datetime'].apply(lambda x: x.day_name())
        df['hour'] = df['datetime'].apply(lambda x: x.hour)
        return df

    def gera_grafico_cliks(self, df, nome_arquivo='grafico_cliks.png'):
        """ função para gravar um grafico analizando os cliks no poste
        
            Arguments:
                df {[dataframe]} -- [dataframe com os dados de onde grafico sera gerado]
            
            Keyword Arguments:
                nome_arquivo {str} -- [nome do arquivo do grafio que sera gerado] (default: {'grafico'}), a estenção sera colocada altomaticamente .png

            Retorno:
                True    -- [verdadeiro em caso de haver mais de um registro gerado]
                False   -- [falso em cado de nao haver registro gerado]
        """
        if self.itens > 0:
            df.plot(x='datetime', y=['num_likes', 'num_photo_view', 'num_video_play', 'num_other_cliks', 'num_link_clicks', 'num_pub_corres'], figsize=(12,8))
            plt.savefig( self.path_proj+'/grafigos/'+nome_arquivo+'_cliks.png' )
            return True
        else:
            return False

    def gera_grafico_comentarios(self, df, nome_arquivo='grafico_comentarios.png'):
        """ função para gravar um grafico_comentarios analizando os comentarios no poste
        
            Arguments:
                df {[dataframe]} -- [dataframe com os dados de onde grafico_comentarios sera gerado]
            
            Keyword Arguments:
                nome_arquivo {str} -- [nome do arquivo do grafio que sera gerado] (default: {'grafico_comentarios'}), a estenção sera colocada altomaticamente .png

            Retorno:
                True    -- [verdadeiro em caso de haver mais de um registro gerado]
                False   -- [falso em cado de nao haver registro gerado]
        """
        if self.itens > 0: 
            df.plot(x='datetime', y=['num_likes', 'num_comments', 'num_shares'], figsize=(12,8))
            plt.savefig( self.path_proj+'/grafigos/'+nome_arquivo+'_comentarios.png' )
            return True
        else:
            return False

    def frequencia_postagem(self, df):
        """ fraquencia das postagens
        
            Arguments:
                df {[datafreme]} -- [df]

                Retorna:
                    count =>  quantidade processada      
                    mean =>  media de internalo de postagem
                    std  =>  divisão padrão - standard deviation
                    min  =>  minimo de intervalo de postagem
                    25%    
                    50%
                    75%
                    max  => periodo maximo sem uma postagem 
        """
        if self.itens > 0:
            delta_datetime = df['datetime'].shift(1) - df['datetime']
            delta_datetime_df = pd.Series(delta_datetime).describe().apply(str)
            freq_postes_df = delta_datetime_df.to_frame(name='frequencia de postes '+self.arquivo_id[:-12]+'mestre')
            return freq_postes_df
        else:
            return ''

    def dia_semana(self, df):
        list_key = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        list_value = []

        if self.itens > 0:
            for key in list_key:
                if key in df.keys():
                    list_value.append(df[key])
                else:
                    list_value.append(0)

            df_resultado = pd.DataFrame(index = list_key, data = {'weekday': list_value}).reset_index()
            return (df_resultado, True)
        else:
            return ('', False)

    def gera_grafico_dia_semana(self, nome_trimestre, dados_poste_semana, imprime=False):
        """ gera grafico e inprime quantidade de poster por dia da semana
        
            Arguments:
                nome_trimestre      {[str]}      -- [nome do trimestre correspondente]
                dados_poste_semana  {[data]}     -- [dados relativo ao trimestre a ser impresso]
                Imprime             {[Borleano]  -- [verdadeiro mostra na tela, falso não]

            Retorno:
                Grafico gerado dos dias da semana
                A impressão dos dados do trimestre correspondente em tela
        """
        grafico_ax = sns.barplot(x='index', y='weekday', data=dados_poste_semana)
        grafico_ax.figure.savefig(self.path_proj+'/grafigos/'+nome_trimestre+'_dia_semana.png')
        
        # caso queira ver os numeros em tela
        if imprime:
            print( nome_trimestre )
            print( dados_poste_semana )
            print( self.itens )
   
        return




def main():
    # defini path e ip do arquivo
    path_proj = os.path.expanduser("~/documents/github/_python_projetos/facebookAnalize")
    arqv_id = "1-tri-facebook.tw"

    tri_unico = 3      # trimestre unico a sera gerado
    tri_todos = False  # imprime todos os trimestres

    # instancia a classe poster
    poster = face_poster(arqv_id)
    tri_start, trimestre = poster.trimestre_periodo(tri_todos, tri_unico) 

    # loop de trimestre a ser gerados
    for n in range(tri_start, trimestre):
        arqv_id = str(n+1)+arqv_id[1:]
        #poster = face_poster(arqv_id)

        # abre arquivo e renomeia colunas 
        dfreme = poster.ler_csv(path_proj, arqv_id)
        dfreme = poster.renomea_colunas( dfreme )
        #print( dfreme["link_name"][1] )

        # filtrando datafreme
        dfreme_filtrado = poster.filtra_reindexa(dfreme, "total_publicacao", "status_messagem")
        #print( dfreme_filtrado )

        # gera os graficos por trimestre dos cliks
        #poster.gera_grafico_cliks(dfreme_filtrado, arqv_id)

        # gera os graficos por trimestre dos comentarios 
        #poster.gera_grafico_comentarios(dfreme_filtrado, arqv_id)

        # frequencia de postagem
        frequencia = poster.frequencia_postagem(dfreme_filtrado)
        print(frequencia)
        print()

        # publicação por semana
        poste_semana, status = poster.dia_semana(dict(dfreme_filtrado['weekday'].value_counts()))
        if status:
            poster.gera_grafico_dia_semana(arqv_id[:-12]+'mestre', poste_semana, False)
            print(arqv_id)
           

    return
    


if __name__ == '__main__':
    main()
