# Día 7: Introducción a JavaScript

## ¿Pero qué es programar?

**Programar** es el arte de darle instrucciones a una computadora para que realice tareas específicas. Es como escribir una receta de cocina: paso a paso, le dices a la máquina qué hacer.

Cuando programas, estás creando **algoritmos**: secuencias lógicas de pasos que resuelven un problema. JavaScript es uno de los lenguajes que usamos para escribir estas instrucciones, especialmente en el navegador web.

**¿Por qué JavaScript?**
- Es el único lenguaje que entienden todos los navegadores
- Permite hacer páginas web interactivas
- Es relativamente fácil de aprender para principiantes
- Tiene una comunidad enorme de desarrolladores

---

## Variables

Las **variables** son como cajas donde guardamos información. Imagina que tienes una caja etiquetada "nombre" donde guardas el nombre de una persona. En JavaScript, las variables funcionan exactamente así.

### Asignar un valor a las variables

Para crear una variable y asignarle un valor, usamos el signo `=`:

```javascript
let nombre = "Ana";
let edad = 25;
let estaEstudiando = true;
```

El signo `=` NO significa "igual", significa **"asignar"**. Estamos asignando el valor `"Ana"` a la variable `nombre`.

### var vs let vs const

JavaScript tiene tres formas de declarar variables:

#### **var** (la antigua)
```javascript
var apellido = "García";
```
- Es la forma antigua de declarar variables
- Tiene problemas de alcance (scope) que pueden causar errores
- **Recomendación**: No uses `var` en código nuevo

#### **let** (para valores que cambian)
```javascript
let contador = 0;
contador = 1;  // ✅ Podemos cambiar el valor
contador = 2;  // ✅ Y volverlo a cambiar
```
- Para variables cuyos valores van a cambiar
- Alcance de bloque (más seguro)

#### **const** (para valores constantes)
```javascript
const PI = 3.14159;
PI = 3.14;  // ❌ Error: no se puede reasignar
```
- Para valores que NO van a cambiar
- **Recomendación**: Usa `const` por defecto, solo usa `let` cuando sepas que el valor cambiará

---

## Tipos de Datos

JavaScript tiene varios tipos de datos básicos:

### 1. **String (Cadenas de texto)**
```javascript
const saludo = "Hola Mundo";
const mensaje = 'También con comillas simples';
const nombre = `Mi nombre es ${nombre}`;  // Template literals
```

### 2. **Number (Números)**
```javascript
const edad = 30;
const precio = 19.99;
const temperatura = -5;
```

### 3. **Boolean (Booleanos)**
```javascript
const esMayorDeEdad = true;
const estaLloviendo = false;
```

### 4. **Undefined (Indefinido)**
```javascript
let resultado;  // undefined (declarada pero sin valor)
```

### 5. **Null (Nulo)**
```javascript
const dato = null;  // Intencionalmente vacío
```

### 6. **Array (Arreglos/Listas)**
```javascript
const frutas = ["manzana", "banana", "naranja"];
const numeros = [1, 2, 3, 4, 5];
```

### 7. **Object (Objetos)**
```javascript
const persona = {
  nombre: "Carlos",
  edad: 28,
  ciudad: "Madrid"
};
```

---

## Operaciones

### Operaciones Matemáticas

```javascript
const suma = 5 + 3;           // 8
const resta = 10 - 4;         // 6
const multiplicacion = 6 * 7; // 42
const division = 20 / 4;      // 5
const modulo = 17 % 5;        // 2 (resto de la división)
const potencia = 2 ** 3;      // 8 (2 elevado a 3)
```

### Operaciones con Strings

```javascript
const nombre = "Juan";
const apellido = "Pérez";
const nombreCompleto = nombre + " " + apellido;  // "Juan Pérez"

// Con template literals (más moderno):
const saludo = `Hola, ${nombre} ${apellido}`;  // "Hola, Juan Pérez"
```

### Operaciones de Incremento/Decremento

```javascript
let contador = 0;
contador++;      // contador = 1 (incrementa en 1)
contador--;      // contador = 0 (decrementa en 1)
contador += 5;   // contador = 5 (suma 5)
contador -= 2;   // contador = 3 (resta 2)
contador *= 2;   // contador = 6 (multiplica por 2)
```

---

## Funciones

Las **funciones** son bloques de código reutilizables que realizan una tarea específica. Son como mini-programas dentro de tu programa.

### Declarar una Función

```javascript
// Declaración de función tradicional
function saludar() {
  console.log("¡Hola!");
}

// Llamar/ejecutar la función
saludar();  // Imprime: ¡Hola!
```

### Funciones con Parámetros y Alcance

Los **parámetros** son valores que pasamos a la función para que trabaje con ellos:

```javascript
function saludarPersona(nombre) {
  console.log(`Hola, ${nombre}!`);
}

saludarPersona("Ana");     // Imprime: Hola, Ana!
saludarPersona("Carlos");  // Imprime: Hola, Carlos!
```

