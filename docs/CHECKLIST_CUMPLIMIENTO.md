# Checklist de Cumplimiento - Parcial TicketFast

## Punto 1: Infraestructura de Pruebas

- [x] Se creo el archivo docker-compose.test.yml.
- [x] Se definio el servicio db-test.
- [x] db-test usa la imagen postgres:16-alpine.
- [x] db-test usa tmpfs en /var/lib/postgresql/data.
- [x] Se definio el servicio api-test.
- [x] api-test depende de db-test.
- [x] api-test expone el puerto 8001.

## Punto 2: Prueba de Integracion de API

- [x] Se creo tests/integration/test_api_integracion.py.
- [x] La prueba realiza POST a /reservas/concierto-2026.
- [x] Se envia payload valido con email, zona VIP y cantidad 2.
- [x] Se valida codigo HTTP 201.
- [x] Se consulta directamente la base de datos con SQLAlchemy.
- [x] Se valida que existe un objeto ReservaDB.
- [x] Se valida que cliente_email coincide con el valor enviado.

## Punto 3: Prueba de Sistema

- [x] Se creo tests/system/test_sistema_e2e.py.
- [x] Se usa exclusivamente httpx.
- [x] La prueba apunta a http://localhost:8001.
- [x] Se realiza POST real al evento sistema-evento-xyz.
- [x] Se usa zona General y cantidad 3.
- [x] Se consulta el resumen del evento.
- [x] Se valida que total_recaudado sea 150000.

## Punto 4: Automatizacion Frontend E2E

- [x] Se creo tests/e2e/test_frontend_e2e.py.
- [x] Se usa Playwright.
- [x] La prueba navega a http://localhost:4200/reservas.
- [x] Se usan los data-testid indicados en el enunciado.
- [x] Se diligencia correo, zona VIP y cantidad 1.
- [x] Se hace clic en el boton de confirmacion.
- [x] Se valida dinamicamente el texto 150.000.
- [x] No se usan sleeps manuales.
- [x] Si el frontend no esta disponible, la prueba queda skipped y no failed.

## Repositorio

- [x] Proyecto desarrollado en Python.
- [x] Repositorio versionado con Git.
- [x] Minimo 10 commits antes de la entrega final.
