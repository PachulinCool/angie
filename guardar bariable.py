import tkinter as tk

def mostrar_mensaje():
    nombre = entrada_nombre.get()
    mensaje = f"Hola, soy {nombre}"
    etiqueta_resultado.config(text=mensaje)

# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Saludo Personalizado")

# Crear una etiqueta y un Entry para que el usuario ingrese su nombre
etiqueta_nombre = tk.Label(ventana_principal, text="Ingresa tu nombre:")
etiqueta_nombre.pack(pady=10)

entrada_nombre = tk.Entry(ventana_principal)
entrada_nombre.pack(pady=10)

# Crear un botón que muestra el mensaje personalizado al ser presionado
boton_mostrar_mensaje = tk.Button(ventana_principal, text="Mostrar Mensaje", command=mostrar_mensaje)
boton_mostrar_mensaje.pack(pady=20)

# Crear una etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana_principal, text="")
etiqueta_resultado.pack(pady=10)

# Iniciar el bucle principal de la aplicación
ventana_principal.mainloop()
