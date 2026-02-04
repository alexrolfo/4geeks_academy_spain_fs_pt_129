# Step 2: setTimeout - Tu Primera Herramienta Asíncrona ⏱️

## ¿Qué es setTimeout?

**setTimeout** es una función que ejecuta código **después** de un tiempo determinado. Es tu primera herramienta asíncrona.

```javascript
setTimeout(() => {
  console.log('¡Hola después de 2 segundos!');
}, 2000); // 2000 milisegundos = 2 segundos
```

---

## Sintaxis Básica

```javascript
setTimeout(función, milisegundos, parámetro1, parámetro2, ...);
```

### Parámetros:
1. **función**: Qué ejecutar cuando pase el tiempo
2. **milisegundos**: Cuánto esperar (1000ms = 1 segundo)
3. **parámetros** (opcional): Valores que se pasan a la función

---

## Ejemplo 1: Básico

```javascript
console.log('Inicio');

setTimeout(() => {
  console.log('Ejecuto después de 1 segundo');
}, 1000);

console.log('Fin');

// Salida:
// Inicio
// Fin
// (espera 1 segundo)
// Ejecuto después de 1 segundo
```

**Nota**: `Fin` se imprime antes porque setTimeout es **asíncrono**.

---

## Ejemplo 2: Con Parámetros

```javascript
function saludar(nombre, edad) {
  console.log(`Hola ${nombre}, tienes ${edad} años`);
}

// Pasar parámetros después del tiempo
setTimeout(saludar, 2000, 'Ana', 25);

// Después de 2 segundos:
// Hola Ana, tienes 25 años
```

---

## Ejemplo 3: Cancelar setTimeout

Puedes **cancelar** un setTimeout antes de que se ejecute:

```javascript
const timer = setTimeout(() => {
  console.log('Esto nunca se ejecutará');
}, 3000);

// Cancelar antes de que pasen los 3 segundos
clearTimeout(timer);

console.log('Timer cancelado');
```

---

## setInterval: Repetir Código

**setInterval** ejecuta código **repetidamente** cada cierto tiempo.

```javascript
let contador = 0;

const intervalo = setInterval(() => {
  contador++;
  console.log(`Han pasado ${contador} segundos`);
  
  // Detener después de 5 segundos
  if (contador === 5) {
    clearInterval(intervalo);
    console.log('¡Detenido!');
  }
}, 1000); // Cada 1 segundo

// Salida:
// Han pasado 1 segundos
// Han pasado 2 segundos
// Han pasado 3 segundos
// Han pasado 4 segundos
// Han pasado 5 segundos
// ¡Detenido!
```

---

## Diferencia: setTimeout vs setInterval

### setTimeout
```javascript
setTimeout(() => {
  console.log('Se ejecuta UNA VEZ después de 2 segundos');
}, 2000);
```

### setInterval
```javascript
setInterval(() => {
  console.log('Se ejecuta CADA 2 segundos');
}, 2000);
```

| Función | ¿Cuándo? | Cancelar |
|---------|----------|----------|
| **setTimeout** | Una vez después de X ms | `clearTimeout()` |
| **setInterval** | Cada X ms | `clearInterval()` |

---

## Ejemplo Práctico: Contador de 5 a 0

```javascript
let tiempo = 5;

const cuentaRegresiva = setInterval(() => {
  console.log(tiempo);
  tiempo--;
  
  if (tiempo < 0) {
    clearInterval(cuentaRegresiva);
    console.log('¡Tiempo terminado!');
  }
}, 1000);

// Salida:
// 5
// 4
// 3
// 2
// 1
// 0
// ¡Tiempo terminado!
```

---

## ¿Cómo Funciona? Event Loop Simplificado 🔄

JavaScript tiene un **Event Loop** (bucle de eventos) que maneja el código asíncrono:

### 1. Call Stack (Pila de ejecución)
Donde se ejecuta el código síncrono.

```javascript
console.log('A');    // ← Se ejecuta inmediatamente
console.log('B');    // ← Luego esto
```

### 2. Web APIs
Donde van las operaciones asíncronas (setTimeout, fetch, etc).

```javascript
setTimeout(() => {
  console.log('C');  // ← Va a Web APIs
}, 1000);
```

### 3. Task Queue (Cola de tareas)
Cuando el tiempo se cumple, la función va aquí.

### 4. Event Loop
Cuando el Call Stack está vacío, mueve tareas de la Queue al Stack.

---

## Visualización del Event Loop

```javascript
console.log('1');

setTimeout(() => {
  console.log('2');
}, 0); // ⚠️ 0 milisegundos

console.log('3');
```

**¿Qué sucede?**

