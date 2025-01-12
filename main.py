import streamlit as st
import importlib

# Configuración general para todas las páginas
st.set_page_config(
  page_title='Análisis de indicadores',
  page_icon='imagenes/icono.png',
  layout='wide',
  #initial_sidebar_state='collapsed'
)

# Logo de la barra lateral izquierda
st.sidebar.image('imagenes/lotus-flower.png')
st.sidebar.write('')

# Selección de la página a visualizar
pag = st.sidebar.selectbox(
  "Selecciona una página", 
  ("Descripción general", "Inflación Anual", "Producto Interno Bruto")
) 
st.sidebar.divider()

# Presentado por
st.sidebar.markdown(
  '<h3 style="text-align:center">Trabajo presentado por:</h3>', 
  unsafe_allow_html=True
)
st.sidebar.markdown('''
<p style="text-align:center">
  Yury Daniela Pulido Fonseca<br>
  Mónica Espitia Montaña
</p>         
''', unsafe_allow_html=True)
st.sidebar.markdown(
  '<h1 style="text-align:center">Cloud Computing</h1>', 
  unsafe_allow_html=True
)

# Función que carga la página seleccionada
def cargarPagina(pagina): 
  modulo = importlib.import_module(pagina) 
  modulo.mostrar()  

# LLamado a la función de cargar página
if pag == "Descripción general": 
  cargarPagina('page_1')
elif pag == "Inflación Anual": 
  cargarPagina('page_2') 
elif pag == "Producto Interno Bruto": 
  cargarPagina('page_3')

