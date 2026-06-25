import os

import httpx
import pytest
from playwright.sync_api import Error as PlaywrightError
from playwright.sync_api import expect, sync_playwright


FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:4200")


def frontend_disponible():
    try:
        response = httpx.get(f"{FRONTEND_URL}/reservas", timeout=3.0)
        return response.status_code < 500
    except httpx.RequestError:
        return False


def test_reserva_vip_muestra_total_formateado():
    if not frontend_disponible():
        pytest.skip("Frontend no disponible en http://localhost:4200/reservas")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        try:
            page.goto(
                f"{FRONTEND_URL}/reservas",
                wait_until="domcontentloaded"
            )

            input_email = page.get_by_test_id("input-email-cliente")
            input_zona = page.get_by_test_id("select-zona-evento")
            input_cantidad = page.get_by_test_id("input-cantidad-asientos")
            boton_confirmar = page.get_by_test_id("btn-confirmar-reserva")
            resumen_total = page.get_by_test_id("seccion-resumen-total")

            expect(input_email).to_be_visible()
            expect(input_zona).to_be_visible()
            expect(input_cantidad).to_be_visible()
            expect(boton_confirmar).to_be_visible()

            input_email.fill("cliente@correo.com")

            tipo_elemento_zona = input_zona.evaluate(
                "(element) => element.tagName.toLowerCase()"
            )

            if tipo_elemento_zona == "select":
                try:
                    input_zona.select_option(value="VIP")
                except PlaywrightError:
                    input_zona.select_option(label="VIP")
            else:
                input_zona.fill("VIP")

            input_cantidad.fill("1")
            boton_confirmar.click()

            expect(resumen_total).to_contain_text("150.000", timeout=10000)

        finally:
            browser.close()
