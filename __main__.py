import pandas as pd
import os

csv_file_input= input("Ingrese la ruta completa del archivo CSV: ")
csv_file_path = csv_file_input.strip("'")
excel_file_path = csv_file_path.replace('.csv', '.xlsx')

if not os.path.isfile(csv_file_path):
    print("El archivo CSV no existe, verifique la ruta.")
    exit(0)

try:
    df = pd.read_csv(csv_file_path, low_memory=False)
    df.to_excel(excel_file_path, index=False)
    print(f"Archivo Excel guardado con éxito en: {excel_file_path}")
except Exception as e:
    print(f"Ocurrió un error al procesar el archivo: {e}")