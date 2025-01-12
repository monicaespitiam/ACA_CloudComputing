# Importación de librerías
import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# La función mostrar() carga toda la página

def mostrar():

  st.markdown('<h1 style="text-align: center">Análisis de Indicadores de Desarrollo de Colombia</h1>', unsafe_allow_html=True)
  st.header('Gráfico Inflación Anual')

  # Conexión a la base de datos
  datos = pd.read_csv('Economia_Colombia.csv')
  conexion = sqlite3.connect(':memory:')
  datos.to_sql('economia', conexion, index=False)

  # Creación y ejecución de la consulta SQL
  consulta = '''
  SELECT economia.Año, 
         economia.'Inflación precios al consumidor (% anual)' 
         AS 'Inflación (% anual)' 
  FROM economia'''
  datosInflacion = pd.read_sql_query(consulta, conexion)

  # Cálculo inflación máxima y mínima
  maxInflacion = datosInflacion['Inflación (% anual)'].max()
  anoMaximaInflacion = datosInflacion.loc[datosInflacion['Inflación (% anual)'].idxmax(), 'Año']
  minInflacion = datosInflacion['Inflación (% anual)'].min()
  anoMinimaInflacion = datosInflacion.loc[datosInflacion['Inflación (% anual)'].idxmin(), 'Año']

  # Construcción del gráfico
  fig = plt.figure(figsize=(10, 5)) 
  plt.plot(
      datosInflacion['Año'], 
      datosInflacion['Inflación (% anual)'], 
      color='red', 
      label='Inflación anual'
  )
  plt.xlabel('Año')
  plt.ylabel('Inflación (% anual)')
  plt.xticks(rotation=0)
  plt.ylim(0, maxInflacion + 20) 
  plt.annotate(
    f'''Valor máximo
    Inflación: {maxInflacion} %
    Año: {anoMaximaInflacion}''',
    xy = (anoMaximaInflacion, maxInflacion),
    xytext = (anoMaximaInflacion, maxInflacion+3), 
    ha='center'
  )
  plt.annotate(
    f'''Valor mínimo
    Inflación: {minInflacion} %
    Año: {anoMinimaInflacion}''',
    xy = (anoMinimaInflacion, minInflacion),
    xytext = (anoMinimaInflacion, minInflacion+6), 
    ha='center'
  )
  plt.legend()
  plt.tight_layout()
  plt.grid()
  st.pyplot(fig)

  st.write('''
  En el gráfico obtenido se observan tres picos máximos que corresponden a las inflaciones presentadas en los años 1963, 1977 y 1991, con valores de 26.36%, 33.8% y 30.39%, siendo el del año 1977 la mayor inflación presentada en los 64 años de información.

  Adicionalmente, se observan tres puntos mínimos en los años 2010, 2013 y 2020, con valores de 2.27%, 2.02% y 2.53%, siendo el menor de todos los datos el del año 2013.

  De otra parte, se observa el incremento fuerte que se presentó durante el año 2022, como consecuencia de la pandemia, y también la reducción de la intensidad de  crecimiento durante el año 2023. En los datos del Grupo Banco Mundial aún no se reporta la inflación de 2024 que podría ser del 5% aproximadamente.              
  ''')

  # Datos utilizados en el gráfico
  st.subheader('Datos utilizados en el gráfico')
  col1, col2 = st.columns([6, 3])

  with col1:
    st.write('''
    La consulta SQL fue realizada con el aporte de la librería Pandas. El resultado arrojó 64 registros, correspondientes a información anual entre los años 1960 y 2023. El código correspondiente es el siguiente:                  ''')
    codigo = """
    # Conexión a la base de datos
    datos = pd.read_csv('Economia_Colombia.csv')
    conexion = sqlite3.connect(':memory:')
    datos.to_sql('economia', conexion, index=False)

    # Creación y ejecución de la consulta SQL
    consulta = '''
    SELECT economia.Año, 
           economia.'Inflación precios al consumidor (% anual)' 
           AS 'Inflación (% anual)' 
    FROM economia'''
    datosInflacion = pd.read_sql_query(consulta, conexion)
    """
    st.code(codigo, language='python')

  with col2:
    st.dataframe(datosInflacion)  

  # Código de programación
  st.subheader('Código Python')
  codigo = """
  *
  # Importación de librerías
  import streamlit as st
  import sqlite3
  import pandas as pd
  import matplotlib.pyplot as plt

  # La función mostrar() carga toda la página

  def mostrar():

    st.markdown('<h1 style="text-align: center">Análisis de Indicadores de Desarrollo de Colombia</h1>', unsafe_allow_html=True)
    st.header('Gráfico Inflación Anual')

    # Conexión a la base de datos
    datos = pd.read_csv('Economia_Colombia.csv')
    conexion = sqlite3.connect(':memory:')
    datos.to_sql('economia', conexion, index=False)

    # Creación y ejecución de la consulta SQL
    consulta = '''
    SELECT economia.Año, 
          economia.'Inflación precios al consumidor (% anual)' 
          AS 'Inflación (% anual)' 
    FROM economia'''
    datosInflacion = pd.read_sql_query(consulta, conexion)

    # Cálculo inflación máxima y mínima
    maxInflacion = datosInflacion['Inflación (% anual)'].max()
    anoMaximaInflacion = datosInflacion.loc[datosInflacion['Inflación (% anual)'].idxmax(), 'Año']
    minInflacion = datosInflacion['Inflación (% anual)'].min()
    anoMinimaInflacion = datosInflacion.loc[datosInflacion['Inflación (% anual)'].idxmin(), 'Año']

    # Construcción del gráfico
    fig = plt.figure(figsize=(12, 6)) 
    plt.plot(
        datosInflacion['Año'], 
        datosInflacion['Inflación (% anual)'], 
        color='red', 
        label='Inflación anual'
    )
    plt.xlabel('Año')
    plt.ylabel('Inflación (% anual)')
    plt.xticks(rotation=0)
    plt.ylim(0, maxInflacion + 20) 
    plt.annotate(
      f'''Valor máximo
      Inflación: {maxInflacion} %
      Año: {anoMaximaInflacion}''',
      xy = (anoMaximaInflacion, maxInflacion),
      xytext = (anoMaximaInflacion, maxInflacion+3), 
      ha='center'
    )
    plt.annotate(
      f'''Valor mínimo
      Inflación: {minInflacion} %
      Año: {anoMinimaInflacion}''',
      xy = (anoMinimaInflacion, minInflacion),
      xytext = (anoMinimaInflacion, minInflacion+6), 
      ha='center'
    )
    plt.legend()
    plt.tight_layout()
    plt.grid()
    st.pyplot(fig)

    st.write('''
    En el gráfico obtenido se observan tres picos máximos que corresponden a las inflaciones presentadas en los años 1963, 1977 y 1991, con valores de 26.36%, 33.8% y 30.39%, siendo el del año 1977 la mayor inflación presentada en los 64 años de información.

    Adicionalmente, se observan tres puntos mínimos en los años 2010, 2013 y 2020, con valores de 2.27%, 2.02% y 2.53%, siendo el menor de todos los datos el del año 2013.

    De otra parte, se observa el incremento fuerte que se presentó durante el año 2022, como consecuencia de la pandemia, y también la reducción de la intensidad de  crecimiento durante el año 2023. En los datos del Grupo Banco Mundial aún no se reporta la inflación de 2024 que podría ser del 5% aproximadamente.              
    ''')

    # Datos utilizados en el gráfico
    st.subheader('Datos utilizados en el gráfico')
    col1, col2 = st.columns([6, 3])

    with col1:
      st.write('''
      La consulta SQL fue realizada con el aporte de la librería Pandas. El resultado arrojó 64 registros, correspondientes a información anual entre los años 1960 y 2023. El código correspondiente es el siguiente:                  ''')
      codigo = '''
      # Aquí va el código que ya se indicó más arriba en la sección 'Datos utilizados en el código'
      '''
      st.code(codigo, language='python')

    with col2:
      st.dataframe(datosInflacion)  
  """ 
  st.code(codigo, language='python')

