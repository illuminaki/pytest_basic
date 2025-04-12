# Integración de SonarQube en un proyecto Python

Este documento explica paso a paso cómo integrar SonarQube en un proyecto Python para analizar la calidad del código y la cobertura de pruebas automatizadas.

---

## Requisitos

- Tener Docker instalado y funcionando.
- Tener un proyecto Python local.
- Tener Python y `pip` instalados.

---

## Paso 1: Iniciar SonarQube con Docker

Asegúrate de tener corriendo SonarQube y su base de datos PostgreSQL. Puedes usar esta configuración Docker:

```bash
docker network create sonarnet

docker run -d --name sonarqube_db --network sonarnet -e POSTGRES_USER=sonar -e POSTGRES_PASSWORD=sonar -e POSTGRES_DB=sonar postgres:14

docker run -d --name sonarqube --network sonarnet -p 9000:9000 \
  -e SONAR_JDBC_URL=jdbc:postgresql://sonarqube_db:5432/sonar \
  -e SONAR_JDBC_USERNAME=sonar \
  -e SONAR_JDBC_PASSWORD=sonar \
  sonarqube:community
```

Espera unos minutos y abre [http://localhost:9000](http://localhost:9000). Inicia sesión y genera un token desde tu cuenta.

---

## Paso 2: Instalar `sonar-scanner` (sin Homebrew)

En sistemas Linux (como Ubuntu), puedes instalar el escáner de Sonar manualmente:

```bash
# Descargar el último sonar-scanner
wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-5.0.1.3006-linux.zip

# Descomprimir
unzip sonar-scanner-cli-5.0.1.3006-linux.zip

# Moverlo a una carpeta más estable
sudo mv sonar-scanner-5.0.1.3006-linux /opt/sonar-scanner

# Agregarlo al PATH (temporalmente en la sesión actual)
export PATH=$PATH:/opt/sonar-scanner/bin

# Verificar que funciona
sonar-scanner -v
```

Para hacerlo permanente, edita tu archivo `~/.zshrc`:

```bash
export PATH=$PATH:/opt/sonar-scanner/bin
```

Luego ejecuta:

```bash
source ~/.zshrc
```

---

## Paso 3: Crear archivo de configuración

En la raíz de tu proyecto Python, crea un archivo llamado `sonar-project.properties` con el siguiente contenido:

```properties
sonar.projectKey=nombre_de_tu_proyecto
sonar.sources=.
sonar.host.url=http://localhost:9000
sonar.login=tu_token_generado
```

---

## Paso 4: Ejecutar el análisis

Con todo configurado, ejecuta desde la terminal en la raíz de tu proyecto:

```bash
sonar-scanner
```

Esto enviará el análisis al servidor de SonarQube, donde podrás revisar los resultados en la interfaz web.

---

## Paso 5 (opcional): Agregar cobertura de pruebas

Instala las dependencias necesarias:

```bash
pip install pytest pytest-cov
```

Genera el reporte de cobertura:

```bash
pytest --cov=nombre_de_tu_paquete --cov-report=xml
```

Esto generará un archivo `coverage.xml`. Luego, agrega esta línea a tu archivo `sonar-project.properties`:

```properties
sonar.coverageReportPaths=coverage.xml
```

Ejecuta nuevamente:

```bash
sonar-scanner
```

---

## Resultado

Ahora podrás ver los resultados de calidad y cobertura en tu instancia local de SonarQube en [http://localhost:9000](http://localhost:9000).

---

