from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .database import db


class Review(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    review_text: Mapped[str] = mapped_column(String(500), unique=True, nullable=False)
