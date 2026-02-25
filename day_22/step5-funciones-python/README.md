# 🧩 Step 5: Funciones en Python

## 🎯 Objetivo

Crear bloques reutilizables de código para escribir programas más limpios y mantenibles.

---

## 🛠️ Sintaxis básica

```python
def saludar():
    print("Hola")

saludar()
```

---

## 🎛️ Parámetros y argumentos

```python
def saludar_persona(nombre):
    print("Hola", nombre)

saludar_persona("Ana")
saludar_persona("Pedro")
```

---

## ↩️ Retornar valores con `return`

```python
def sumar(a, b):
    return a + b

resultado = sumar(4, 6)
print(resultado)  # 10
```

Sin `return`, la función devuelve `None`.

---

## 🧩 Parámetros por defecto

```python
def saludar(nombre, idioma="es"):
    if idioma == "es":
        return f"Hola {nombre}"
    if idioma == "en":
        return f"Hello {nombre}"
    return f"Saludo no disponible para {nombre}"

print(saludar("Ana"))
print(saludar("John", "en"))
```

---

## 📍 Scope básico

```python
mensaje = "global"

def demo():
    mensaje = "local"
    print(mensaje)

print(mensaje)  # global
demo()          # local
print(mensaje)  # global
```

La variable local solo existe dentro de la función.

---

## 🧪 Ejercicios

1. Crea función `es_par(numero)` que devuelva `True/False`
2. Crea función `calcular_descuento(precio, porcentaje)`
3. Crea función `clasificar_nota(nota)` que retorne texto
4. Crea función `resumen_lista(lista)` que devuelva cantidad de elementos

---

## ⚠️ Errores comunes

1. Confundir `print()` con `return`
2. Declarar función pero olvidarse de llamarla
3. No validar tipos de entrada cuando la función lo necesita
