# Step 3: Callbacks y el "Callback Hell" 🔥

## ¿Qué es un Callback?

Un **callback** es una función que se pasa como parámetro a otra función para que se ejecute **después** de que algo termine.

```javascript
function hacerAlgo(callback) {
  console.log('Haciendo algo...');
  callback(); // Ejecuta la función que pasamos
}

// Pasamos una función como callback
hacerAlgo(() => {
  console.log('¡Terminé!');
});

// Salida:
// Haciendo algo...
// ¡Terminé!
```

---

## Callbacks en Operaciones Asíncronas

Los callbacks son muy comunes en operaciones asíncronas:

### Ejemplo con setTimeout

```javascript
console.log('Inicio');

setTimeout(() => {
  console.log('Callback ejecutado después de 1 segundo');
}, 1000);

console.log('Fin');

// Salida:
// Inicio
// Fin
// (espera 1 segundo)
// Callback ejecutado después de 1 segundo
```

### Ejemplo con Eventos

```javascript
const boton = document.querySelector('button');

// El callback se ejecuta cuando haces clic
boton.addEventListener('click', () => {
  console.log('¡Botón clickeado!');
});
```

---

## Callbacks para Secuencias

¿Qué pasa si necesitas hacer **varias operaciones en secuencia**?

### Escenario: Pedir datos de un usuario

1. Obtener usuario por ID
2. Obtener sus posts
3. Obtener comentarios del primer post

```javascript
// Simular operaciones asíncronas
function obtenerUsuario(id, callback) {
  setTimeout(() => {
    console.log('Usuario obtenido');
    callback({ id: id, nombre: 'Juan' });
  }, 1000);
}

function obtenerPosts(userId, callback) {
  setTimeout(() => {
    console.log('Posts obtenidos');
    callback([{ id: 1, titulo: 'Primer post' }]);
  }, 1000);
}

function obtenerComentarios(postId, callback) {
  setTimeout(() => {
    console.log('Comentarios obtenidos');
    callback(['Comentario 1', 'Comentario 2']);
  }, 1000);
}

// Usarlos en secuencia...
obtenerUsuario(1, (usuario) => {
  console.log('Usuario:', usuario.nombre);
  
  obtenerPosts(usuario.id, (posts) => {
    console.log('Posts:', posts.length);
    
    obtenerComentarios(posts[0].id, (comentarios) => {
      console.log('Comentarios:', comentarios.length);
    });
  });
});
```

**Problema**: Ya empieza a verse anidado y difícil de leer...

---

## El "Callback Hell" (Pirámide de la Muerte) 💀

Cuando tienes muchas operaciones asíncronas secuenciales, tu código se convierte en una **pirámide indentada**:

```javascript
hacerAlgo1((resultado1) => {
  hacerAlgo2(resultado1, (resultado2) => {
    hacerAlgo3(resultado2, (resultado3) => {
      hacerAlgo4(resultado3, (resultado4) => {
        hacerAlgo5(resultado4, (resultado5) => {
          hacerAlgo6(resultado5, (resultado6) => {
            console.log('¡Finalmente!');
          });
        });
      });
    });
  });
});
```

### ¿Por qué es un problema?

1. **❌ Difícil de leer**: Demasiada indentación
2. **❌ Difícil de mantener**: Cambiar algo es complicado
3. **❌ Difícil de debuggear**: Encontrar errores es un caos
4. **❌ Difícil de testear**: No puedes probar partes individuales fácilmente
5. **❌ Manejo de errores complejo**: Tienes que manejar errores en cada nivel

---

## Ejemplo Real: Callback Hell

Imagina que necesitas:

1. Autenticarte con un servidor
2. Obtener datos de usuario
3. Obtener configuración del usuario
4. Obtener notificaciones
5. Renderizar todo

```javascript
autenticar('usuario', 'password', (error, token) => {
  if (error) {
    console.log('Error de autenticación:', error);
    return;
  }
  
  obtenerUsuario(token, (error, usuario) => {
    if (error) {
      console.log('Error obteniendo usuario:', error);
      return;
    }
    
    obtenerConfiguracion(usuario.id, (error, config) => {
      if (error) {
        console.log('Error obteniendo config:', error);
        return;
      }
      
      obtenerNotificaciones(usuario.id, (error, notificaciones) => {
        if (error) {
          console.log('Error obteniendo notificaciones:', error);
          return;
        }
        
        renderizar(usuario, config, notificaciones, (error) => {
          if (error) {
            console.log('Error renderizando:', error);
            return;
          }
          
          console.log('¡Todo listo!');
        });
      });
    });
  });
});
```

**Resultado**: Un código imposible de mantener 😱

---

## Visualización del Problema

### Sin Callback Hell (Ideal)
```
Paso 1
Paso 2
Paso 3
Paso 4
```

