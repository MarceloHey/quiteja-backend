from app import db, app
from sqlalchemy import Integer, Column, DateTime, func, String, Float


class Debt(db.Model):
    __tablename__ = "debts"
    id = Column(Integer, primary_key=True)
    product = Column(String(256), nullable=False)
    due_date = Column(DateTime(timezone=True), nullable=False)
    value = Column(Float, nullable=False)
    user_id = Column(Integer, unique=True, nullable=False)
    created_at = Column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.current_timestamp(),
    )

    def __repr__(self):
        return f"<Debt {self.name}>"


with app.app_context():
    db.create_all()
