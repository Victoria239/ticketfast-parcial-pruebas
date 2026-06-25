# Comandos de Ejecucion - TicketFast

## Crear entorno virtual

python -m venv .venv
.\.venv\Scripts\activate

## Instalar dependencias

pip install -r requirements.txt

## Levantar infraestructura de pruebas

docker compose -f docker-compose.test.yml up --build -d

## Verificar contenedores

docker compose -f docker-compose.test.yml ps

## Ejecutar prueba de integracion

pytest tests/integration/test_api_integracion.py -q

## Ejecutar prueba de sistema

Antes de ejecutar la prueba de sistema, se recomienda reiniciar los contenedores para limpiar la base de datos temporal:

docker compose -f docker-compose.test.yml down
docker compose -f docker-compose.test.yml up --build -d
pytest tests/system/test_sistema_e2e.py -q

## Ejecutar prueba E2E de frontend

Instalar navegador de Playwright:

python -m playwright install chromium

Ejecutar prueba:

pytest tests/e2e/test_frontend_e2e.py -q

Nota: si el frontend no esta corriendo en http://localhost:4200, la prueba queda skipped.

## Detener infraestructura

docker compose -f docker-compose.test.yml down
