# 🧭 Step 0: Contexto Backend + Python

## 🎯 Objetivo

Entender qué problema resuelve el backend y por qué empezamos con Python antes de construir APIs con Flask.

---

## 🌐 Frontend vs Backend (Visión Práctica)

### Frontend
Es lo que el usuario ve e interactúa:
- Botones
- Formularios
- Vistas y estilos

### Backend
Es la lógica detrás de escena:
- Validar datos
- Guardar información en base de datos
- Reglas de negocio
- Autenticación
- Responder peticiones HTTP

Piensa así:
- Frontend = mostrador de una tienda
- Backend = almacén + sistema interno

---

## 🔄 Flujo Básico Request/Response

```
Usuario hace click en "Guardar"
    ↓
Frontend envía request (HTTP)
    ↓
Backend valida y procesa
    ↓
Backend responde (JSON)
    ↓
Frontend actualiza la interfaz
```

Este flujo es lo que empezarás a dominar desde hoy.

---

## 🐍 ¿Por qué Python aquí?

- Sintaxis limpia para enfocarte en lógica
- Gran ecosistema backend (Flask, FastAPI, Django)
- Muy usado en automatización y data
- Curva de aprendizaje amigable para primeras semanas

---

## ⚙️ Preparación mínima del entorno

En terminal:

```bash
python3 --version
```

Deberías ver algo como `Python 3.x.x`.

Crear tu primer script:

```bash
mkdir -p ~/python_intro
cd ~/python_intro
touch app.py
```

Contenido de `app.py`:

```python
print("Hola desde Python")
```

Ejecutar:

```bash
python3 app.py
```

---

## 🧠 Mini ejercicio de comprensión

Clasifica cada tarea como frontend o backend:

1. Mostrar una lista de tareas en pantalla
2. Guardar una nueva tarea en base de datos
3. Validar que un email tenga formato correcto en servidor
4. Cambiar color de un botón al hacer hover

---

## ⚠️ Errores comunes al empezar

1. Instalar Python pero usar comando incorrecto (`python` vs `python3`)
2. Escribir código en terminal sin guardarlo en archivo
3. Enfocarse en memorizar sintaxis en vez de entender flujo

---

## ✅ Resultado esperado de este step

Si terminaste este step bien, ya puedes explicar:
- Qué hace el backend
- Cómo se comunica con frontend
- Por qué Python es una buena puerta de entrada
