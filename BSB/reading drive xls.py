import pandas as pd
import requests
import io

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

    required_data = dataframe.iloc[2:14, 1:7]

    # Mostrar los datos seleccionados
    print(required_data)
else:
    print("No se pudo descargar el archivo. Verifica la URL y los permisos.")
