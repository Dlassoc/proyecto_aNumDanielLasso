import tkinter as tk
import sympy as sp
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from funciones import *  # Asegúrate de que tienes el archivo funciones.py con las funciones necesarias
from math import exp

# Configuración de la ventana principal
root = tk.Tk()
root.geometry('1000x800')
root.title('Análisis Numérico')

# Frame principal donde se cargan las diferentes páginas
main_frame = tk.Frame(root)
main_frame.pack(expand=True, fill=tk.BOTH)

def home_page():
    for widget in main_frame.winfo_children():
        widget.destroy()
    
    home_frame = tk.Frame(main_frame, bg="light cyan")
    home_frame.pack(expand=True, fill=tk.BOTH, pady=20)
    
    lb = tk.Label(home_frame, text='Bienvenid@', font=('Great Vibes', 38), bg='Light cyan', fg='red')
    lb.pack(pady=80)
    
    msg = '''
    En esta calculadora, podrás resolver ecuaciones de los siguientes tipos:
    - Series de Taylor
    - Ceros de funciones
    - Interpolación
    - Ecuaciones diferenciales
    '''
    lb1 = tk.Label(home_frame, text=msg, font=('Dancing Script', 14), bg='Light cyan')
    lb1.pack(pady=10)

# Función para insertar operadores predefinidos en los campos de entrada
def insertar_operador(entry_widget, operador):
    funciones = {'e': 'exp()', 'sin': 'sin()', 'cos': 'cos()'}
    contenido_actual = entry_widget.get()
    nuevo_contenido = contenido_actual + funciones.get(operador, '')
    entry_widget.delete(0, tk.END)
    entry_widget.insert(tk.END, nuevo_contenido)

# Función para calcular la serie de Taylor
def obtener_datos_taylor():
    try:
        f = entry_funcion.get()
        f = sp.sympify(f)
        punto = float(entry_point.get())
        grado = int(entry_grade.get())
        poli = taylor(f, punto, grado)
        entry_solution_taylor.delete(0, tk.END)
        entry_solution_taylor.insert(tk.END, poli)
    except Exception as e:
        tk.messagebox.showerror("Error", f"Error al calcular Taylor: {e}")

