# 👑 Invitación Digital Interactiva - Plantilla Royal Grace (Clon Exacto)

Clonación completa e interactiva de la plantilla **Royal Grace** de [Zareqia](https://zareqia.com/invite/demo?template=royal-grace).

---

## 📁 Estructura del Proyecto

```text
invitacion animada/
├── index.html                   # Invitación interactiva completa y lista para usar
├── app.html                     # Versión clonada de la aplicación web React / Vite
├── iniciar_servidor.bat         # Doble clic para iniciar servidor local en Windows
├── server.py                    # Servidor HTTP local en Python
├── royal_grace_demo_data.json   # Datos originales de demostración extraídos
├── README.md                    # Esta guía
└── assets/
    ├── videos/
    │   ├── demo-royal-grace.mp4 # Video de apertura con sobre y sello 3D
    │   └── royal-grace.mp4      # Versión en alta definición limpia
    ├── images/
    │   ├── royal-grace-welcome-bg.jpg # Textura de cabecera superior
    │   ├── royal-grace-general-bg.jpg # Textura general con patrón imperial
    │   ├── royal-grace-end-bg.jpg     # Textura floral de pie de página
    │   ├── slide-1.jpg a 4            # Fotos para galería / diapositivas
    │   ├── Royal_Grace.webp           # Miniatura de portada
    │   └── favicon.png
    ├── audio/
    │   ├── track3.mp3           # Canción romántica de fondo ("Chill")
    │   ├── track1.mp3
    │   └── track2.mp3
    ├── index-DnLzk0PB.css       # Hoja de estilos original compilada
    └── *.js                     # Módulos y librerías React (78 archivos)
```

---

## 🚀 Cómo Ejecutar

### Opción 1: Servidor Local (Recomendado)
Haz **doble clic en `iniciar_servidor.bat`** (o ejecuta `python server.py` en la terminal).
Se abrirá automáticamente en tu navegador en:
- `http://localhost:8080/index.html` (Versión standalone optimizada)
- `http://localhost:8080/app.html?template=royal-grace` (Versión React completa)

### Opción 2: Abrir Directamente
Puedes abrir directamente el archivo `index.html` en Chrome, Edge o Firefox.

---

## ✨ Características y Animaciones Incluidas

1. **Apertura 3D del Sobre con Sello de Cera:**
   - Botón interactivo *"Toca para abrir"* que inicia la animación en video full-screen.
2. **Música de Fondo Romántica:**
   - Pista instrumental con reproductor flotante animado y botón de silencio/reproducción.
3. **Tarjeta de los Novios Animada:**
   - Transición suave al terminar el video con tipografía Dancing Script, corazón dorado y nombres con subtítulos.
4. **Indicador de Desplazamiento:**
   - Animación flotante de flecha que invita a bajar por la invitación.
5. **Tarjeta Raspadita en Forma de Corazón (Royal Heart Scratch Card):**
   - Geometría de corazón SVG exacta de Royal Grace (`13:12` aspect ratio).
   - Lienzo HTML5 Canvas con textura metálica dorada, destellos y viñeta 3D.
   - Detección de rascado continuo con ratón o pantalla táctil/móvil.
   - Al raspar más del 40%, **se revela la fecha, se dispara lluvia de confeti y el título cambia animadamente a *"Nuestra historia comienza"***.
6. **Carrusel de Fotos Interactivo (Photo Slideshow):**
   - Transición fluida con cambio automático cada 4 segundos.
   - Doble capa visual: fondo desenfocado atmosférico (*backdrop blur*) y fotografía frontal nítida.
   - Soporte táctil móvil (*swipe*), arrastre con ratón, flechas de navegación elegantes y puntos indicadores con píldora dorada activa.
7. **Contador Regresivo en Vivo:**
   - Días, Horas, Minutos y Segundos calculados en tiempo real hacia la fecha del evento.
8. **Itinerario / Programa del Día:**
   - Línea de tiempo vertical con iconos y detalles de cada momento (Llegada, Ceremonia, Recepción).
9. **Eventos Previos:**
   - Tarjetas elegantes para eventos como Mahendi, Haldi u otros eventos familiares.
10. **Lugar y Mapa:**
    - Tarjeta con detalles de la recepción y botón directo hacia Google Maps.
11. **Código de Vestimenta:**
    - Indicaciones para damas y caballeros con diseño elegante.
12. **Hospedaje y Transporte:**
    - Instrucciones para hoteles con código de descuento y horarios de transporte / traslado.
13. **Mesa de Regalos:**
    - Mensaje emotivo de agradecimiento y datos bancarios o sobres.
14. **Confirmación de Asistencia (RSVP):**
    - Formulario interactivo que al completarse **envía la confirmación formateada directamente a WhatsApp**.
