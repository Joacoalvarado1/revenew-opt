import pandas as pd
from optimization_app.dataloader import DataLoader
from optimization_app.optimization import OptimizationModel
from tkinter import Tk, filedialog

def main():
    try:
        # Pedir al usuario seleccionar el archivo CSV
        Tk().withdraw()
        file_path = filedialog.askopenfilename(
            title="Selecciona el archivo CSV",
            filetypes=[("CSV files", "*.csv")]
        )

        if not file_path:
            print("⚠️ No se seleccionó ningún archivo.")
            return

        print(f"📂 Archivo seleccionado: {file_path}")

        with open(file_path, 'rb') as f:
            loader = DataLoader(f)
            df = loader.load_and_validate()

        print("✅ CSV cargado correctamente.")
        
        # Revisar si están las columnas necesarias
        required_cols = ['Machine_1_Available_Hours', 'Machine_2_Available_Hours']
        for col in required_cols:
            if col not in df.columns:
                print(f"❌ Faltan columnas necesarias en el archivo CSV: {col}")
                return

        capacidad_a = df.loc[0, 'Machine_1_Available_Hours']
        capacidad_b = df.loc[0, 'Machine_2_Available_Hours']

        model = OptimizationModel(df, capacidad_a, capacidad_b)
        solution, total_income = model.solve()

        print("\n🔧 Resultados de optimización:")
        for producto, cantidad in solution.items():
            print(f"  - {producto}: {cantidad} unidades")

        print(f"\n💰 Ingreso total óptimo: {total_income}")

    except Exception as e:
        print(f"❌ Error durante la ejecución: {e}")

if __name__ == "__main__":
    main()
