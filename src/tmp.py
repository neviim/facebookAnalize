# --- frequencia dos postes
''' calcula a frequencia de postes
    count    =>  quantidade processada      
     mean    =>  media de internalo de postagem
      std    =>  divisão padrão - standard deviation
      min    =>  minimo de intervalo de postagem
      25%    
      50%
      75%
      max    => periodo maximo sem uma postagem
'''
delta_datetime = df['datetime'].shift(1) - df['datetime']
delta_datetime_df = pd.Series(delta_datetime).describe().apply(str)
freq_postes_df = delta_datetime_df.to_frame(name='frequencia de postes')
#print( freq_postes_df )

# Numero de poster por semana
df_weekday = week_day(dict(df['weekday'].value_counts()))
#publ_semana_graf = sns.barplot(x='index', y='weekday', data = df_weekday)
#print( publ_semana_graf )

# Estatísticas sobre o número de postagens nos primeiros dias
df_hora = hora(dict(df['hour'].value_counts()))
#ax = sns.barplot(x='index', y='hour', data = df_hora)
#print(ax )

# Estatísticas sobre o número de tipos de publicações
#df_status_tipo = df['status_type'].value_counts().to_frame(name='status_type')
#grafico = sns.barplot(x='index', y='status_type', data = df_status_tipo.reset_index())
#print( grafico )

#
#grafico = sns.stripplot(x="status_type", y="num_likes", data=df, jitter=True)
#sns.stripplot(x="weekday", y="num_other_cliks", data=df, jitter=True)
#print( df )

sns.stripplot(x="weekday", y="num_likes", data=df, jitter=True)

