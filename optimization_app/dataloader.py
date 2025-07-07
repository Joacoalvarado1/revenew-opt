
import pandas as pd

class DataLoader:
    required_columns = [
        'Product_A_Production_Time_Machine_1',
        'Product_A_Production_Time_Machine_2',
        'Product_B_Production_Time_Machine_1',
        'Product_B_Production_Time_Machine_2',
        'Machine_1_Available_Hours',
        'Machine_2_Available_Hours',
        'Price_Product_A',
        'Price_Product_B'
    ]

    def __init__(self, file):
        self.file = file

    def load_and_validate(self):
        df = pd.read_csv(self.file)
        for col in self.required_columns:
            if col not in df.columns:
                raise ValueError(f"Falta la columna requerida: {col}")
        if df.isnull().values.any():
            raise ValueError("El archivo contiene valores vacíos.")
        return df
