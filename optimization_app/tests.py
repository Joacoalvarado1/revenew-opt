from django.test import TestCase
from .optimization import OptimizationModel
import pandas as pd
import numpy as np

class OptimizationModelTest(TestCase):
    def test_random_data(self):
        np.random.seed(42) 
        data = {
            "Product_A_Production_Time_Machine_1": [round(np.random.uniform(1.0, 3.0), 2)],
            "Product_A_Production_Time_Machine_2": [round(np.random.uniform(1.0, 3.0), 2)],
            "Product_B_Production_Time_Machine_1": [round(np.random.uniform(0.5, 2.0), 2)],
            "Product_B_Production_Time_Machine_2": [round(np.random.uniform(0.5, 2.0), 2)],
            "Machine_1_Available_Hours": [round(np.random.uniform(6.0, 12.0), 2)],
            "Machine_2_Available_Hours": [round(np.random.uniform(6.0, 12.0), 2)],
            "Price_Product_A": [np.random.randint(50, 150)],
            "Price_Product_B": [np.random.randint(30, 120)],
        }
        df = pd.DataFrame(data)
        model = OptimizationModel(df, capacidad_a=float(df["Machine_1_Available_Hours"][0]), capacidad_b=float(df["Machine_2_Available_Hours"][0]))
        solution, total = model.solve()

        print("Datos simulados:")
        print(df)
        print("Resultado:", solution, total)

        self.assertIsInstance(solution, dict)
        self.assertIsInstance(total, (int, float))
        self.assertGreaterEqual(total, 0)
