from sqlalchemy import Integer, String, Date, DateTime, func
from sqlalchemy.orm import mapped_column
from app import db


class User(db.Model):
    __tablename__ = "users"
    id = mapped_column(Integer, primary_key=True)
    cpf = mapped_column(String(11), unique=True, nullable=False)
    name = mapped_column(String(100), unique=True, nullable=False)
    date = mapped_column(Date(), nullable=False)
    created_at = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.current_timestamp(),
    )

    def __repr__(self):
        return f"<User {self.name}>"
