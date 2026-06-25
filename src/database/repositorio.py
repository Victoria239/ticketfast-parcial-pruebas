from sqlalchemy.orm import Session

from src.database.models import ReservaDB


PRECIOS_ZONAS = {
    "VIP": 150000,
    "General": 50000,
}


class ReservasRepositorio:
    def __init__(self, db: Session):
        self.db = db

    def guardar_reserva(
        self,
        evento_id: str,
        cliente_email: str,
        zona: str,
        cantidad: int
    ) -> ReservaDB:
        nueva_reserva = ReservaDB(
            evento_id=evento_id,
            cliente_email=cliente_email,
            zona=zona,
            cantidad=cantidad
        )

        self.db.add(nueva_reserva)
        self.db.commit()
        self.db.refresh(nueva_reserva)

        return nueva_reserva

    def calcular_total_evento(self, evento_id: str) -> int:
        reservas = (
            self.db.query(ReservaDB)
            .filter(ReservaDB.evento_id == evento_id)
            .all()
        )

        total = 0

        for reserva in reservas:
            precio_zona = PRECIOS_ZONAS.get(reserva.zona, 0)
            total += reserva.cantidad * precio_zona

        return total