```
1. Call Stack: console.log('1')           → Imprime "1"
2. Call Stack: setTimeout(...)            → Va a Web APIs
3. Call Stack: console.log('3')           → Imprime "3"
4. Call Stack está vacío                  → Event Loop activa
5. Task Queue: callback de setTimeout     → Mueve al Call Stack
6. Call Stack: console.log('2')           → Imprime "2"
```

**Salida**: 1, 3, 2

**Conclusión**: Incluso con 0ms, setTimeout es asíncrono y se ejecuta después del código síncrono.

---

## Ejemplo Real: Mostrar Mensaje Después de Cargar

```javascript
console.log('Cargando datos...');

setTimeout(() => {
  console.log('✅ Datos cargados exitosamente');
}, 2000);

console.log('Continúa usando la app mientras carga...');

// Salida inmediata:
// Cargando datos...
// Continúa usando la app mientras carga...
// (espera 2 segundos)
// ✅ Datos cargados exitosamente
```

---

## Ejemplo con React

```javascript
import { useState, useEffect } from 'react';

function ContadorTiempo() {
  const [segundos, setSegundos] = useState(0);

  useEffect(() => {
    // Incrementar cada segundo
    const intervalo = setInterval(() => {
      setSegundos(prev => prev + 1);
    }, 1000);

    // Limpiar al desmontar
    return () => clearInterval(intervalo);
  }, []);

  return (
    <div>
      <h2>Han pasado {segundos} segundos</h2>
    </div>
  );
}

export default ContadorTiempo;
```

---

## Errores Comunes

### Error 1: No guardar el ID para cancelar

```javascript
// ❌ MALO - No puedes cancelarlo
setTimeout(() => {
  console.log('No puedo cancelar esto');
}, 5000);

// ✅ BIEN
const timer = setTimeout(() => {
  console.log('Puedo cancelar esto');
}, 5000);

// Si necesito cancelar:
clearTimeout(timer);
```

### Error 2: Olvidar clearInterval

```javascript
// ❌ MALO - Se ejecuta para siempre
setInterval(() => {
  console.log('Esto nunca se detiene');
}, 1000);

// ✅ BIEN
const intervalo = setInterval(() => {
  console.log('Esto puedo detener');
}, 1000);

// Detener después de 5 segundos
setTimeout(() => {
  clearInterval(intervalo);
}, 5000);
```

### Error 3: Confundir segundos con milisegundos

```javascript
// ❌ MALO - Espera 3 milisegundos (casi instantáneo)
setTimeout(() => {
  console.log('Muy rápido');
}, 3); // 3ms

// ✅ BIEN - Espera 3 segundos
setTimeout(() => {
  console.log('Después de 3 segundos');
}, 3000); // 3000ms = 3 segundos
```

---

## setTimeout Anidados (Secuencia)

Si quieres ejecutar cosas en secuencia:

```javascript
console.log('Inicio');

setTimeout(() => {
  console.log('Paso 1');
  
  setTimeout(() => {
    console.log('Paso 2');
    
    setTimeout(() => {
      console.log('Paso 3');
    }, 1000);
  }, 1000);
}, 1000);

// Salida (con 1 segundo entre cada uno):
// Inicio
// Paso 1
// Paso 2
// Paso 3
```

**Problema**: Esto se vuelve difícil de leer (¡adelanto del "Callback Hell" en Step 3!).

---

## Puntos Clave ✨

1. **setTimeout**: Ejecuta código después de X milisegundos
2. **setInterval**: Ejecuta código cada X milisegundos
3. **clearTimeout/clearInterval**: Cancelar timers
4. **Event Loop**: JavaScript procesa asíncrono cuando el Call Stack está vacío
5. **1000ms = 1 segundo**: Siempre usa milisegundos
6. **Siempre limpiar**: Usa clear cuando ya no necesites el timer

---

## Tu Ejercicio 🎯

Crea una cuenta regresiva que:

1. ✅ Empiece en 10
2. ✅ Cada segundo imprima el número
3. ✅ Cuando llegue a 0, imprima "🚀 ¡Despegue!"
4. ✅ Se detenga automáticamente

**Pista**: Usa `setInterval` y `clearInterval`

---

## Próximos Pasos

Una vez domines setTimeout/setInterval:

✅ setTimeout para código asíncrono  
✅ setInterval para repetir código  
✅ Event Loop básico  
✅ Cómo cancelar timers  

Estarás listo para:
- **Step 3**: Callbacks y el problema del "Callback Hell"
- **Step 4**: Promises - Una solución más elegante

---

**💡 Consejo**: setTimeout es tu primera herramienta asíncrona. Es simple, pero es la base para entender código asíncrono más complejo.

**⚠️ Importante**: Siempre recuerda que setTimeout/setInterval son **aproximados**. Si el Call Stack está ocupado, pueden retrasarse más del tiempo especificado.
