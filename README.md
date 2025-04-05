# Python Testing Project with Pytest

Un proyecto de demostración que implementa tests unitarios en Python utilizando pytest. Este proyecto incluye ejemplos de testing sobre una aplicación MVC simple para gestión de tareas.

## Características

- Tests unitarios para modelo, vista y controlador
- Ejemplos de fixtures y parametrización
- Cobertura de código con coverage
- Reportes HTML de cobertura
- Integración con Docker para entorno aislado

## Requisitos

- Docker
- Docker Compose
- Git

## Estructura del Proyecto

```
pytest_basic/
├── pytest/
│   ├── model.py
│   ├── view.py
│   ├── controller.py
│   ├── main.py
│   ├── test_task.py
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── requirements.txt
├── PYTEST_EXPLANATION.md
└── README.md
```

## Módulos del Proyecto

- **model.py**: Implementación del modelo de tareas
- **view.py**: Vista para mostrar las tareas
- **controller.py**: Controlador que coordina modelo y vista
- **main.py**: Punto de entrada de la aplicación
- **test_task.py**: Suite completa de pruebas unitarias

## Iniciar el Proyecto

1. Clona el repositorio:
   ```bash
   git clone git@github.com:illuminaki/pytest_basic.git
   cd pytest_basic/pytest
   ```

2. Construye y ejecuta los contenedores con Docker Compose:
   ```bash
   docker-compose up --build
   ```

3. Ejecutar los tests:
   ```bash
   docker-compose exec app pytest
   ```

## Comandos de Testing

### Ejecutar todos los tests
```bash
docker-compose exec app pytest
```

### Ejecutar tests con verbose
```bash
docker-compose exec app pytest -v
```

### Generar reporte de cobertura
```bash
docker-compose exec app pytest --cov=. --cov-report=html
```

## Desarrollo

Para desarrollar nuevos tests:

1. Los tests se montan en un volumen de Docker, por lo que los cambios se reflejan automáticamente
2. Para añadir nuevas dependencias, actualiza `requirements.txt` y reconstruye:
   ```bash
   docker-compose up --build
   ```

## Detener el Entorno

Para detener el entorno de testing:

```bash
docker-compose down
```

## Documentación Adicional

Para una explicación detallada de los conceptos de testing y pytest, consulta el archivo [PYTEST_EXPLANATION.md](./PYTEST_EXPLANATION.md).