# Página del método de Taylor
def taylor_page():
    for widget in main_frame.winfo_children():
        widget.destroy()

    global entry_funcion, entry_point, entry_grade, entry_solution_taylor
    
    taylor_frame = tk.Frame(main_frame, bg="light cyan")
    taylor_frame.pack(expand=True, fill=tk.BOTH, pady=20)
    
    lb = tk.Label(taylor_frame, text='Método de Taylor', font=('Bold', 40), bg='Light cyan')
    lb.pack(pady=10)
    
    lb1 = tk.Label(taylor_frame, text='Aproximación de un polinomio de Taylor.', font=('Arial', 12), bg='Light cyan')
    lb1.pack(pady=10)

    entry_funcion_frame = tk.Frame(taylor_frame, bg="light cyan")
    lb_insert_funcion = tk.Label(entry_funcion_frame, text='Inserte la función:', font=('Arial', 12), bg='light cyan')
    lb_insert_funcion.pack(side=tk.LEFT, padx=5)
    entry_funcion = tk.Entry(entry_funcion_frame, font=('Arial', 12), width=60)
    entry_funcion.pack(side=tk.LEFT)
    entry_funcion_frame.pack(pady=5)

    # Botones para funciones comunes
    buttons_frame = tk.Frame(taylor_frame, bg="light cyan")
    exp_btn = tk.Button(buttons_frame, text="e", font=('Bold', 12), fg='blue4', bd=5, bg='#c3c3c3', command=lambda: insertar_operador(entry_funcion, 'e'))
    exp_btn.pack(side=tk.LEFT, padx=5)
    sin_btn = tk.Button(buttons_frame, text="Sin", font=('Bold', 12), fg='blue4', bd=5, bg='#c3c3c3', command=lambda: insertar_operador(entry_funcion, 'sin'))
    sin_btn.pack(side=tk.LEFT, padx=5)
    cos_btn = tk.Button(buttons_frame, text="Cos", font=('Bold', 12), fg='blue4', bd=5, bg='#c3c3c3', command=lambda: insertar_operador(entry_funcion, 'cos'))
    cos_btn.pack(side=tk.LEFT, padx=5)
    buttons_frame.pack(pady=5)

    entry_grade_frame = tk.Frame(taylor_frame, bg="light cyan")
    lb_insert_grade = tk.Label(entry_grade_frame, text='Inserte el grado:', font=('Arial', 12), bg='light cyan')
    lb_insert_grade.pack(side=tk.LEFT, padx=5)
    entry_grade = tk.Entry(entry_grade_frame, font=('Arial', 12), width=30)
    entry_grade.pack(side=tk.LEFT)
    entry_grade_frame.pack(pady=5)

    entry_point_frame = tk.Frame(taylor_frame, bg="light cyan")
    lb_insert_point = tk.Label(entry_point_frame, text='Inserte el punto:', font=('Arial', 12), bg='light cyan')
    lb_insert_point.pack(side=tk.LEFT, padx=5)
    entry_point = tk.Entry(entry_point_frame, font=('Arial', 12), width=30)
    entry_point.pack(side=tk.LEFT)
    entry_point_frame.pack(pady=5)

    execute_btn = tk.Button(taylor_frame, text="Ejecutar", font=('Bold', 15), fg='red', bd=5, bg='#c3c3c3', command=obtener_datos_taylor)
    execute_btn.pack(pady=10)

    solution_taylor_frame = tk.Frame(taylor_frame, bg="light cyan")
    lb_solution = tk.Label(solution_taylor_frame, text='Solución', font=('Bold', 30), bg='Light cyan', fg='red')
    lb_solution.pack()
    lb_enunciado_solution = tk.Label(solution_taylor_frame, text='El polinomio aproximado a la función dada es:', font=('Arial', 12), bg='Light cyan')
    lb_enunciado_solution.pack(pady=10)
    entry_solution_frame = tk.Frame(solution_taylor_frame, bg="light cyan")
    entry_solution_taylor = tk.Entry(entry_solution_frame, font=('Arial', 12), width=60)
    entry_solution_taylor.pack(side=tk.LEFT)
    entry_solution_frame.pack(pady=5)
    solution_taylor_frame.pack(pady=20)

    # Botón para ver la gráfica
    grafica_btn = tk.Button(solution_taylor_frame, text="Ver gráfica", font=('Bold', 15), fg='red', bd=5, bg='#c3c3c3', command=lambda: grafica_taylor_page(entry_solution_taylor.get()))
    grafica_btn.pack(pady=10)

