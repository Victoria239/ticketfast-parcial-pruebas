import os

import httpx


API_BASE_URL = os.getenv("API_TEST_URL", "http://localhost:8001")


def test_flujo_completo_reserva_y_resumen_sistema():
    evento_id = "sistema-evento-xyz"

    payload = {
        "cliente_email": "sistema@correo.com",
        "zona": "General",
        "cantidad": 3
    }

    with httpx.Client(base_url=API_BASE_URL, timeout=10.0) as client:
        respuesta_creacion = client.post(
            f"/reservas/{evento_id}",
            json=payload
        )

        assert respuesta_creacion.status_code == 201

        respuesta_resumen = client.get(
            f"/reservas/{evento_id}/resumen"
        )

        assert respuesta_resumen.status_code == 200

        resumen = respuesta_resumen.json()

    assert resumen["evento_id"] == evento_id
    assert resumen["total_recaudado"] == 150000
