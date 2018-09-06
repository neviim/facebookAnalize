# facebookAnalize

Algorítimo para analisar alguns dados fornecido pelo facebook em csv

""" Ambiente de trabalho 

    Emquanto em desenvolvimento e em beta teste este codigo funcionara na pasta pre-definida:

    ~/documents/github/_python_projetos/facebookAnalize"

    Posteriormente esta sendo ajustada para uso padrão, tambem exige en caso de windows que o anaconda python esteja instalado, ja que meus anigos resolverão todos usar windows, por motivo tecnico trabalhista, os que ainda resistem e lutão bravamente com o linux sera mais facil, pip install -r resolve tudo.

    Como a maioria do usuario windows não utilizam o prompt ai vai a receita do bolo.

    PS C:\Users\jorge $> conda activate py37
    (py37) C:\>

    (py37) C:\>jupyter notebook list
           Currently running servers:
           http://localhost:8888/?token=6031a497d4a65e264ea5874d47f49d2ac27b758dedc4d408 :: C:\Users\jorge

           ctrl+shift+p
           Jupyter: Enter com a url do local/remoto Jupyter Notebook

    (py37) C:\>

    # --- instalar dependencias no ambiente virtual que esta sendo utilizado.

    (py37) C:\> pip install -r requirements.txt
    (py37) C:\> cd src
    (py37) C:\> python analisar_poste.py


    # ---

    Se tiver usando vscode, com plugin para jupter instalado este codigo esta preparado para
    retornar resultados no ambiente do VS. ele atua utilizando uma instancia do Jupter que esteja ativa 
    bas para isso passar o endereço com o token no VScode.


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


    Autor: Neviim Jads, ;)
"""