**Función Scope (Alcance)**: Las variables declaradas dentro de una función solo existen dentro de esa función.

```javascript
function ejemplo() {
  let variableLocal = "Solo existo aquí";
  console.log(variableLocal);  // ✅ Funciona
}

ejemplo();
console.log(variableLocal);  // ❌ Error: variableLocal no está definida
```

### Funciones que Retornan Valores

```javascript
function sumar(a, b) {
  return a + b;
}

const resultado = sumar(5, 3);  // resultado = 8
console.log(resultado);
```

### Funciones Anónimas

Son funciones sin nombre, generalmente asignadas a variables:

```javascript
const multiplicar = function(a, b) {
  return a * b;
};

console.log(multiplicar(4, 5));  // 20
```

### Arrow Functions (Funciones Flecha) - Moderno

```javascript
const dividir = (a, b) => {
  return a / b;
};

// Versión corta (cuando solo hay un return):
const restar = (a, b) => a - b;

console.log(dividir(10, 2));  // 5
console.log(restar(10, 3));   // 7
```

---

## Operaciones Lógicas

### Operadores de Comparación

```javascript
5 == "5"    // true  (compara solo valor)
5 === "5"   // false (compara valor Y tipo)
5 != "5"    // false
5 !== "5"   // true
5 > 3       // true  (mayor que)
5 < 3       // false (menor que)
5 >= 5      // true  (mayor o igual)
5 <= 4      // false (menor o igual)
```

**⚠️ Importante**: Usa siempre `===` y `!==` en lugar de `==` y `!=` para evitar errores.

### Operadores AND y OR

#### **AND (`&&`)**: Todas las condiciones deben ser verdaderas

```javascript
const edad = 20;
const tieneCarnet = true;

if (edad >= 18 && tieneCarnet) {
  console.log("Puede conducir");  // ✅ Se ejecuta
}
```

#### **OR (`||`)**: Al menos una condición debe ser verdadera

```javascript
const esFinDeSemana = true;
const esVacaciones = false;

if (esFinDeSemana || esVacaciones) {
  console.log("Puede descansar");  // ✅ Se ejecuta
}
```

#### **NOT (`!`)**: Invierte el valor

```javascript
const estaLloviendo = false;

if (!estaLloviendo) {
  console.log("Puedes salir");  // ✅ Se ejecuta
}
```

---

## Controlar el Flujo de tu Código

### if / else if / else

```javascript
const nota = 85;

if (nota >= 90) {
  console.log("Excelente");
} else if (nota >= 70) {
  console.log("Bien");  // ✅ Se ejecuta esto
} else if (nota >= 50) {
  console.log("Suficiente");
} else {
  console.log("Insuficiente");
}
```

### Switch

Útil cuando tienes muchas condiciones basadas en el mismo valor:

```javascript
const diaSemana = "lunes";

switch (diaSemana) {
  case "lunes":
    console.log("Inicio de semana");
    break;
  case "viernes":
    console.log("Casi fin de semana");
    break;
  case "sabado":
  case "domingo":
    console.log("Fin de semana");
    break;
  default:
    console.log("Día regular");
}
```

### Operador Ternario (Condiciones inline)

Una forma compacta de escribir `if/else`:

```javascript
// Sintaxis: condicion ? valorSiTrue : valorSiFalse

const edad = 20;
const mensaje = edad >= 18 ? "Mayor de edad" : "Menor de edad";
console.log(mensaje);  // "Mayor de edad"

// Equivalente a:
let mensajeTradicional;
if (edad >= 18) {
  mensajeTradicional = "Mayor de edad";
} else {
  mensajeTradicional = "Menor de edad";
}
```

---

## Bucles (Loops)

Los bucles nos permiten repetir código múltiples veces.

### While

Se ejecuta mientras la condición sea verdadera:

```javascript
let contador = 0;

while (contador < 5) {
  console.log(`Contador: ${contador}`);
  contador++;
}
// Imprime: 0, 1, 2, 3, 4
```

### For

El bucle más común, ideal cuando sabes cuántas veces quieres repetir:

```javascript
for (let i = 0; i < 5; i++) {
  console.log(`Iteración: ${i}`);
}
// Imprime: 0, 1, 2, 3, 4
```

**Explicación**:
- `let i = 0`: Inicialización
- `i < 5`: Condición (mientras sea true, continúa)
- `i++`: Incremento (después de cada iteración)

### For...of (Recorrer Arrays)

```javascript
const frutas = ["manzana", "banana", "naranja"];

for (const fruta of frutas) {
  console.log(fruta);
}
// Imprime: manzana, banana, naranja
```

### For...in (Recorrer Objetos)

```javascript
const persona = {
  nombre: "Ana",
  edad: 25,
  ciudad: "Madrid"
};

for (const propiedad in persona) {
  console.log(`${propiedad}: ${persona[propiedad]}`);
}
// Imprime:
// nombre: Ana
// edad: 25
// ciudad: Madrid
```

