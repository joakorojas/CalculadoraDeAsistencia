import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image




def calculate_percentage():
    try:
        subjectName = subject_entry.get()
        modulosAFaltar = int(faltas_entry.get())
        modulosDados = int(modulos_entry.get())
        ausentes = int(ausentes_entry.get())

        if modulosAFaltar < 0 or modulosDados < 0 or ausentes < 0:
            result_label.config(text="Error: Ingresa números mayores o iguales a cero en los campos correspondientes", foreground="red")
            return

        if modulosAFaltar > modulosDados:
            error_message = "Error: La cantidad de módulos a faltar no puede ser mayor a la cantidad de módulos dados después de la falta"
            result_label.config(text=error_message, foreground="red", font=("Arial", 12, "bold"), wraplength=400)
            return

        presentes = modulosDados - ausentes - modulosAFaltar

        resultado = round((presentes / modulosDados) * 100, 2)

        if resultado < 75:
            result_label.config(text=f"Tu porcentaje de asistencia en {subjectName} será de: {resultado}%", foreground="red", font=("Arial", 12, "bold"), wraplength=400)
        else:
            result_label.config(text=f"Tu porcentaje de asistencia en {subjectName} será de: {resultado}%", foreground="green", font=("Arial", 12, "bold"), wraplength=400)
    except ValueError:
        result_label.config(text="Error: Ingresa números enteros en los campos correspondientes", foreground="red", wraplength=400)

def restart():
    subject_entry.delete(0, tk.END)
    faltas_entry.delete(0, tk.END)
    modulos_entry.delete(0, tk.END)
    ausentes_entry.delete(0, tk.END)
    result_label.config(text="", foreground="black")

def close_app():
    window.destroy()

def show_main_window():
    start_frame.pack_forget()
    main_frame.pack()

# Crear la ventana de la aplicación
window = tk.Tk()
window.title("Calculadora de Asistencia")
window.geometry("500x500")
window.resizable(False, False)

# Establecer el estilo para el tema
style = ttk.Style(window)
style.theme_use("clam")

# Crear el marco de inicio
start_frame = ttk.Frame(window)
start_frame.pack(pady=50, fill="both", expand=True)

# Etiqueta de bienvenida
welcome_label = ttk.Label(start_frame, text="Calculadora de Asistencia", font=("Arial", 20))
welcome_label.pack(pady=10)

# Etiqueta de descripción
description_label = ttk.Label(start_frame, text="Este programa te ayudará a calcular tu porcentaje de asistencias a una materia.\nPor favor utilícelo a consciencia y teniendo en cuenta que el prototipo puede contener errores.\nSi encuentra algún error, comuníquese con el desarrollador.", font=("Arial", 10), wraplength=400, justify="center")
description_label.pack(pady=10)

# Footer en el marco de inicio
start_footer_label = ttk.Label(start_frame, text="© Powered by: Joaquin Rojas 3517466759 v1.0", font=("Arial", 8, "bold"))
start_footer_label.pack(side="bottom")

# Botón para iniciar
start_button = ttk.Button(start_frame, text="Iniciar", command=show_main_window)
start_button.pack(pady=10)

# Ruta de la imagen
image_path = "img6.png"

# Cargar la imagen
image = Image.open(image_path)

# Ajustar el tamaño de la imagen si es necesario
image = image.resize((150, 130))

# Crear un objeto PhotoImage
photo = ImageTk.PhotoImage(image)

# Crear una etiqueta para mostrar la imagen
image_label = ttk.Label(start_frame, image=photo)
image_label.pack(pady=10)

# Crear el marco principal
main_frame = ttk.Frame(window)

# Establecer las dimensiones de la pantalla de cálculos
main_frame_width = 00
main_frame_height = 600
main_frame.place(width=main_frame_width, height=main_frame_height, relx=0.5, rely=0.5, anchor="center")

# Ajustar la forma en que se expande el marco principal
main_frame.pack(fill="both", expand=True)

# Etiqueta de título en el marco principal
main_title_label = ttk.Label(main_frame, text="Calculadora de Asistencia", font=("Arial", 20))
main_title_label.pack(pady=10)

# Crear un contenedor para los campos de entrada
input_frame = ttk.Frame(main_frame)
input_frame.pack(pady=20)

# Etiqueta y entrada para el nombre de la materia
subject_label = ttk.Label(input_frame, text="Nombre de la materia:")
subject_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
subject_entry = ttk.Entry(input_frame)
subject_entry.grid(row=0, column=1, padx=5, pady=5)

# Etiqueta y entrada para la cantidad de módulos a faltar
faltas_label = ttk.Label(input_frame, text="¿A cuántos módulos quieres faltar?")
faltas_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
faltas_entry = ttk.Entry(input_frame)
faltas_entry.grid(row=1, column=1, padx=5, pady=5)

# Etiqueta y entrada para la cantidad de módulos dados
modulos_label = ttk.Label(input_frame, text="¿Cuántos módulos se habrán dado después de la falta?")
modulos_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
modulos_entry = ttk.Entry(input_frame)
modulos_entry.grid(row=2, column=1, padx=5, pady=5)

# Etiqueta y entrada para la cantidad de ausentes
ausentes_label = ttk.Label(input_frame, text="¿Cuántos ausentes tienes en esta materia?")
ausentes_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
ausentes_entry = ttk.Entry(input_frame)
ausentes_entry.grid(row=3, column=1, padx=5, pady=5)

# Crear el contenedor para los botones
button_container = ttk.Frame(main_frame)
button_container.pack(pady=10)

# Botón para calcular el porcentaje de asistencia
calculate_button = ttk.Button(button_container, text="Calcular", command=calculate_percentage)
calculate_button.pack(side="left", padx=5)

# Botón para reiniciar los campos y los resultados
restart_button = ttk.Button(button_container, text="Reiniciar", command=restart, style="Restart.TButton")
restart_button.pack(side="left", padx=5)

# Cambiar el estilo del botón Cerrar
style.configure("Close.TButton", font=("Arial", 12, "bold"))
style.configure("Close.TButton", foreground="white", background="#FF0000")
style.map("Close.TButton",
          foreground=[("pressed", "white"), ("active", "white")],
          background=[("pressed", "#B30000"), ("active", "#B30000")])

# Botón para cerrar la aplicación
close_button = ttk.Button(button_container, text="Cerrar", command=close_app, style="Close.TButton")
close_button.pack(side="right", padx=5)


# Etiqueta para mostrar el resultado
result_label = ttk.Label(main_frame, text="", foreground="black", font=("Arial", 12))
result_label.pack(pady=10)

# Footer en el marco principal
main_footer_label = ttk.Label(main_frame, text="© Powered by: Joaquin Rojas 3517466759 v1.0", font=("Arial", 8, "bold"))
main_footer_label.pack(side="bottom")

# Cambiar el estilo del botón Calcular
style.configure("TButton", font=("Arial", 12, "bold"))
style.configure("TButton", foreground="white", background="#4CAF50")
style.map("TButton",
          foreground=[("pressed", "white"), ("active", "white")],
          background=[("pressed", "#45A049"), ("active", "#45A049")])

# Cambiar el estilo del botón Reiniciar
style.configure("Restart.TButton", font=("Arial", 12, "bold"))
style.configure("Restart.TButton", foreground="white", background="#FF5722")
style.map("Restart.TButton",
          foreground=[("pressed", "white"), ("active", "white")],
          background=[("pressed", "#E64A19"), ("active", "#E64A19")])

# Ejecutar la aplicación
window.mainloop()
