# TicketFast - Parcial Pruebas de Software

Proyecto desarrollado para el examen parcial de Pruebas de Integracion, Sistema y E2E.

## Contexto

TicketFast es una plataforma de reserva de boletos para eventos masivos. El sistema permite crear reservas por evento y calcular el total recaudado segun la zona y la cantidad de asientos reservados.

## Reglas de negocio

- Zona VIP: 150000 COP por asiento.
- Zona General: 50000 COP por asiento.
- No se permiten zonas diferentes a VIP o General.
- La cantidad de asientos debe ser minimo 1.
- El total recaudado se calcula sumando cantidad por precio de zona para todas las reservas activas del evento.

## Tecnologias

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker Compose
- Pytest
- HTTPX
- Playwright

## Estructura del proyecto

src/database/
- models.py: modelo ReservaDB.
- config.py: configuracion de conexion a base de datos.
- repositorio.py: operaciones de persistencia y calculo financiero.

src/reservas/
- api.py: endpoints de reservas y resumen financiero.

tests/integration/
- test_api_integracion.py: prueba de integracion con API y consulta directa a base de datos.

tests/system/
- test_sistema_e2e.py: prueba de sistema usando HTTP real con httpx.

tests/e2e/
- test_frontend_e2e.py: prueba E2E de frontend con Playwright.

docs/
- CHECKLIST_CUMPLIMIENTO.md: verificacion de requisitos del parcial.
- COMANDOS_EJECUCION.md: comandos para ejecutar el proyecto y las pruebas.

## Infraestructura de pruebas

El archivo docker-compose.test.yml define:

- db-test con postgres:16-alpine.
- tmpfs en /var/lib/postgresql/data para datos temporales.
- api-test exponiendo el puerto 8001.
- dependencia de api-test hacia db-test con healthcheck.

## Ejecucion rapida

Instalar dependencias:

pip install -r requirements.txt

Levantar contenedores:

docker compose -f docker-compose.test.yml up --build -d

Ejecutar prueba de integracion:

pytest tests/integration/test_api_integracion.py -q

Ejecutar prueba de sistema:

pytest tests/system/test_sistema_e2e.py -q

Ejecutar prueba E2E:

pytest tests/e2e/test_frontend_e2e.py -q

## Nota sobre prueba E2E

El enunciado asume que el frontend esta corriendo en http://localhost:4200.  
Si no esta disponible, la prueba E2E queda como skipped para evitar fallos por una dependencia externa no levantada.