### Con Callback Hell (Realidad)
```
Paso 1
  Paso 2
    Paso 3
      Paso 4
        Paso 5
          Paso 6
            Paso 7
              ¡Ayuda!
```

---

## Intentos de Solución: Funciones Nombradas

Puedes intentar evitar la pirámide usando funciones nombradas:

```javascript
function paso3(resultado3) {
  console.log('Paso 3:', resultado3);
}

function paso2(resultado2) {
  hacerAlgo3(resultado2, paso3);
}

function paso1(resultado1) {
  hacerAlgo2(resultado1, paso2);
}

hacerAlgo1(paso1);
```

**Problema**: Aunque es menos anidado, sigue siendo difícil de seguir el flujo del código.

---

## Manejo de Errores en Callbacks

El manejo de errores es repetitivo y propenso a errores:

```javascript
function obtenerDatos(callback) {
  setTimeout(() => {
    const error = null; // o un error real
    const datos = { nombre: 'Juan' };
    
    if (error) {
      callback(error, null);
    } else {
      callback(null, datos);
    }
  }, 1000);
}

// Usar:
obtenerDatos((error, datos) => {
  if (error) {
    console.log('Error:', error);
    return;
  }
  
  console.log('Datos:', datos);
  
  // Si necesitas otra operación, anidas de nuevo...
  otraOperacion(datos, (error, resultado) => {
    if (error) {
      console.log('Error:', error);
      return;
    }
    
    // Y así sucesivamente...
  });
});
```

**Problema**: Tienes que verificar `if (error)` en cada nivel.

---

## Comparación: Callbacks vs Código Síncrono

### Código Síncrono (Fácil de leer)
```javascript
try {
  const usuario = obtenerUsuario(1);
  const posts = obtenerPosts(usuario.id);
  const comentarios = obtenerComentarios(posts[0].id);
  console.log('Listo!');
} catch (error) {
  console.log('Error:', error);
}
```

### Callbacks (Difícil de leer)
```javascript
obtenerUsuario(1, (error, usuario) => {
  if (error) return console.log(error);
  
  obtenerPosts(usuario.id, (error, posts) => {
    if (error) return console.log(error);
    
    obtenerComentarios(posts[0].id, (error, comentarios) => {
      if (error) return console.log(error);
      
      console.log('Listo!');
    });
  });
});
```

---

## ¿Cuál es la Solución?

### 🎉 Promises al Rescate

JavaScript introdujo **Promises** para solucionar el Callback Hell.

Con Promises, el código de arriba se vería así:

```javascript
obtenerUsuario(1)
  .then(usuario => obtenerPosts(usuario.id))
  .then(posts => obtenerComentarios(posts[0].id))
  .then(comentarios => {
    console.log('Listo!');
  })
  .catch(error => {
    console.log('Error:', error);
  });
```

**Ventajas**:
- ✅ Más legible (flujo lineal)
- ✅ Un solo `.catch()` para todos los errores
- ✅ Más fácil de mantener
- ✅ Más fácil de testear

---

## Puntos Clave ✨

1. **Callback**: Función que se ejecuta después de otra operación
2. **Callback Hell**: Pirámide de callbacks anidados
3. **Problemas**: Difícil de leer, mantener, debuggear y testear
4. **Solución**: Promises (Step 4) y async/await (Step 5)
5. **Manejo de errores**: Repetitivo en cada nivel con callbacks

---

## Tu Ejercicio 🎯

Analiza este código y cuenta cuántos niveles de anidación tiene:

```javascript
operacion1((resultado1) => {
  operacion2(resultado1, (resultado2) => {
    operacion3(resultado2, (resultado3) => {
      operacion4(resultado3, (resultado4) => {
        console.log('Final:', resultado4);
      });
    });
  });
});
```

**Respuesta**: 4 niveles de anidación

**Pregunta**: ¿Cómo manejarías errores en cada operación? (Spoiler: tedioso)

---

## Próximos Pasos

Ahora que entiendes el problema del Callback Hell:

✅ Qué son los callbacks  
✅ Por qué los callbacks anidados son problemáticos  
✅ Dificultades de mantenimiento y manejo de errores  

Estarás listo para:
- **Step 4**: Promises - La solución al Callback Hell
- **Step 5**: Async/Await - Sintaxis más limpia sobre Promises

---

**💡 Consejo**: El Callback Hell fue un problema real en JavaScript antiguo. Por eso se crearon las Promises. Entender el problema te ayudará a apreciar la solución.

**🎯 Regla**: Si ves más de 2-3 niveles de callbacks anidados, probablemente necesitas Promises o async/await.

**📖 Historia**: Antes del 2015 (ES6), todos teníamos que lidiar con Callback Hell. Las Promises cambiaron todo.
