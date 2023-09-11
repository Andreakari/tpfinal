from guizero import App, Text, PushButton, Box, ListBox

# Datos de ejemplo para las encuestas
encuestas = [
    {
        "pregunta": "¿Cuál es la capital de Francia?",
        "opciones": ["Londres", "Berlín", "París", "Madrid"],
        "respuesta_correcta": "París"
    },
    {
        "pregunta": "¿Cuál es el río más largo del mundo?",
        "opciones": ["Nilo", "Amazonas", "Misisipi", "Yangtsé"],
        "respuesta_correcta": "Amazonas"
    },
    {
        "pregunta": "¿Cuál es el planeta más grande del sistema solar?",
        "opciones": ["Tierra", "Marte", "Júpiter", "Venus"],
        "respuesta_correcta": "Júpiter"
    },
    {
        "pregunta": "¿Qué es un CPU?",
        "opciones": ["Central Processing Unit", "Computer Personal Unit", "Control Processing Unit", "Central Process Unit"],
        "respuesta_correcta": "Central Processing Unit"
    },
    {
        "pregunta": "¿Cuál es el lenguaje de programación más utilizado?",
        "opciones": ["Java", "C++", "Python", "JavaScript"],
        "respuesta_correcta": "Python"
    },
    {
        "pregunta": "¿Qué significa HTML?",
        "opciones": ["Hyperlink Text Markup Language", "Hypertext Transfer Markup Language", "High-level Text Markup Language", "Hyper Transfer Text Markup Language"],
        "respuesta_correcta": "Hypertext Transfer Markup Language"
    },
    {
        "pregunta": "¿En qué año se fundó Google?",
        "opciones": ["1995", "2000", "1998", "2002"],
        "respuesta_correcta": "1998"
    }
]

contador_encuesta = 0

# Variables para llevar un registro de las respuestas correctas e incorrectas
respuestas_correctas = 0
respuestas_incorrectas = 0

# Cantidad total de preguntas en la encuesta
total_preguntas = len(encuestas)

# Función para mostrar una encuesta
def mostrar_encuesta():
    if contador_encuesta < total_preguntas:
        encuesta_actual = encuestas[contador_encuesta]
        pregunta_text.value = f"Pregunta {contador_encuesta + 1} de {total_preguntas}:\n{encuesta_actual['pregunta']}"
        opciones_list.clear()
        for opcion in encuesta_actual["opciones"]:
            opciones_list.append(opcion)

# Función para verificar la respuesta
def verificar_respuesta():
    global respuestas_correctas, respuestas_incorrectas
    seleccionados = opciones_list.value
    if seleccionados is None:
        resultado_text.value = "Por favor, selecciona al menos una opción."
    elif contador_encuesta < total_preguntas:
        respuesta_correcta = encuestas[contador_encuesta]["respuesta_correcta"]
        if respuesta_correcta in seleccionados:
            resultado_text.value = "Respuesta Correcta"
            respuestas_correctas += 1
        else:
            resultado_text.value = "Respuesta Incorrecta"
            respuestas_incorrectas += 1

# Función para avanzar a la siguiente encuesta
def siguiente_encuesta():
    global contador_encuesta
    contador_encuesta += 1
    if contador_encuesta < total_preguntas:
        mostrar_encuesta()
        resultado_text.value = ""  # Limpiar el resultado cuando avanzas a la siguiente encuesta
    elif contador_encuesta == total_preguntas:
        # Después de responder la última pregunta, muestra el botón de contador
        mostrar_contador_button.enable()

# Función para mostrar el recuento de respuestas al final de la encuesta
def mostrar_contador():
    resultado_text.value = f"Respuestas Correctas: {respuestas_correctas}\nRespuestas Incorrectas: {respuestas_incorrectas}"

# Crear la aplicación principal con un fondo de color
app = App("Encuestas Interactivas", width=800, height=400, bg="Gray")

# Crear texto para la pregunta
pregunta_text = Text(app, text="", grid=[0, 0, 2, 1])

# Crear lista de opciones para selección múltiple
opciones_list = ListBox(app, multiselect=True, grid=[0, 1, 2, 1])

# Crear botón para verificar la respuesta
verificar_button = PushButton(app, text="Verificar", command=verificar_respuesta, grid=[0, 2, 1, 1])

# Crear botón para avanzar a la siguiente encuesta
siguiente_button = PushButton(app, text="Siguiente", command=siguiente_encuesta, grid=[1, 2, 1, 1])

# Crear texto para mostrar el resultado
resultado_text = Text(app, text="", grid=[0, 3, 2, 1])

# Crear botón para mostrar el recuento de respuestas (inicialmente deshabilitado)
mostrar_contador_button = PushButton(app, text="Mostrar Contador al Final de la Encuesta", command=mostrar_contador, grid=[0, 4, 2, 1])
mostrar_contador_button.disable()  # Inicialmente deshabilitado

# Mostrar la primera encuesta al iniciar
mostrar_encuesta()

app.display()
