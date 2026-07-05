from sqlalchemy import BigInteger
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from database.db import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    telegram_id: Mapped[int] = mapped_column(
        BigInteger,
        unique=True,
    )

    full_name: Mapped[str] = mapped_column(
        String(255)
    )

    username: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )
