

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

