Documentación del Proyecto: Chat Local con Notificación de Ayuda

Descripción del Proyecto

El proyecto es una aplicación de chat local diseñada con Python y la biblioteca Tkinter para la interfaz gráfica.
Los usuarios pueden conectarse a un servidor en una red local, enviar mensajes entre ellos y usar un botón especial para enviar una notificación de "Ayuda" a todos los participantes del chat.

Características Principales

Chat en tiempo real: Los mensajes enviados se transmiten a todos los usuarios conectados al servidor.

Notificación de ayuda: Un botón permite a los usuarios enviar un mensaje especial indicando que necesitan ayuda.

Interfaz: Diseñada con Tkinter, incluye un área de mensajes desplazable, entrada de texto y botones de acción.

Múltiples usuarios: Soporta múltiples conexiones simultáneas en la misma red local.

Requisitos del Sistema
-Python 3.8 o superior.
Librerías necesarias:
-socket
-threading
-tkinter (incluida con Python por defecto).
Configuración de red local: La aplicación debe ejecutarse en la misma red para que clientes y servidor puedan comunicarse.
Estructura del Proyecto
Cliente:
Archivo: cliente.py
Funciones principales:
receive(): Escucha mensajes del servidor.
write(): Envía mensajes al servidor.
notify_help(): Envía una notificación de ayuda al servidor.
Servidor:
Archivo: servidor.py
Funciones principales:
broadcast(message): Transmite mensajes a todos los clientes conectados.
handle_client(client): Maneja mensajes y desconexiones de clientes.
receive(): Acepta nuevas conexiones de clientes.
Archivo de Configuración:
Archivo: config.ini
Propósito: Contiene la dirección IP y el puerto del servidor.
Instrucciones de Instalación
Clonar o descargar el proyecto. Descarga todos los archivos (cliente.py, servidor.py, config.ini) y colócalos en una carpeta.

Instalar Python.

Descarga Python desde python.org.
Asegúrate de incluir pip y agregar Python al PATH durante la instalación.
Configurar el servidor.

Abre el archivo config.ini.
Configura los valores de IP y Puerto según tu red local.
Ejecutar el servidor.

Ejecuta servidor.py desde la terminal o un IDE.
bash
Copiar código
python servidor.py
Asegúrate de que la dirección IP y el puerto sean correctos.
Ejecutar el cliente.

Ejecuta cliente.py desde la terminal o un IDE.
bash
Copiar código
python cliente.py
Ingresa un apodo cuando se te solicite y comienza a chatear.
Detalles Técnicos
Archivo cliente.py
python
Copiar código
import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

# Funcionalidades principales de cliente
# Se manejan conexión, recepción, y envío de mensajes
Archivo servidor.py
python
Copiar código
import socket
import threading

# Servidor escucha nuevas conexiones y gestiona mensajes
# Difunde mensajes a todos los clientes conectados
Archivo config.ini
ini
Copiar código
[Servidor]
IP = 127.0.0.1
Puerto = 5000
Uso de la Aplicación
Ejecuta primero el servidor en la computadora anfitriona.
Inicia el cliente en otras computadoras de la misma red.
Usa el campo de entrada para enviar mensajes o el botón "Pedir ayuda" para notificaciones.
Mensajes Especiales
Notificación de ayuda: Cuando un usuario presiona el botón "Pedir ayuda", el mensaje:
php
Copiar código
<Apodo> necesita ayuda.
se envía automáticamente a todos los usuarios conectados.
Solución de Problemas
El cliente no se conecta al servidor:
Verifica que el servidor esté ejecutándose.
Asegúrate de que la dirección IP y el puerto coincidan con los de config.ini.
No se reciben mensajes:
Comprueba la conexión de red local.
Revisa si el firewall está bloqueando las conexiones.
Archivos de Ayuda
README.md: Incluye esta documentación.
config.ini: Permite personalizar la configuración del servidor.
