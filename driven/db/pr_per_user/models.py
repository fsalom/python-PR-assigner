from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class PullRequestPerUserMO(Base):
    __tablename__ = "pr_per_user"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    url: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(auto_now_add=True)
    created_by: Mapped[str] = mapped_column(nullable=False)
    assigned_to_email: Mapped[str] = mapped_column(nullable=False)

    class Meta:
        ordering = ('created_at',)