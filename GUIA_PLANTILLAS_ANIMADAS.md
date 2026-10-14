# 📖 Guía Maestra: Arquitectura de Invitaciones Animadas de Lujo y Mega-Prompt para Nuevas Plantillas

Esta guía desglosa con máxima precisión técnica el funcionamiento interno de la plantilla **Royal Grace**, todos los componentes necesarios para replicar este nivel de animación y elegancia, y te proporciona un **Mega-Prompt Maestro** para generar nuevas plantillas temáticas (Bodas, XV Años, Bautizos, Aniversarios, Fiestas de Gala, etc.) manteniendo exactamente el mismo estándar de interacción y experiencia de usuario.

---

## ÍNDICE
1. [Análisis Técnico Detallado: ¿Cómo Funciona la Animación?](#1-análisis-técnico-detallado-cómo-funciona-la-animación)
   - [1.1 El Motor de Apertura 3D y Audio Desbloqueado](#11-el-motor-de-apertura-3d-y-audio-desbloqueado)
   - [1.2 La Raspadita en Forma de Corazón (Canvas + Clip-Path + Confeti)](#12-la-raspadita-en-forma-de-corazón-canvas--clip-path--confeti)
   - [1.3 El Carrusel Cinemático con Desenfoque Atmosférico](#13-el-carrusel-cinemático-con-desenfoque-atmosférico)
   - [1.4 Contador Regresivo en Tiempo Real y Sincronización con Calendarios](#14-contador-regresivo-en-tiempo-real-y-sincronización-con-calendarios)
   - [1.5 Confirmación de Asistencia (RSVP) Inteligente hacia WhatsApp](#15-confirmación-de-asistencia-rsvp-inteligente-hacia-whatsapp)
2. [Recursos Necesarios para Crear Nuevas Plantillas](#2-recursos-necesarios-para-crear-nuevas-plantillas)
   - [2.1 Biblioteca de Activos (Multimedia y Texturas)](#21-biblioteca-de-activos-multimedia-y-texturas)
   - [2.2 Paletas Cromáticas y Tríadas Tipográficas Recomendadas](#22-paletas-cromáticas-y-tríadas-tipográficas-recomendadas)
3. [Mega-Prompt Maestro para Generar Nuevas Plantillas](#3-mega-prompt-maestro-para-generar-nuevas-plantillas)
   - [3.1 Instrucciones de Uso del Prompt](#31-instrucciones-de-uso-del-prompt)
   - [3.2 Texto Completo del Prompt (Copiar y Pegar)](#32-texto-completo-del-prompt-copiar-y-pegar)

---

## 1. Análisis Técnico Detallado: ¿Cómo Funciona la Animación?

La experiencia de la invitación no es una simple página web estática: está concebida como una **película interactiva en capas** que responde a la física del usuario.

### 1.1 El Motor de Apertura 3D y Audio Desbloqueado
* **El Problema del Autoplay en Navegadores:**  
  Tanto iOS Safari como Google Chrome bloquean la reproducción automática de audio y videos con sonido sin que exista una interacción física previa del usuario (*User Gesture Activation*).
* **La Solución Implementada:**  
  1. La página inicia con una pantalla de bloqueo elegante (`.tap-to-open-overlay`) con el video pausado en el fotograma 0 (`poster="royal-grace-poster.jpg"`).
  2. Un botón pulsante invita al usuario: *"Toca para abrir la invitación"*.
  3. Al recibir el primer clic o toque táctil:
     * Se desvanece suavemente el overlay (`opacity: 0; pointer-events: none`).
     * Se desbloquea el contexto de audio del navegador: el archivo `track3.mp3` comienza a reproducirse con volumen gradual y en bucle.
     * Se reproduce el video 3D full-screen del sobre abriéndose y el sello de cera rompiéndose.
  4. **Orquestación de la Transición:**  
     Exactamente a los **5.5 segundos** (o cuando se dispara el evento `video.ended`), la tarjeta frontal con los nombres de los novios (`.hero-card`) emerge con una animación de escala y opacidad (`transform: translate(-50%, -50%) scale(1); opacity: 1;`), acompañada del indicador flotante de flecha que invita a deslizar hacia abajo.
  5. **Botón Flotante de Música Persistente:**  
     Un botón circular fijo en la esquina superior derecha (`.audio-btn`) con icono SVG animado permite pausar y reanudar la música en cualquier punto de la navegación sin recargar la página.

---

### 1.2 La Raspadita en Forma de Corazón (Canvas + Clip-Path + Confeti)
Esta es una de las piezas visuales más sofisticadas. No es un rectángulo con una máscara sencilla; consta de **5 capas superpuestas**:

```text
[ Capa 5: Borde dorado vectorial SVG (Stroke con opacity 0.8)             ]
[ Capa 4: Brillo especular 3D (Gradiente radial blanco translúcido)       ]
[ Capa 3: Sombra de viñeta 3D (Gradiente radial oscuro blend multiply)    ]
[ Capa 2: Canvas HTML5 interactivo (Raspado con destination-out)          ]
[ Capa 1: Tarjeta con fecha revelada (Fondo pergamino + tipografías)     ]
--------------------------------------------------------------------------
[ Capa 0 Base: Sombra arrojada (Filter: drop-shadow recortado en corazón) ]
```

1. **La Geometría del Corazón (Clip-Path en Objeto Unitario):**  
   Utiliza un `SVG <clipPath id="royal-heart-clip" clipPathUnits="objectBoundingBox">`. Al usar coordenadas normalizadas de 0 a 1:
   ```xml
   <path d="M0.5,0.96 C0.5,0.96 0.06,0.70 0.06,0.36 C0.06,0.18 0.20,0.06 0.32,0.06 C0.42,0.06 0.48,0.14 0.5,0.24 C0.52,0.14 0.58,0.06 0.68,0.06 C0.80,0.06 0.94,0.18 0.94,0.36 C0.94,0.70 0.5,0.96 0.5,0.96 Z"/>
   ```
   El corazón mantiene una proporción áurea de `aspect-ratio: 13 / 12` y escala perfectamente en cualquier pantalla (iPhone, tablet o monitor de escritorio) sin deformarse.

2. **Pintura Procedural de Oro Metálico en el Canvas:**  
   Al cargar la página, una función en JavaScript pinta en el elemento `<canvas>`:
   * Un gradiente radial con reflejo dorado (`#f6dc97` $\rightarrow$ `#d4a84a` $\rightarrow$ `#8a6620`).
   * Cientos de micropartículas doradas, bronce y perla generadas matemáticamente con `Math.random()`.
   * 80 destellos de brillo estelar con bordes difuminados.
   * Un oscurecimiento perimetral para lograr volumen tridimensional.

3. **Mecánica de Raspado Continuo:**  
   En vez de dibujar círculos aislados, el código rastrea `lastPos` y `currentPos`. Al arrastrar el dedo o el ratón:
   ```javascript
   ctx.globalCompositeOperation = 'destination-out'; // "Borra" el oro y deja ver lo de abajo
   ctx.lineWidth = 44;
   ctx.lineCap = 'round';
   ctx.lineJoin = 'round';
   ctx.beginPath();
   ctx.moveTo(lastPos.x, lastPos.y);
   ctx.lineTo(currentPos.x, currentPos.y);
   ctx.stroke();
   ```
   Esto hace que el trazo se sienta sedoso, natural y sin saltos ni cortes.

4. **Medición de Cobertura en Tiempo Real y Revelación:**  
   Cada vez que el usuario raspa, se analiza el canal alfa del canvas (`imgData.data[i] < 200`).  
   Al superar el **40% de área despejada**:
   * El canvas recibe la clase `.fade-out` y desaparece suavemente en 0.75 segundos.
   * El título superior cambia automáticamente de *"Rasca para Descubrir"* a *"Nuestra historia comienza"*.
   * Se dispara el motor de confeti físico con 95 partículas giratorias (doradas, oliva y crema) con aceleración y gravedad.

---

### 1.3 El Carrusel Cinemático con Desenfoque Atmosférico
Para exhibir las fotos de la pareja o festejado sin cortes bruscos:
* **Técnica de Doble Capa:**  
  Dentro de cada diapositiva conviven dos etiquetas `<img>`:
  1. **Fondo ambiental:** La misma foto ampliada al `118%`, desenfocada con `filter: blur(22px)` y atenuada al `68%` de opacidad.
  2. **Foto principal frontal:** Centrada con `object-fit: cover` nítida. Esto garantiza que fotos verticales u horizontales siempre llenen el contenedor de forma estética.
* **Ciclo Automático e Interacción Humana:**  
  * Cambia de diapositiva cada 4000 ms.
  * Si el usuario pasa el ratón o toca la pantalla, el temporizador se pausa automáticamente.
  * Detecta gestos de deslizamiento táctil (*swipe*) con umbral de 38 píxeles.
  * Puntos de navegación con píldora activa animada (`width: 24px; background: #dfb758;`).

---

### 1.4 Contador Regresivo en Tiempo Real y Sincronización con Calendarios
* **Cálculo de Milisegundos:** Calcula `tiempoRestante = fechaObjetivo - fechaActual` y actualiza mediante `requestAnimationFrame` o intervalos de 1 segundo los días, horas, minutos y segundos.
* **Exportación de Calendario Universal:**  
  La función `addToCalendar()` crea en caliente un archivo estándar de calendario `.ics` (*iCalendar*) que descarga el evento con alarma 24 horas antes, y a su vez ofrece el enlace directo para añadirlo a Google Calendar en un solo clic.

---

### 1.5 Confirmación de Asistencia (RSVP) Inteligente hacia WhatsApp
* El formulario captura: Nombre del invitado, Asistencia (Sí/No), Número de pases/acompañantes y mensaje opcional.
* Al enviar, no requiere bases de datos complejas: procesa los datos y abre una URL codificada (`https://wa.me/{numero}?text={mensaje}`) con un mensaje estructurado y con emojis listo para enviar por WhatsApp al anfitrión.

---

## 2. Recursos Necesarios para Crear Nuevas Plantillas

Para fabricar una plantilla nueva con este mismo estándar, requieres los siguientes 4 bloques de insumos:

### 2.1 Biblioteca de Activos (Multimedia y Texturas)

| Archivo | Formato Recomendado | Dimensiones / Especificación | Propósito |
| :--- | :--- | :--- | :--- |
| **Video de Apertura** | MP4 (H.264, Web-optimized) | 1080x1920 (Vertical 9:16) o 1080x1080, ~2 a 4 MB | Animación 3D del sobre abriéndose o telón descorriéndose. |
| **Poster del Video** | JPG / WebP | 1080x1920, ~60 a 90 KB | Primer fotograma estático mientras el usuario presiona "Abrir". |
| **Música de Fondo** | MP3 (128 kbps, Joint Stereo) | Duración de 1:30 a 3:00 min, con loop suave | Canción temática instrumental emotiva. |
| **Textura de Cabecera** | JPG / PNG con transparencia | Ancho 1200px | Fondo con degradado o cenefa superior. |
| **Textura General** | JPG repetible (Seamless Pattern) | 600x600 o similar | Fondo con trama sutil (damasco, mármol, estrellas, lino). |
| **Fotos del Carrusel** | JPG optimizado (Compresión 80%) | 800x1000 píxeles, 4 fotos | Fotografías de estudio o momentos especiales. |
| **Favicon** | PNG 32x32 o 96x96 | 96x96 píxeles | Icono representativo en la pestaña del navegador. |

---

### 2.2 Paletas Cromáticas y Tríadas Tipográficas Recomendadas

#### A. Para Bodas Clásicas y Reales (Estilo Royal Grace)
* **Colores:** Verde Oliva Profundo (`#3E5634`), Dorado Champagne (`#8a7a4e` / `#d4a84a`), Crema Papiro (`#f7f4ed`).
* **Tipografías:**
  * Script/Caligrafía: `Great Vibes` o `Allura`.
  * Encabezados/Romana: `Cinzel` o `Cormorant Garamond`.
  * Lectura: `Montserrat` o `Lora`.

#### B. Para XV Años / Sweet 16 (Estilo Princesa & Glamour)
* **Colores:** Rosa Pastel / Blush (`#E8A598`), Oro Rosa (`#B76E79`), Blanco Perlado (`#FFF9FA`), Acento Borgoña (`#5E1925`).
* **Tipografías:**
  * Script: `Dancing Script` o `Parisienne`.
  * Encabezados: `Playfair Display`.
  * Lectura: `Poppins` o `Montserrat`.

#### C. Para Bautizo o Baby Shower (Estilo Celestial / Angelical)
* **Colores:** Azul Cielo Suave (`#8ECAE6`), Dorado Suave (`#D4AF37`), Blanco Nube (`#FDFDFD`), Lino Beige (`#F2E9E4`).
* **Tipografías:**
  * Script: `Alex Brush` o `Italianno`.
  * Encabezados: `Marcellus`.
  * Lectura: `Nunito` o `Quicksand`.

#### D. Para Fiestas de Gala, Cumpleaños VIP o Aniversarios (Estilo Black & Gold)
* **Colores:** Negro Obsidiana (`#0F0F0F`), Oro Puro (`#DFB758`), Carbón Intenso (`#1E1E1E`), Marfil (`#FFFDF8`).
* **Tipografías:**
  * Script: `Passions Conflict` o `Pinyon Script`.
  * Encabezados: `Cinzel Decorative` o `Bodoni Moda`.
  * Lectura: `Inter` o `Cormorant Infant`.

---

## 3. Mega-Prompt Maestro para Generar Nuevas Plantillas

Copia y pega este prompt en tu IA favorita (Claude, Gemini, GPT) rellenando únicamente la sección de **Parámetros del Evento**. El prompt obligará a la IA a escribir el código completo, sin dependencias pesadas y con todas las animaciones interactivas activas.

---

### 3.1 Instrucciones de Uso del Prompt
1. Copia todo el bloque que está dentro de la caja de código a continuación.
2. Rellena los datos en la sección **`[CONFIGURACIÓN DEL EVENTO]`** (tipo de evento, nombres, colores, fecha, teléfono de WhatsApp).
3. Pídele al modelo que genere el archivo único `index.html` autoportante.

---

### 3.2 Texto Completo del Prompt (Copiar y Pegar)

```markdown
Actúa como un Desarrollador Web Frontend Senior y Diseñador UI/UX especializado en invitaciones web interactivas de ultra lujo y experiencias web inmersivas en HTML5, CSS3 moderno y Vanilla JavaScript.

Tu tarea es crear una plantilla completa, interactiva, responsiva y lista para producción en un único archivo index.html autoportante, inspirada en la arquitectura de la plantilla Royal Grace de Zareqia.

[CONFIGURACIÓN DEL EVENTO]
- Tipo de Evento: [Ej: Boda de Gala / Quinceañera / Bautizo / 50 Años / Baby Shower]
- Nombre(s) de los Protagonistas: [Ej: Isabella Sofía / Zayn & Nora / Mateo]
- Subtítulos / Rol familiar: [Ej: Mis XV Años / Hija de... / Celebración de Amor]
- Fecha y Hora del Evento: [Ej: 2027-04-18T18:00:00]
- Lugar de la Ceremonia y Recepción: [Ej: Hacienda Las Rosas, Salón Imperial]
- Dirección completa y enlace a Maps: [Ej: Av. Principal 123 / Enlace de Google Maps]
- Código de Vestimenta: [Ej: Formal Riguroso / Tonos Pastel]
- Teléfono para RSVP por WhatsApp: [Ej: +521234567890 o tu número con código de país]
- Paleta de Colores Principal:
  * Color Primario (Fondo/Contraste): [Ej: #0F172A o #3E5634 o #1A0B2E]
  * Color Secundario (Acento/Detalles): [Ej: #D4AF37 dorado / #B76E79 oro rosa]
  * Color de Fondo de Pergamino/Secciones: [Ej: #FAF7F2 o #FFF9F5]
  * Color de Texto Principal: [Ej: #2D3748 o #3B4432]
- Estilo Tipográfico Deseado: [Ej: Clásico Imperial / Cuento de Hadas / Modern Luxury]

[REQUISITOS TÉCNICOS Y ARQUITECTURA OBLIGATORIA]

1. ESTRUCTURA Y AUTOCONTENIDO:
- El código debe estar en un ÚNICO archivo HTML limpio, con todo el CSS en la etiqueta <style> y todo el JavaScript en <script>.
- Usa Google Fonts con enlace <link> para tipografía caligráfica (ej: 'Great Vibes', 'Dancing Script'), romana elegante (ej: 'Cinzel', 'Playfair Display') y cuerpo legible ('Cormorant Garamond', 'Montserrat').
- Debe ser 100% Mobile-First y perfectamente responsivo (desde 320px hasta pantallas 4K).

2. SECCIÓN HERO CON APERTURA DE SOBRE 3D Y AUDIO DESBLOQUEADO:
- Incluye un reproductor <video> vertical optimizado de fondo (assets/videos/demo-royal-grace.mp4) con póster (assets/videos/royal-grace-poster.jpg) o la ruta configurada.
- Un overlay elegante "Toca para abrir la invitación" (.tap-to-open-overlay) con animación suave de pulso.
- Al hacer clic en cualquier parte de este overlay:
  a) Desvanece el overlay.
  b) Desbloquea y reproduce un audio de fondo en bucle (<audio id="bg-audio">).
  c) Reproduce el video de apertura del sobre.
  d) A los 5.5 segundos (o evento 'ended'), hace aparecer con animación 'scale-in' la tarjeta con los nombres y subtítulos de los protagonistas y la flecha indicadora de scroll.
- Incluye un botón flotante (.audio-btn) en la esquina superior derecha con icono de bocina/ondas para silenciar/activar la música en cualquier momento.

3. TARJETA RASPADITA EN FORMA DE CORAZÓN (ROYAL HEART SCRATCH CARD):
- Un elemento SVG invisible con <clipPath id="royal-heart-clip" clipPathUnits="objectBoundingBox"> con el trazado vectorial idéntico:
  d="M0.5,0.96 C0.5,0.96 0.06,0.70 0.06,0.36 C0.06,0.18 0.20,0.06 0.32,0.06 C0.42,0.06 0.48,0.14 0.5,0.24 C0.52,0.14 0.58,0.06 0.68,0.06 C0.80,0.06 0.94,0.18 0.94,0.36 C0.94,0.70 0.5,0.96 0.5,0.96 Z"
- Contenedor con aspect-ratio: 13 / 12, capa de sombra arrojada con filtro drop-shadow exterior y contorno SVG dorado con stroke: 1.3px y non-scaling-stroke.
- Dentro del corazón:
  * Capa inferior con textura de pergamino, mensaje "¡Estás Invitado!", fecha en números grandes, día de la semana y hora.
  * Canvas interactivo superior pintado proceduralmente con gradiente radial metálico acorde a la paleta, destellos de luz y micropartículas brillantes.
  * Lógica táctil y de ratón usando 'destination-out' con trazo continuo entre puntos para raspar suavemente.
  * Cálculo dinámico de píxeles despejados: cuando supere el 40%, el canvas debe desvanecerse (fade-out), el título superior debe transformarse animadamente en "Nuestra historia comienza" (o mensaje afín al evento), y debe detonar una lluvia de 90 partículas de confeti en pantalla completa con gravedad y rotación.
- Incluye un botón dorado "Agregar al Calendario" que descargue el evento .ics y ofrezca enlace a Google Calendar.

4. CARRUSEL DE FOTOS CINEMÁTICO (SLIDESHOW):
- Situado debajo de la raspadita.
- Marco elegante con esquinas redondeadas (border-radius: 22px), sombra de lujo y borde sutil.
- Mínimo 4 diapositivas que usen la técnica de doble capa:
  * Imagen de fondo escalada al 118% con filter: blur(22px) y opacidad atenuada.
  * Imagen frontal nítida en primer plano.
- Autoplay cada 4 segundos, pausándose al pasar el ratón o tocar la pantalla.
- Detección de arrastre y swipe táctil izquierda/derecha.
- Flechas circulares prev/next con efecto glassmorphism y puntos indicadores abajo con píldora activa ensanchada.

5. SECCIONES OBLIGATORIAS ADICIONALES:
- Contador Regresivo en Vivo: Días, Horas, Minutos, Segundos con cálculo en tiempo real.
- Itinerario del Día / Programa: Línea de tiempo vertical con iconos vectoriales y horas del evento.
- Ubicación y Recepción: Tarjeta con nombre del salón, dirección y botón con enlace directo a Google Maps.
- Código de Vestimenta: Cuadros ilustrativos para mujeres y hombres con recomendaciones de etiqueta.
- Hospedaje / Transporte (si aplica): Opciones de hoteles o traslados.
- Mesa de Regalos: Mensaje de agradecimiento con datos bancarios o sobres.
- Formulario de Confirmación (RSVP): Campos de nombre, asistencia (Sí/No), acompañantes y mensaje, con botón que genere el enlace directo a WhatsApp listo para enviar.

6. DETALLES ESTÉTICOS:
- Divisores dorados con filigrana SVG entre secciones.
- Animación de entrada con IntersectionObserver (.animate-on-scroll) para que cada bloque aparezca suavemente al hacer scroll.
- No uses librerías pesadas externas como jQuery o Bootstrap. Todo debe ser Vanilla CSS y Vanilla JS ultra rápido y compatible con Vercel y GitHub Pages.

Genera el código completo del archivo index.html listo para guardar y abrir en el navegador.
```

---

### ¿Cómo utilizar esta guía para tus clientes o futuros proyectos?
1. **Guarda este archivo** como referencia maestra del estándar de animación.
2. Cada vez que vayas a cotizar o diseñar una nueva invitación temática, toma el **Mega-Prompt del punto 3.2**, reemplaza los datos de `[CONFIGURACIÓN DEL EVENTO]` y tendrás una plantilla completamente nueva y operativa en cuestión de minutos, conservando el video de apertura, la música, el corazón interactivo y el carrusel de fotos.
