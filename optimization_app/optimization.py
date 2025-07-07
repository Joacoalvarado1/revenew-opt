class OptimizationModel:
    def __init__(self, df, capacidad_a, capacidad_b):
        self.df = df
        self.capacidad_a = capacidad_a
        self.capacidad_b = capacidad_b

    def solve(self):
        # Datos
        a1 = self.df["Product_A_Production_Time_Machine_1"][0]
        a2 = self.df["Product_A_Production_Time_Machine_2"][0]
        b1 = self.df["Product_B_Production_Time_Machine_1"][0]
        b2 = self.df["Product_B_Production_Time_Machine_2"][0]
        pa = self.df["Price_Product_A"][0]
        pb = self.df["Price_Product_B"][0]

# Fuerza Bruta para probar todas las combinaciones posibles :
        best_total = 0
        best_solution = {}

        for x in range(0, int(self.capacidad_a // a1) + 1):
            for y in range(0, int(self.capacidad_b // b2) + 1):
                if x * a1 + y * b1 <= self.capacidad_a and x * a2 + y * b2 <= self.capacidad_b:
                    total = x * pa + y * pb
                    if total > best_total:
                        best_total = total
                        best_solution = {"Producto A": x, "Producto B": y}

        return best_solution, best_total
