from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.get("/reservas", response_class=HTMLResponse)
def reservas():
    return '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>TicketFast Reservas</title>
    </head>
    <body>
        <h1>Reservas TicketFast</h1>

        <form id="form-reserva">
            <label>Correo cliente</label>
            <input data-testid="input-email-cliente" type="email" />

            <label>Zona</label>
            <select data-testid="select-zona-evento">
                <option value="">Seleccione una zona</option>
                <option value="VIP">VIP</option>
                <option value="General">General</option>
            </select>

            <label>Cantidad</label>
            <input data-testid="input-cantidad-asientos" type="number" />

            <button data-testid="btn-confirmar-reserva" type="submit">
                Confirmar reserva
            </button>
        </form>

        <section data-testid="seccion-resumen-total">
            Total: 0
        </section>

        <script>
            const form = document.getElementById("form-reserva");

            form.addEventListener("submit", function(event) {
                event.preventDefault();

                const zona = document.querySelector('[data-testid="select-zona-evento"]').value;
                const cantidad = Number(document.querySelector('[data-testid="input-cantidad-asientos"]').value);
                const resumen = document.querySelector('[data-testid="seccion-resumen-total"]');

                let precio = 0;

                if (zona === "VIP") {
                    precio = 150000;
                }

                if (zona === "General") {
                    precio = 50000;
                }

                const total = precio * cantidad;

                resumen.textContent = "Total: " + total.toLocaleString("es-CO");
            });
        </script>
    </body>
    </html>
    '''
