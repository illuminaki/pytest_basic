# Ejercicio Práctico: Sistema de Gestión de Biblioteca

Este ejercicio te ayudará a practicar testing en Python usando pytest con un proyecto más complejo. Implementarás un sistema de gestión de biblioteca siguiendo el patrón MVC y escribirás tests exhaustivos para cada componente.

## Descripción del Proyecto

Desarrolla un sistema de gestión de biblioteca que permita:
- Gestionar libros (añadir, eliminar, actualizar)
- Gestionar usuarios (registrar, dar de baja)
- Gestionar préstamos (prestar libros, devolver libros)
- Buscar libros por diferentes criterios
- Generar reportes

## Estructura Sugerida

```
library_system/
├── src/
│   ├── models/
│   │   ├── book.py
│   │   ├── user.py
│   │   └── loan.py
│   ├── views/
│   │   ├── book_view.py
│   │   ├── user_view.py
│   │   └── loan_view.py
│   └── controllers/
│       ├── book_controller.py
│       ├── user_controller.py
│       └── loan_controller.py
└── tests/
    ├── models/
    │   ├── test_book.py
    │   ├── test_user.py
    │   └── test_loan.py
    ├── views/
    │   ├── test_book_view.py
    │   ├── test_user_view.py
    │   └── test_loan_view.py
    └── controllers/
        ├── test_book_controller.py
        ├── test_user_controller.py
        └── test_loan_controller.py
```

## Pasos del Ejercicio

### 1. Implementación del Modelo

#### Book
- Implementa una clase Book con atributos:
  - ID
  - Título
  - Autor
  - ISBN
  - Estado (disponible/prestado)
- Métodos para validar ISBN y actualizar estado

#### User
- Implementa una clase User con:
  - ID
  - Nombre
  - Email
  - Historial de préstamos
- Métodos para validar email y gestionar préstamos

#### Loan
- Implementa una clase Loan que relacione:
  - Libro prestado
  - Usuario
  - Fecha de préstamo
  - Fecha de devolución prevista
- Métodos para calcular multas por retraso

### 2. Tests para los Modelos

Escribe tests que verifiquen:

#### Book Tests
- Creación correcta de libros
- Validación de ISBN
- Cambios de estado
- Manejo de errores

#### User Tests
- Registro correcto de usuarios
- Validación de email
- Límite de préstamos simultáneos
- Historial de préstamos

#### Loan Tests
- Creación de préstamos
- Cálculo de fechas de devolución
- Cálculo de multas
- Estados de préstamo

### 3. Implementación de Controladores

Desarrolla controladores que:
- Coordinen la interacción entre modelos
- Implementen reglas de negocio
- Manejen errores apropiadamente

### 4. Tests para Controladores

Verifica que los controladores:
- Apliquen correctamente las reglas de negocio
- Manejen casos límite
- Gestionen errores adecuadamente
- Coordinen múltiples modelos

### 5. Implementación de Vistas

Crea vistas que:
- Muestren información formateada
- Validen entrada de usuarios
- Manejen diferentes formatos de salida

### 6. Tests para Vistas

Verifica que las vistas:
- Formateen correctamente la salida
- Validen entrada correctamente
- Manejen diferentes tipos de datos

## Casos de Prueba Sugeridos

### 1. Préstamo de Libros
- Prestar libro a usuario válido
- Intentar prestar libro ya prestado
- Prestar a usuario con préstamos vencidos
- Prestar más libros del límite permitido

### 2. Devolución de Libros
- Devolver libro en fecha
- Devolver libro con retraso
- Intentar devolver libro no prestado
- Calcular multas correctamente

### 3. Búsqueda de Libros
- Buscar por título exacto
- Buscar por autor
- Buscar por ISBN
- Búsqueda con resultados múltiples
- Búsqueda sin resultados

### 4. Gestión de Usuarios
- Registro con datos válidos
- Registro con email duplicado
- Actualización de datos
- Baja de usuario con préstamos activos

## Retos Adicionales

1. **Persistencia de Datos**
   - Añade una capa de base de datos
   - Implementa tests con fixtures de base de datos
   - Prueba rollbacks y transacciones

2. **API REST**
   - Implementa endpoints REST
   - Añade tests de integración
   - Prueba diferentes métodos HTTP

3. **Concurrencia**
   - Maneja préstamos simultáneos
   - Implementa bloqueos
   - Prueba condiciones de carrera

## Criterios de Evaluación

✅ Tests cubren casos positivos y negativos
✅ Uso apropiado de fixtures
✅ Tests parametrizados donde sea relevante
✅ Manejo adecuado de excepciones
✅ Cobertura de código > 90%
✅ Tests legibles y bien documentados
✅ Uso de mocks cuando sea apropiado

## Consejos

1. Comienza con tests simples y ve aumentando la complejidad
2. Usa TDD: escribe los tests antes del código
3. Mantén los tests independientes entre sí
4. Documenta los casos de prueba complejos
5. Usa fixtures para código repetitivo
6. Implementa mocks para dependencias externas

## Entrega

El proyecto debe incluir:
- Código fuente completo
- Suite de tests completa
- Documentación de setup
- Reporte de cobertura
- Dockerfile y docker-compose.yml
