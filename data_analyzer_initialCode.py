import tkinter as tk
from tkinter import filedialog
import pandas as pd
import csv

def create_csv(file_path, data):
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["id", "age", "gender", "score"])
        for row in data:
            writer.writerow(row)

def load_dataset(file_path):
    dataset = pd.read_csv(file_path)
    return dataset

def basic_analysis(dataset):
    summary_statistics = dataset.describe()
    return summary_statistics

def load_csv():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        dataset = load_dataset(file_path)
        summary_statistics = basic_analysis(dataset)
        print("Resumen estadístico del conjunto de datos:")
        print(summary_statistics)

def create_gui():
    root = tk.Tk()
    root.title("Data Analyzer")

    load_button = tk.Button(root, text="Cargar CSV", command=load_csv)
    load_button.pack(pady=20)

    root.mainloop()

def main():
    # Crear datos de ejemplo para el archivo CSV
    data = [
        [1, 25, "M", 78],
        [2, 30, "F", 82],
        [3, 35, "M", 90],
        [4, 28, "F", 75],
        [5, 32, "M", 85]
    ]

    # Ruta del archivo CSV
    file_path = "datos.csv"

    # Crear el archivo CSV
    create_csv(file_path, data)
    print(f"Archivo CSV '{file_path}' creado con éxito.")

    # Crear y mostrar la interfaz gráfica de usuario
    create_gui()

if __name__ == "__main__":
    main()

