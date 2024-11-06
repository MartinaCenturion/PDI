import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

# Configuración del cliente
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5000))

# Función para recibir mensajes
def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            chat_area.config(state=tk.NORMAL)
            chat_area.insert(tk.END, message + "\n")
            chat_area.config(state=tk.DISABLED)
            chat_area.yview(tk.END)
        except:
            print("Error en la conexión.")
            client.close()
            break

# Función para enviar mensajes
def write():
    message = f'{nickname}: {msg_entry.get()}'
    client.send(message.encode('utf-8'))
    msg_entry.delete(0, tk.END)

# Función para cerrar la ventana y la conexión
def on_closing():
    client.close()
    window.quit()

# Función para notificar que se necesita ayuda
def notify_help():
    message = f'{nickname} necesita ayuda.'
    client.send(message.encode('utf-8'))

# Configuración de la ventana principal de Tkinter
window = tk.Tk()
window.title("Chat Local - Tkinter")
window.geometry("400x500")
window.configure(bg="#222222")

# Título
title_label = tk.Label(window, text="Chat Local", bg="#222222", fg="#FFFFFF", font=("Helvetica", 16, "bold"))
title_label.grid(row=0, column=0, padx=10, pady=10)

# Área de mensajes
chat_area = scrolledtext.ScrolledText(window, state='disabled', width=50, height=20, bg="#333333", fg="#FFFFFF", font=("Arial", 10))
chat_area.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

# Entrada de mensaje
msg_entry = tk.Entry(window, width=30, bg="#444444", fg="#FFFFFF", font=("Arial", 10))
msg_entry.grid(row=2, column=0, padx=10, pady=10)

# Botón de enviar
send_button = tk.Button(window, text="Enviar", command=write, width=10, bg="#4CAF50", fg="#FFFFFF", font=("Arial", 10, "bold"))
send_button.grid(row=2, column=1, padx=10, pady=10)

# Botón de notificación de ayuda
help_button = tk.Button(window, text="Pedir ayuda", command=notify_help, width=10, bg="#FF5722", fg="#FFFFFF", font=("Arial", 10, "bold"))
help_button.grid(row=3, column=0, padx=10, pady=10, columnspan=2)

# Evento para cerrar la ventana
window.protocol("WM_DELETE_WINDOW", on_closing)

# Solicitar apodo del usuario
nickname = input("Elige tu apodo: ")
client.send(nickname.encode('utf-8'))

# Hilo para recibir mensajes
receive_thread = threading.Thread(target=receive)
receive_thread.start()

# Iniciar la aplicación
window.mainloop()