---

## ¿Por qué usar Funciones?

Imagina que necesitas calcular el área de varios rectángulos en tu código:

### ❌ Sin funciones (código repetitivo)

```javascript
// Rectángulo 1
const base1 = 5;
const altura1 = 3;
const area1 = base1 * altura1;
console.log(area1);

// Rectángulo 2
const base2 = 8;
const altura2 = 4;
const area2 = base2 * altura2;
console.log(area2);

// Rectángulo 3
const base3 = 6;
const altura3 = 2;
const area3 = base3 * altura3;
console.log(area3);
```

### ✅ Con funciones (código reutilizable)

```javascript
function calcularArea(base, altura) {
  return base * altura;
}

console.log(calcularArea(5, 3));  // 15
console.log(calcularArea(8, 4));  // 32
console.log(calcularArea(6, 2));  // 12
```

**Ventajas de usar funciones**:
1. **Reutilización**: Escribe una vez, usa muchas veces
2. **Organización**: Código más limpio y fácil de entender
3. **Mantenimiento**: Si hay un error, lo corriges en un solo lugar
4. **Abstracción**: Ocultas la complejidad detrás de un nombre descriptivo

---

## Llamadas de Funciones Anidadas

Puedes llamar funciones dentro de otras funciones:

```javascript
function saludar(nombre) {
  return `Hola, ${nombre}`;
}

function despedir(nombre) {
  return `Adiós, ${nombre}`;
}

function conversacionCompleta(nombre) {
  const saludo = saludar(nombre);
  const despedida = despedir(nombre);
  return `${saludo}. Fue un placer. ${despedida}`;
}

console.log(conversacionCompleta("María"));
// "Hola, María. Fue un placer. Adiós, María"
```

### Ejemplo más complejo:

```javascript
function calcularIVA(precio) {
  return precio * 0.21;
}

function calcularDescuento(precio, porcentaje) {
  return precio * (porcentaje / 100);
}

function precioFinal(precioBase, descuentoPorcentaje) {
  const precioConDescuento = precioBase - calcularDescuento(precioBase, descuentoPorcentaje);
  const iva = calcularIVA(precioConDescuento);
  return precioConDescuento + iva;
}

console.log(precioFinal(100, 10));
// Precio: 100€
// Descuento 10%: 90€
// IVA 21%: 108.9€
```

---

## Renderizado Condicional

En desarrollo web, muchas veces necesitas mostrar u ocultar elementos según condiciones:

```javascript
function mostrarMensajeBienvenida(usuario) {
  if (usuario) {
    return `Bienvenido, ${usuario.nombre}`;
  } else {
    return "Por favor, inicia sesión";
  }
}

const usuarioActual = { nombre: "Carlos", edad: 30 };
console.log(mostrarMensajeBienvenida(usuarioActual));
// "Bienvenido, Carlos"

console.log(mostrarMensajeBienvenida(null));
// "Por favor, inicia sesión"
```

### Con operador ternario:

```javascript
function obtenerEstadoUsuario(estaLogueado) {
  return estaLogueado ? "Usuario activo" : "Usuario invitado";
}

console.log(obtenerEstadoUsuario(true));   // "Usuario activo"
console.log(obtenerEstadoUsuario(false));  // "Usuario invitado"
```

---

## Entonces... ¿Te gustó programar?

La programación es como aprender un nuevo idioma. Al principio puede parecer complicado, pero con práctica se vuelve cada vez más natural.

**Recuerda**:
- ✅ **Practica todos los días**: Aunque sea 15 minutos
- ✅ **Experimenta**: Cambia los valores, rompe el código, aprende de los errores
- ✅ **Lee código de otros**: Aprenderás diferentes formas de resolver problemas
- ✅ **Construye proyectos pequeños**: La mejor forma de aprender es creando cosas

### La pregunta fundamental: ¿Qué preguntar?

Programar es un 70% **hacer las preguntas correctas** y un 30% escribir código. Antes de escribir código, pregúntate:

1. **¿Qué problema estoy resolviendo?**
2. **¿Qué información necesito?** (variables)
3. **¿Qué decisiones debo tomar?** (condicionales)
4. **¿Necesito repetir algo?** (bucles)
5. **¿Puedo reutilizar esto?** (funciones)

---

## Ejercicios Prácticos

Ahora que conoces los conceptos básicos, es momento de practicar. En la carpeta `javascript-intro` encontrarás ejercicios incrementales que te ayudarán a dominar cada concepto.

**Estructura de los ejercicios**:
- `step1-variables.html`: Variables y tipos de datos
- `step2-functions.html`: Funciones básicas
- `step3-conditionals.html`: Condicionales y operadores lógicos
- `step4-loops.html`: Bucles
- `step5-final-project.html`: Proyecto integrador

**¡Adelante! 🚀**
