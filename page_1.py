import streamlit as st

# La función mostrar() carga toda la página

def mostrar():

  st.markdown('<h1 style="text-align: center">Análisis de Indicadores de Desarrollo de Colombia</h1>', unsafe_allow_html=True)

  st.header('Descripción general')

  st.markdown('''
  Este trabajo se basa en la información suministrada por el <strong>Grupo Banco Mundial</strong>, organización que tiene como objetivo poner fin a la pobreza extrema y promover la prosperidad compartida en un planeta habitable. Agrupa a las siguientes instituciones:
  <ul>
    <li>Banco Internacional de Reconstrucción y Desarrollo (BIRF)</li>
    <li>Asociación Internacional de Fomento (AIF)</li>
    <li>Corporación Financiera Internacional (IFC)</li>
    <li>Organismo Multilateral de Garantía de Inversiones (MIGA)</li>
    <li>Centro Internacional de Arreglo de Diferencias Relativas a Inversiones (CIADI)</li>
  </ul>

  Los datos utilizados corresponden a los indicadores de desarrollo de Colombia. La descarga se obtuvo en tablas de formato CSV, que con la ayuda de Python se convirtieron en tablas de una base de datos SQLite creada en memoria Ram durante el proceso de visualización.
              
  La información suministrada se compone en términos generales de 1496 indicadores anuales de desarrollo del país, entre los años 1960 y 2023. Para los análisis se consideraron solamente algunos de ellos. De acuerdo a lo indicado en el sitio web del grupo los datos son de acceso libre y gratuito.

  Los datos fueron descargados de: https://datos.bancomundial.org/pais/colombia

  En la manipulación de la información se utilizó SQL para crear consultas y Python como lenguaje de programación. Adicionalmente se utilizó la librería Streamlit para la visualización web de los resultados.

  Streamlit permite crear y compartir aplicaciones web interactivas de ciencia de datos y aprendizaje automático. Adicionalmente, cuenta con una plataforma <strong>Community Cloud</strong> para implementar, administrar y compartir aplicaciones.         
  ''', unsafe_allow_html=True) 

  # Bibliografía
  st.html('<br>')
  st.subheader('Bibliografía')
  st.write(''' 
  Colombia. (2024). *Indicadores de Desarrollo Mundial*. Grupo Banco Mundial. https://datos.bancomundial.org/pais/colombia         

  Kade. (2024, 10 de diciembre). *E-commerce data analysis using SQL and Python*. [Notebook]. Kaggle. https://www.kaggle.com/code/khafre/e-commerce-data-analysis-using-sql-and-python/notebook

  Terenci Claramunt. (2024, 9 de abril). *SQL Challenge: E-commerce data analysis*. [Notebook]. Kaggle. https://www.kaggle.com/code/terencicp/sql-challenge-e-commerce-data-analysis  
           
  Streamlit. (s.f.). *A faster way to build and share data apps*. Streamlit. https://streamlit.io/
           
  Streamlit documentation. (s.f.). *Documentation*. Streamlit. https://docs.streamlit.io/    
           
  Community Cloud. (s.f.). *Deploy, manage, and share your apps with the world, directly from Streamlit*. Streamlit. https://streamlit.io/cloud  

  Pixabay. (2016). *Yoga 1805784*. [Imagen]. Pixabay. https://cdn.pixabay.com/photo/2016/11/07/13/04/yoga-1805784_1280.png
  ''')