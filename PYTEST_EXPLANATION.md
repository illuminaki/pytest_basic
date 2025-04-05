# Pytest: Guía Práctica de Testing en Python

## Introducción

Pytest es uno de los frameworks de testing más populares para Python. Esta guía explica los conceptos fundamentales de testing usando pytest, con ejemplos prácticos y mejores prácticas.

## Conceptos Fundamentales

### 1. Tests Unitarios
- Prueban unidades individuales de código (funciones, métodos, clases)
- Aíslan la funcionalidad específica
- Verifican comportamientos esperados

### 2. Fixtures
- Proporcionan datos o estados para los tests
- Reutilizables entre diferentes tests
- Reducen la duplicación de código

### 3. Assertions
- Verifican resultados esperados
- Comprueban estados y comportamientos
- Proporcionan mensajes claros de error

## Estructura del Proyecto

```
pytest_basic/
├── src/
│   ├── __init__.py
│   └── calculator.py
├── tests/
│   ├── __init__.py
│   └── test_calculator.py
├── requirements.txt
└── README.md
```

## Ejemplos Prácticos

### Test Básico
```python
def test_suma():
    assert 2 + 2 == 4, "La suma básica debería funcionar"
```

### Test con Fixture
```python
import pytest

@pytest.fixture
def calculator():
    return Calculator()

def test_calculator_suma(calculator):
    assert calculator.suma(3, 5) == 8
```

### Test Parametrizado
```python
@pytest.mark.parametrize("a, b, expected", [
    (3, 5, 8),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_suma_parametrizada(a, b, expected):
    assert suma(a, b) == expected
```

## Buenas Prácticas

1. **Nombrado de Tests**
   - Usar nombres descriptivos
   - Seguir el patrón test_[funcionalidad]_[escenario]
   - Mantener consistencia en el nombrado

2. **Organización**
   - Separar tests por funcionalidad
   - Usar fixtures para código común
   - Mantener tests independientes

3. **Assertions**
   - Usar assertions específicas
   - Incluir mensajes descriptivos
   - Verificar casos límite

4. **Cobertura**
   - Probar casos positivos y negativos
   - Incluir casos límite
   - Verificar excepciones esperadas

## Comandos Útiles

```bash
# Ejecutar todos los tests
pytest

# Ejecutar tests con verbose
pytest -v

# Ejecutar tests con nombre específico
pytest test_calculator.py

# Mostrar cobertura de código
pytest --cov=src

# Generar reporte HTML de cobertura
pytest --cov=src --cov-report=html
```

## Patrones Comunes

### 1. Setup y Teardown
```python
def setup_function():
    # Se ejecuta antes de cada test
    pass

def teardown_function():
    # Se ejecuta después de cada test
    pass
```

### 2. Marcadores
```python
@pytest.mark.slow
def test_operacion_lenta():
    # Test que toma tiempo
    pass
```

### 3. Excepciones
```python
def test_division_por_cero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
```

## Integración Continua

1. **Configuración con GitHub Actions**
   - Automatización de tests
   - Verificación de cobertura
   - Reportes de resultados

2. **Pre-commit Hooks**
   - Ejecutar tests antes de commits
   - Verificar estilo de código
   - Asegurar calidad de código

## Mejores Prácticas de Testing

1. **FIRST Principles**
   - Fast (Rápido)
   - Independent (Independiente)
   - Repeatable (Repetible)
   - Self-validating (Auto-validante)
   - Timely (Oportuno)

2. **Arrange-Act-Assert**
   - Preparar el escenario
   - Ejecutar la acción
   - Verificar resultados

3. **Mocking y Patching**
   - Simular dependencias externas
   - Aislar unidades de código
   - Controlar comportamientos

## Referencias

- Documentación oficial de Pytest
- Python Testing with Pytest (Brian Okken)
- Clean Code (Robert C. Martin)
- Test-Driven Development (Kent Beck)
