# revenew-opt

Este proyecto fue desarrollado como parte de una prueba técnica para la empresa Revenew. Se trata de una aplicación web construida con Django que permite subir un archivo CSV, configurar parámetros de capacidad, ejecutar un modelo de optimización lineal y mostrar los resultados.

## 🎯 Objetivo

Maximizar los ingresos diarios de una empresa manufacturera, decidiendo la cantidad óptima de productos A y B a producir, respetando restricciones de tiempo en dos máquinas.

## ⚙️ Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Joacoalvarado1/revenew-opt.git
   cd revenew-opt
   ```

2. Crea un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv env
   source env/bin/activate  # En Windows: env\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Ejecución

Para levantar la aplicación web localmente:

```bash
python manage.py runserver
```

Luego abre en tu navegador: [http://localhost:8000](http://localhost:8000)

Desde ahí puedes:
- Subir tu archivo CSV (con formato correcto).
- Ingresar las capacidades de las máquinas.
- Ver el resultado óptimo: unidades a producir de A y B, e ingreso total.

## 🧪 `main.py` – Ejecución directa

Si deseas probar la lógica sin levantar el servidor web:

```bash
python main.py
```

Este archivo carga un CSV de ejemplo, ejecuta la optimización e imprime el resultado por consola.

## 📂 Estructura del CSV

El archivo CSV debe contener las siguientes columnas:

- `PA`, `PB`: Precios de los productos A y B.
- `TA1`, `TA2`: Tiempo requerido por unidad de A en máquinas 1 y 2.
- `TB1`, `TB2`: Tiempo requerido por unidad de B en máquinas 1 y 2.
- `TM1`, `TM2`: Tiempo total disponible en las máquinas 1 y 2.

**Ejemplo:**

| PA | PB | TA1 | TA2 | TB1 | TB2 | TM1 | TM2 |
|----|----|-----|-----|-----|-----|-----|-----|
| 50 | 80 | 3   | 2   | 4   | 5   | 26  | 23  |

## 📌 Consideraciones

- La solución utiliza `scipy.optimize.linprog` para resolver el modelo.
- No se utiliza base de datos persistente; todo se ejecuta en memoria.
- La aplicación fue diseñada con separación clara entre backend, lógica de negocio y frontend.

## 📄 Licencia

Este proyecto fue desarrollado exclusivamente con fines evaluativos y educativos.