# Función para mostrar la gráfica del polinomio de Taylor
def grafica_taylor_page(funcion):
    try:
        for widget in main_frame.winfo_children():
            widget.destroy()
        
        grafica_taylor_frame = tk.Frame(main_frame, bg="light cyan")
        grafica_taylor_frame.pack(expand=True, fill=tk.BOTH, pady=20)

        lb = tk.Label(grafica_taylor_frame, text='Gráfica', font=('Bold', 40), bg='Light cyan')
        lb.pack(pady=10)

        # Crear una figura de Matplotlib
        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)

        # Convertir la función simbólica a una función lambda
        x = sp.Symbol('x')
        taylor_func = sp.lambdify(x, sp.sympify(funcion), "numpy")
        x_vals = np.linspace(-10, 10, 400)
        y_vals = taylor_func(x_vals)

        # Graficar la función
        ax.plot(x_vals, y_vals, label='Polinomio de Taylor', color='blue')

        ax.legend()
        ax.grid(True, linestyle='--', alpha=0.7)

        # Crear un lienzo de Matplotlib para Tkinter
        canvas = FigureCanvasTkAgg(fig, master=grafica_taylor_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    except Exception as e:
        tk.messagebox.showerror("Error", f"Error al graficar: {e}")

# Función para obtener datos para el cálculo de ceros de funciones
def obtener_datos_ceros(metodo):
    try:
        y = entry_funcion_ceros.get()
        y = sp.sympify(y)
        punto_x0 = float(entry_x0.get())
        punto_x1 = float(entry_x1.get())
        tol = float(entry_tol.get())
        f = lambda x: eval(str(y))
        raiz = metodo(f, punto_x0, punto_x1, tol)
        entry_solution_ceros.delete(0, tk.END)
        entry_solution_ceros.insert(tk.END, raiz)
    except Exception as e:
        tk.messagebox.showerror("Error", f"Error en el cálculo de ceros: {e}")

# Página para encontrar ceros de funciones
def ceros_page():
    for widget in main_frame.winfo_children():
        widget.destroy()

    global entry_funcion_ceros, entry_x0, entry_x1, entry_tol, entry_solution_ceros
    
    ceros_frame = tk.Frame(main_frame, bg="light cyan")
    ceros_frame.pack(expand=True, fill=tk.BOTH, pady=20)
    
    lb = tk.Label(ceros_frame, text='Ceros de Funciones', font=('Bold', 40), bg='Light cyan')
    lb.pack(pady=10)
    
    lb1 = tk.Label(ceros_frame, text='Búsqueda de ceros de funciones utilizando diferentes métodos numéricos.', font=('Arial', 12), bg='Light cyan')
    lb1.pack(pady=10)
    
    entry_funcion_ceros_frame = tk.Frame(ceros_frame, bg="light cyan")
    lb_insert_funcion = tk.Label(entry_funcion_ceros_frame, text='Inserte la función:', font=('Arial', 12), bg='light cyan')
    lb_insert_funcion.pack(side=tk.LEFT, padx=5)
    entry_funcion_ceros = tk.Entry(entry_funcion_ceros_frame, font=('Arial', 12), width=60)
    entry_funcion_ceros.pack(side=tk.LEFT)
    entry_funcion_ceros_frame.pack(pady=5)

    entry_x0_frame = tk.Frame(ceros_frame, bg="light cyan")
    lb_insert_x0 = tk.Label(entry_x0_frame, text='Inserte el valor de x0:', font=('Arial', 12), bg='light cyan')
    lb_insert_x0.pack(side=tk.LEFT, padx=5)
    entry_x0 = tk.Entry(entry_x0_frame, font=('Arial', 12), width=30)
    entry_x0.pack(side=tk.LEFT)
    entry_x0_frame.pack(pady=5)

    entry_x1_frame = tk.Frame(ceros_frame, bg="light cyan")
    lb_insert_x1 = tk.Label(entry_x1_frame, text='Inserte el valor de x1:', font=('Arial', 12), bg='light cyan')
    lb_insert_x1.pack(side=tk.LEFT, padx=5)
    entry_x1 = tk.Entry(entry_x1_frame, font=('Arial', 12), width=30)
    entry_x1.pack(side=tk.LEFT)
    entry_x1_frame.pack(pady=5)

    entry_tol_frame = tk.Frame(ceros_frame, bg="light cyan")
    lb_insert_tol = tk.Label(entry_tol_frame, text='Inserte la tolerancia:', font=('Arial', 12), bg='light cyan')
    lb_insert_tol.pack(side=tk.LEFT, padx=5)
    entry_tol = tk.Entry(entry_tol_frame, font=('Arial', 12), width=30)
    entry_tol.pack(side=tk.LEFT)
    entry_tol_frame.pack(pady=5)

    methods_frame = tk.Frame(ceros_frame, bg="light cyan")
    bis_btn = tk.Button(methods_frame, text="Bisección", font=('Bold', 12), fg='blue4', bd=5, bg='#c3c3c3', command=lambda: obtener_datos_ceros(Biseccion))
    bis_btn.pack(side=tk.LEFT, padx=5)
    falsa_btn = tk.Button(methods_frame, text="Posición Falsa", font=('Bold', 12), fg='blue4', bd=5, bg='#c3c3c3', command=lambda: obtener_datos_ceros(Pos_falsa))
    falsa_btn.pack(side=tk.LEFT, padx=5)
    newton_btn = tk.Button(methods_frame, text="Newton", font=('Bold', 12), fg='blue4', bd=5, bg='#c3c3c3', command=lambda: obtener_datos_ceros(Newton))
    newton_btn.pack(side=tk.LEFT, padx=5)
    sec_btn = tk.Button(methods_frame, text="Secante", font=('Bold', 12), fg='blue4', bd=5, bg='#c3c3c3', command=lambda: obtener_datos_ceros(Secante))
    sec_btn.pack(side=tk.LEFT, padx=5)
    methods_frame.pack(pady=10)

    solution_ceros_frame = tk.Frame(ceros_frame, bg="light cyan")
    lb_solution = tk.Label(solution_ceros_frame, text='Solución', font=('Bold', 30), bg='Light cyan', fg='red')
    lb_solution.pack()
    lb_enunciado_solution = tk.Label(solution_ceros_frame, text='La raíz aproximada de la función dada es:', font=('Arial', 12), bg='Light cyan')
    lb_enunciado_solution.pack(pady=10)
    entry_solution_frame = tk.Frame(solution_ceros_frame, bg='light cyan')
    entry_solution_ceros = tk.Entry(entry_solution_frame, font=('Arial', 12), width=60)
    entry_solution_ceros.pack(side=tk.LEFT)
    entry_solution_frame.pack(pady=5)
    solution_ceros_frame.pack(pady=20)

# Función para obtener datos para interpolación
def obtener_datos_interpolacion(metodo):
    try:
        x_values = list(map(float, entry_x_values.get().split(',')))
        y_values = list(map(float, entry_y_values.get().split(',')))
        valor_a_interpolar = float(entry_valor_interpolar.get())

        if metodo == mc:
            resultado, a0, a1 = metodo(x_values, y_values, valor_a_interpolar)
            entry_solution_interpolacion.delete(0, tk.END)
            entry_solution_interpolacion.insert(tk.END, resultado)
            entry_ecuacion_minimos_cuadrados.delete(0, tk.END)
            entry_ecuacion_minimos_cuadrados.insert(tk.END, f"y = {a0:.4f} + {a1:.4f} * x")
        else:
            resultado = metodo(x_values, y_values, valor_a_interpolar)
            entry_solution_interpolacion.delete(0, tk.END)
            entry_solution_interpolacion.insert(tk.END, resultado)
            entry_ecuacion_minimos_cuadrados.delete(0, tk.END)  # Limpiar la entrada de la ecuación para otros métodos

        # Mostrar el frame de soluciones después del cálculo exitoso
        solution_interpolacion_frame.pack(pady=20)

    except Exception as e:
        tk.messagebox.showerror("Error", f"Error en el cálculo de interpolación: {e}")




# Página de interpolación
def interpolacion_page():
    for widget in main_frame.winfo_children():
        widget.destroy()

    global entry_x_values, entry_y_values, entry_valor_interpolar, entry_solution_interpolacion, entry_ecuacion_minimos_cuadrados, solution_interpolacion_frame
    
    interpolacion_frame = tk.Frame(main_frame, bg="light cyan")
    interpolacion_frame.pack(expand=True, fill=tk.BOTH, pady=20)
    
    lb = tk.Label(interpolacion_frame, text='Interpolación', font=('Bold', 40), bg='Light cyan')
    lb.pack(pady=10)
    
    lb1 = tk.Label(interpolacion_frame, text='Interpolación de datos utilizando diferentes métodos numéricos.', font=('Arial', 12), bg='Light cyan')
    lb1.pack(pady=10)
    
    entry_x_values_frame = tk.Frame(interpolacion_frame, bg="light cyan")
    lb_insert_x_values = tk.Label(entry_x_values_frame, text='Inserte los valores de X (separados por comas):', font=('Arial', 12), bg='light cyan')
    lb_insert_x_values.pack(side=tk.LEFT, padx=5)
    entry_x_values = tk.Entry(entry_x_values_frame, font=('Arial', 12), width=60)
    entry_x_values.pack(side=tk.LEFT)
    entry_x_values_frame.pack(pady=5)

    entry_y_values_frame = tk.Frame(interpolacion_frame, bg="light cyan")
    lb_insert_y_values = tk.Label(entry_y_values_frame, text='Inserte los valores de Y (separados por comas):', font=('Arial', 12), bg='light cyan')
    lb_insert_y_values.pack(side=tk.LEFT, padx=5)
    entry_y_values = tk.Entry(entry_y_values_frame, font=('Arial', 12), width=60)
    entry_y_values.pack(side=tk.LEFT)
    entry_y_values_frame.pack(pady=5)

    entry_valor_interpolar_frame = tk.Frame(interpolacion_frame, bg="light cyan")
    lb_insert_valor_interpolar = tk.Label(entry_valor_interpolar_frame, text='Inserte el valor a interpolar:', font=('Arial', 12), bg='light cyan')
    lb_insert_valor_interpolar.pack(side=tk.LEFT, padx=5)
    entry_valor_interpolar = tk.Entry(entry_valor_interpolar_frame, font=('Arial', 12), width=30)
    entry_valor_interpolar.pack(side=tk.LEFT)
    entry_valor_interpolar_frame.pack(pady=5)

    methods_frame = tk.Frame(interpolacion_frame, bg="light cyan")
    pols_btn = tk.Button(methods_frame, text="Pol Simple", font=('Bold', 12), fg='blue4', bd=5, bg='#c3c3c3', command=lambda: obtener_datos_interpolacion(p_simple))
    pols_btn.pack(side=tk.LEFT, padx=5)
    lagrange_btn = tk.Button(methods_frame, text="Lagrange", font=('Bold', 12), fg='blue4', bd=5, bg='#c3c3c3', command=lambda: obtener_datos_interpolacion(lagrange))
    lagrange_btn.pack(side=tk.LEFT, padx=5)
    min_cuadrados_btn = tk.Button(methods_frame, text="Mínimos Cuadrados", font=('Bold', 12), fg='blue4', bd=5, bg='#c3c3c3', command=lambda: obtener_datos_interpolacion(mc))
    min_cuadrados_btn.pack(side=tk.LEFT, padx=5)
    methods_frame.pack(pady=10)

    # Crear la sección de soluciones pero no mostrarla inicialmente
    solution_interpolacion_frame = tk.Frame(interpolacion_frame, bg="light cyan")
    lb_solution = tk.Label(solution_interpolacion_frame, text='Solución', font=('Bold', 30), bg='Light cyan', fg='red')
    lb_solution.pack()
    lb_enunciado_solution = tk.Label(solution_interpolacion_frame, text='El valor interpolado es:', font=('Arial', 12), bg='Light cyan')
    lb_enunciado_solution.pack(pady=10)
    entry_solution_frame = tk.Frame(solution_interpolacion_frame, bg='light cyan')
    entry_solution_interpolacion = tk.Entry(entry_solution_frame, font=('Arial', 12), width=60)
    entry_solution_interpolacion.pack(side=tk.LEFT)
    entry_solution_frame.pack(pady=5)
    
    lb_ecuacion_minimos_cuadrados = tk.Label(solution_interpolacion_frame, text='Ecuación de la recta de mejor ajuste (si aplica):', font=('Arial', 12), bg='Light cyan')
    lb_ecuacion_minimos_cuadrados.pack(pady=10)
    entry_ecuacion_frame = tk.Frame(solution_interpolacion_frame, bg='light cyan')
    entry_ecuacion_minimos_cuadrados = tk.Entry(entry_ecuacion_frame, font=('Arial', 12), width=60)
    entry_ecuacion_minimos_cuadrados.pack(side=tk.LEFT)
    entry_ecuacion_frame.pack(pady=5)

    # Inicialmente no mostrar el frame de soluciones
    solution_interpolacion_frame.pack_forget()




def ver_grafica_minimos_cuadrados():
    try:
        # Obtener los valores de entrada
        x_values = list(map(float, entry_x_values.get().split(',')))
        y_values = list(map(float, entry_y_values.get().split(',')))

        # Verificar que los coeficientes a0 y a1 están disponibles
        if not entry_ecuacion_minimos_cuadrados.get():
            tk.messagebox.showerror("Error", "No hay coeficientes disponibles para la gráfica. Asegúrese de calcular primero la interpolación de mínimos cuadrados.")
            return

        # Extraer a0 y a1 de la ecuación mostrada en la interfaz
        a0, a1 = map(float, entry_ecuacion_minimos_cuadrados.get().replace("y = ", "").replace(" * x", "").split(" + "))
        
        # Crear los puntos para la recta de mejor ajuste
        x_line = np.linspace(min(x_values), max(x_values), 100)
        y_line = a0 + a1 * x_line

        # Crear la gráfica
        plt.figure(figsize=(10, 6))
        plt.plot(x_values, y_values, 'bo', label='Datos Originales')
        plt.plot(x_line, y_line, 'r-', label=f'Recta de Mejor Ajuste: y = {a0:.4f} + {a1:.4f}x')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Método de Mínimos Cuadrados')
        plt.legend()
        plt.grid(True)
        plt.show()

    except Exception as e:
        tk.messagebox.showerror("Error", f"Error al mostrar la gráfica: {e}")


# Función para obtener datos para resolver ecuaciones diferenciales
def obtener_datos_ecuaciones_diferenciales(metodo):
    try:
        y = entry_funcion_diferencial.get()
        y = sp.sympify(y)
        punto_x0 = float(entry_x0_dif.get())
        punto_y0 = float(entry_y0_dif.get())
        h = float(entry_h.get())
        n = int(entry_n.get())
        f = lambda x, y: eval(str(y))
        x_vals, y_vals = metodo(f, punto_x0, punto_y0, h, n)
        entry_solution_ecuaciones_diferenciales.delete(0, tk.END)
        entry_solution_ecuaciones_diferenciales.insert(tk.END, f"X: {x_vals}, Y: {y_vals}")
    except Exception as e:
        tk.messagebox.showerror("Error", f"Error en el cálculo de ecuaciones diferenciales: {e}")

# Página de ecuaciones diferenciales
def ecuaciones_diferenciales_page():
    for widget in main_frame.winfo_children():
        widget.destroy()

    global entry_funcion_diferencial, entry_x0_dif, entry_y0_dif, entry_h, entry_n, entry_solution_ecuaciones_diferenciales
    
    ecuaciones_diferenciales_frame = tk.Frame(main_frame, bg="light cyan")
    ecuaciones_diferenciales_frame.pack(expand=True, fill=tk.BOTH, pady=20)
    
    lb = tk.Label(ecuaciones_diferenciales_frame, text='Ecuaciones Diferenciales', font=('Bold', 40), bg='Light cyan')
    lb.pack(pady=10)
    
    lb1 = tk.Label(ecuaciones_diferenciales_frame, text='Resolución de ecuaciones diferenciales utilizando diferentes métodos numéricos.', font=('Arial', 12), bg='Light cyan')
    lb1.pack(pady=10)
    
    entry_funcion_diferencial_frame = tk.Frame(ecuaciones_diferenciales_frame, bg="light cyan")
    lb_insert_funcion = tk.Label(entry_funcion_diferencial_frame, text='Inserte la ecuación diferencial:', font=('Arial', 12), bg='light cyan')
    lb_insert_funcion.pack(side=tk.LEFT, padx=5)
    entry_funcion_diferencial = tk.Entry(entry_funcion_diferencial_frame, font=('Arial', 12), width=60)
    entry_funcion_diferencial.pack(side=tk.LEFT)
    entry_funcion_diferencial_frame.pack(pady=5)

    entry_x0_frame_dif = tk.Frame(ecuaciones_diferenciales_frame, bg="light cyan")
    lb_insert_x0 = tk.Label(entry_x0_frame_dif, text='Inserte el valor de x0:', font=('Arial', 12), bg='light cyan')
    lb_insert_x0.pack(side=tk.LEFT, padx=5)
    entry_x0_dif = tk.Entry(entry_x0_frame_dif, font=('Arial', 12), width=30)
    entry_x0_dif.pack(side=tk.LEFT)
    entry_x0_frame_dif.pack(pady=5)

    entry_y0_frame_dif = tk.Frame(ecuaciones_diferenciales_frame, bg="light cyan")
    lb_insert_y0 = tk.Label(entry_y0_frame_dif, text='Inserte el valor de y0:', font=('Arial', 12), bg='light cyan')
    lb_insert_y0.pack(side=tk.LEFT, padx=5)
    entry_y0_dif = tk.Entry(entry_y0_frame_dif, font=('Arial', 12), width=30)
    entry_y0_dif.pack(side=tk.LEFT)
    entry_y0_frame_dif.pack(pady=5)

    entry_h_frame = tk.Frame(ecuaciones_diferenciales_frame, bg="light cyan")
    lb_insert_h = tk.Label(entry_h_frame, text='Inserte el valor de h (paso):', font=('Arial', 12), bg='light cyan')
    lb_insert_h.pack(side=tk.LEFT, padx=5)
    entry_h = tk.Entry(entry_h_frame, font=('Arial', 12), width=30)
    entry_h.pack(side=tk.LEFT)
    entry_h_frame.pack(pady=5)

    entry_n_frame = tk.Frame(ecuaciones_diferenciales_frame, bg="light cyan")
    lb_insert_n = tk.Label(entry_n_frame, text='Inserte el número de pasos:', font=('Arial', 12), bg='light cyan')
    lb_insert_n.pack(side=tk.LEFT, padx=5)
    entry_n = tk.Entry(entry_n_frame, font=('Arial', 12), width=30)
    entry_n.pack(side=tk.LEFT)
    entry_n_frame.pack(pady=5)

    methods_frame = tk.Frame(ecuaciones_diferenciales_frame, bg="light cyan")
    euler_btn = tk.Button(methods_frame, text="Euler", font=('Bold', 12), fg='blue4', bd=5, bg='#c3c3c3', command=lambda: obtener_datos_ecuaciones_diferenciales(Euler))
    euler_btn.pack(side=tk.LEFT, padx=5)
    rk4_btn = tk.Button(methods_frame, text="Runge-Kutta 4", font=('Bold', 12), fg='blue4', bd=5, bg='#c3c3c3', command=lambda: obtener_datos_ecuaciones_diferenciales(Runge4))
    rk4_btn.pack(side=tk.LEFT, padx=5)
    methods_frame.pack(pady=10)

    solution_ecuaciones_diferenciales_frame = tk.Frame(ecuaciones_diferenciales_frame, bg="light cyan")
    lb_solution = tk.Label(solution_ecuaciones_diferenciales_frame, text='Solución', font=('Bold', 30), bg='Light cyan', fg='red')
    lb_solution.pack()
    lb_enunciado_solution = tk.Label(solution_ecuaciones_diferenciales_frame, text='Los valores de la solución son:', font=('Arial', 12), bg='Light cyan')
    lb_enunciado_solution.pack(pady=10)
    entry_solution_frame = tk.Frame(solution_ecuaciones_diferenciales_frame, bg='light cyan')
    entry_solution_ecuaciones_diferenciales = tk.Entry(entry_solution_frame, font=('Arial', 12), width=60)
    entry_solution_ecuaciones_diferenciales.pack(side=tk.LEFT)
    entry_solution_frame.pack(pady=5)
    solution_ecuaciones_diferenciales_frame.pack(pady=20)

# Menú de navegación
menu = tk.Menu(root)
root.config(menu=menu)

# Opción de menú para la página principal
home_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label='Inicio', menu=home_menu)
home_menu.add_command(label='Inicio', command=home_page)

# Opción de menú para la página de Taylor
taylor_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label='Taylor', menu=taylor_menu)
taylor_menu.add_command(label='Taylor', command=taylor_page)

# Opción de menú para la página de Ceros de Funciones
ceros_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label='Ceros de Funciones', menu=ceros_menu)
ceros_menu.add_command(label='Ceros de Funciones', command=ceros_page)

# Opción de menú para la página de Interpolación
interpolacion_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label='Interpolación', menu=interpolacion_menu)
interpolacion_menu.add_command(label='Interpolación', command=interpolacion_page)

# Opción de menú para la página de Ecuaciones Diferenciales
ecuaciones_diferenciales_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label='Ecuaciones Diferenciales', menu=ecuaciones_diferenciales_menu)
ecuaciones_diferenciales_menu.add_command(label='Ecuaciones Diferenciales', command=ecuaciones_diferenciales_page)

# Cargar la página principal al inicio
home_page()

# Iniciar el bucle principal de la interfaz
root.mainloop()
