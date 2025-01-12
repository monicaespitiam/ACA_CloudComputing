# Importación de librerías
import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# La función mostrar() carga toda la página

def mostrar():

  st.markdown('<h1 style="text-align: center">Análisis de Indicadores de Desarrollo de Colombia</h1>', unsafe_allow_html=True)
  st.header('Gráfico Producto Interno Bruto')

  # Conexión a la base de datos
  datos = pd.read_csv('Economia_Colombia.csv')
  conexion = sqlite3.connect(':memory:')
  datos.to_sql('economia', conexion, index=False)

  # Creación y ejecución de la consulta SQL
  consulta = '''
  SELECT economia.Año, 
         economia.'PIB (millones US$)' 
  FROM economia'''
  datosPIB = pd.read_sql_query(consulta, conexion)

  # Cálculo PIB máximo
  maxPIB = datosPIB['PIB (millones US$)'].max()
  anoMaximoPIB = datosPIB.loc[datosPIB['PIB (millones US$)'].idxmax(), 'Año']

  # Construcción del gráfico de barras
  fig = plt.figure(figsize=(10, 5)) 
  plt.bar(
      datosPIB['Año'], 
      datosPIB['PIB (millones US$)'], 
      color='blue', 
      label='PIB (millones US$)'
  )
  plt.xlabel('Año')
  plt.ylabel('PIB (millones US$)')
  plt.xticks(rotation=0)
  plt.ylim(0, maxPIB + 120000) 
  plt.annotate(
    f'''Valor máximo
    PIB: {maxPIB} millones US$
    Año: {anoMaximoPIB}''',
    xy = (anoMaximoPIB, maxPIB),
    xytext = (anoMaximoPIB, maxPIB + 12000), 
    ha='center'
  )
  plt.legend()
  plt.tight_layout()
  plt.grid()
  st.pyplot(fig)

  st.markdown('''
  El crecimiento del PIB de 1960 al año 2023 puede interpretarse de varias formas:
  
  <ul>
    <li>La subida sostenida a largo de los años refleja un crecimiento económico. Aunque el crecimiento fue lento en algunos periodos, la tendencia general es positiva.</li>
    <li>En 1960 la economía estaba centrada en la agricultura. Con el tiempo se ha presentado una diversificación económica en la industria, el comercio y los servicios.</li>
    <li>Los aumentos en la productividad laboral y tecnológica han contribuido al crecimiento del PIB. Además la adopción de nuevas tecnologías y la mejora en la infraestructura también han influido.</li>
    <li>La inversión extranjera y la apertura de la economía a mercados globales han impulsado el crecimiento económico.</li>
    <li>También podrían haber contribuido las reformas económicas y la estabilidad política.</li>                     
  </ul>                       
  ''', unsafe_allow_html=True)

  # Datos utilizados en el gráfico
  st.subheader('Datos utilizados en el gráfico')
  col1, col2 = st.columns([6, 3])

  with col1:
    st.write('''
    El resultado arrojó 64 registros, correspondientes a información anual entre los años 1960 y 2023. El código correspondiente es el siguiente:                  ''')
    codigo = """
    # Conexión a la base de datos
    datos = pd.read_csv('Economia_Colombia.csv')
    conexion = sqlite3.connect(':memory:')
    datos.to_sql('economia', conexion, index=False)

    # Creación y ejecución de la consulta SQL
    consulta = '''
    SELECT economia.Año, 
           economia.'PIB (millones US$)' 
    FROM economia'''
    datosPIB = pd.read_sql_query(consulta, conexion)
    """
    st.code(codigo, language='python')

  with col2:
    st.dataframe(datosPIB)  

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
  st.header('Gráfico Producto Interno Bruto')

  # Conexión a la base de datos
  datos = pd.read_csv('Economia_Colombia.csv')
  conexion = sqlite3.connect(':memory:')
  datos.to_sql('economia', conexion, index=False)

  # Creación y ejecución de la consulta SQL
  consulta = '''
  SELECT economia.Año, 
        economia.'PIB (millones US$)' 
  FROM economia'''
  datosPIB = pd.read_sql_query(consulta, conexion)

  # Cálculo PIB máximo
  maxPIB = datosPIB['PIB (millones US$)'].max()
  anoMaximoPIB = datosPIB.loc[datosPIB['PIB (millones US$)'].idxmax(), 'Año']

  # Construcción del gráfico de barras
  fig = plt.figure(figsize=(10, 5)) 
  plt.bar(
  datosPIB['Año'], 
  datosPIB['PIB (millones US$)'], 
  color='blue', 
  label='PIB (millones US$)'
  )
  plt.xlabel('Año')
  plt.ylabel('PIB (millones US$)')
  plt.xticks(rotation=0)
  plt.ylim(0, maxPIB + 120000) 
  plt.annotate(
  f'''Valor máximo
  PIB: {maxPIB} millones US$
  Año: {anoMaximoPIB}''',
  xy = (anoMaximoPIB, maxPIB),
  xytext = (anoMaximoPIB, maxPIB + 12000), 
  ha='center'
  )
  plt.legend()
  plt.tight_layout()
  plt.grid()
  st.pyplot(fig)

  st.markdown('''
  El crecimiento del PIB de 1960 al año 2023 puede interpretarse de varias formas:
  
  <ul>
  <li>La subida sostenida a largo de los años refleja un crecimiento económico. Aunque el crecimiento fue lento en algunos periodos, la tendencia general es positiva.</li>
  <li>En 1960 la economía estaba centrada en la agricultura. Con el tiempo se ha presentado una diversificación económica en la industria, el comercio y los servicios.</li>
  <li>Los aumentos en la productividad laboral y tecnológica han contribuido al crecimiento del PIB. Además la adopción de nuevas tecnologías y la mejora en la infraestructura también han influido.</li>
  <li>La inversión extranjera y la apertura de la economía a mercados globales han impulsado el crecimiento económico.</li>
  <li>También podrían haber contribuido las reformas económicas y la estabilidad política.</li>                     
  </ul>                       
  ''', unsafe_allow_html=True)

  # Datos utilizados en el gráfico
  st.subheader('Datos utilizados en el gráfico')
  col1, col2 = st.columns([6, 3])

  with col1:
  st.write('''
  El resultado arrojó 64 registros, correspondientes a información anual entre los años 1960 y 2023. El código correspondiente es el siguiente:                  ''')
  codigo = '''
  # Aquí va el código que ya se indicó más arriba en la sección 'Datos utilizados en el código'
  '''
  st.code(codigo, language='python')

  with col2:
  st.dataframe(datosPIB) 
  """ 
  st.code(codigo, language='python')