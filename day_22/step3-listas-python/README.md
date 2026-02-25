# 📦 Step 3: Listas en Python

## 🎯 Objetivo

Aprender a guardar múltiples valores en una sola variable y manipularlos de forma segura.

---

## 📋 Crear listas

```python
nombres = ["Ana", "Luis", "Marta"]
numeros = [10, 20, 30, 40]
mixta = ["Python", 3, True]
```

---

## 🔎 Acceder por índice

```python
frutas = ["manzana", "pera", "plátano"]

print(frutas[0])   # manzana
print(frutas[-1])  # plátano
```

---

## ✂️ Slicing

```python
numeros = [1, 2, 3, 4, 5, 6]

print(numeros[1:4])   # [2, 3, 4]
print(numeros[:3])    # [1, 2, 3]
print(numeros[3:])    # [4, 5, 6]
```

---

## 🛠️ Métodos más usados

```python
tareas = ["estudiar", "entrenar"]

tareas.append("leer")
print(tareas)  # ['estudiar', 'entrenar', 'leer']

tareas.remove("entrenar")
print(tareas)  # ['estudiar', 'leer']

ultima = tareas.pop()
print(ultima)  # leer
print(tareas)  # ['estudiar']
```

Ordenar:

```python
nums = [8, 3, 10, 1]
nums.sort()
print(nums)  # [1, 3, 8, 10]
```

---

## 🧪 Ejercicios

1. Crea una lista con 5 comidas favoritas
2. Añade una comida nueva con `append()`
3. Elimina una con `remove()`
4. Imprime la primera y la última
5. Ordena una lista de números de menor a mayor

---

## ⚠️ Errores comunes

1. Intentar acceder a índices que no existen
2. Confundir `remove(valor)` con `pop(indice)`
3. Modificar una lista mientras la recorres sin cuidado
