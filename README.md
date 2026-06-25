# TicketFast - Parcial Pruebas de Software

Proyecto desarrollado para el examen parcial de **Pruebas de Integración, Sistema y E2E** del curso de Pruebas de Software.  
El sistema simula una plataforma llamada **TicketFast**, encargada de gestionar reservas de boletos para eventos masivos.

## Descripción del proyecto

TicketFast permite registrar reservas de asientos para eventos y calcular el total recaudado según la zona seleccionada y la cantidad de asientos reservados.

Las zonas disponibles son:

- **VIP:** 150.000 COP por asiento.
- **General:** 50.000 COP por asiento.

Además, el sistema valida que solo se puedan registrar reservas con zonas válidas y con una cantidad mínima de un asiento.

## Qué se realizó

En este proyecto se implementó una API con **FastAPI**, persistencia con **SQLAlchemy** y una base de datos real en **PostgreSQL** usando Docker.

También se desarrollaron las pruebas solicitadas en el parcial:

- Prueba de integración de API.
- Prueba de sistema usando peticiones HTTP reales.
- Prueba E2E de frontend con Playwright.
- Infraestructura de pruebas con `docker-compose.test.yml`.

## Tecnologías utilizadas

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker Compose
- Pytest
- HTTPX
- Playwright

## Estructura del proyecto

```txt
ticketfast-parcial-pruebas/
│
├── src/
│   ├── database/
│   │   ├── config.py
│   │   ├── models.py
│   │   └── repositorio.py
│   │
│   └── reservas/
│       └── api.py
│
├── tests/
│   ├── integration/
│   │   └── test_api_integracion.py
│   │
│   ├── system/
│   │   └── test_sistema_e2e.py
│   │
│   └── e2e/
│       └── test_frontend_e2e.py
│
├── frontend_mock/
│   └── app.py
│
├── docs/
│   ├── CHECKLIST_CUMPLIMIENTO.md
│   └── COMANDOS_EJECUCION.md
│
├── docker-compose.test.yml
├── Dockerfile
├── requirements.txt
└── pytest.ini

Ejecución del proyecto
1. Crear y activar entorno virtual
python -m venv .venv

En Windows:

.\.venv\Scripts\activate
2. Instalar dependencias
pip install -r requirements.txt
3. Instalar navegador de Playwright
python -m playwright install chromium
4. Levantar la infraestructura de pruebas
docker compose -f docker-compose.test.yml up --build -d
5. Verificar contenedores
docker compose -f docker-compose.test.yml ps

Se espera que los servicios db-test y api-test estén activos.

6. Levantar el frontend mock

En otra terminal, ejecutar:

uvicorn frontend_mock.app:app --host 127.0.0.1 --port 4200

Este frontend permite validar la prueba E2E en la ruta:

http://localhost:4200/reservas
7. Ejecutar todas las pruebas
pytest tests/integration tests/system tests/e2e -q

