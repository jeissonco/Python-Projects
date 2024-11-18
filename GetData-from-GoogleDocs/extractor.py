import pandas as pd
import requests
import io


def get_data_google_docs():

    # URL del archivo con formato para descargar como Excel
    url = "https://docs.google.com/spreadsheets/d/1LGparnpoUY7HFKsmdiGnp-zm725SaTcca4ndM22Vu5U/export?format=xlsx"

    # Descarga el archivo Excel desde la URL
    response = requests.get(url)

    # Verifica que la solicitud haya sido exitosa (código 200 significa éxito)
    if response.status_code == 200:
        # Carga el archivo en memoria
        file_data = io.BytesIO(response.content)



        # read by  sheet of an excel file
        xls_doc = pd.ExcelFile(file_data)
        
        
        dataframe = xls_doc.parse('M -3009')

        # Selección de datos por columna y fila
        required_data = dataframe.iloc[2:14, 1:7]

        #una prueba de datos 
        '''data_test = {
        'destino': ['Lugar A', 'Lugar B', 'Lugar C'],
        'hora': ['10:00 AM', '12:00 PM', '02:00 PM'],
        'descripcion': ['Entrega de paquetes', 'Recolección de documentos', 'Entrega urgente']
        }'''

        #required_data = pd.DataFrame(data_test)
        # Mostrar los datos seleccionados
        print(required_data)
    else:
        print("No se pudo descargar el archivo. Verifica la URL y los permisos.")


    return required_data