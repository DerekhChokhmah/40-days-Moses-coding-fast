from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import ForeignKey
from datetime import datetime, timezone
class Base(DeclarativeBase):
    pass

class Monitor(Base):
    __tablename__ = "monitors"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    url: Mapped[str] = mapped_column()
    active: Mapped[bool] = mapped_column(default=True)

class MonitoringResult(Base):
    __tablename__ = "monitors_results"
    id: Mapped[int] = mapped_column(primary_key=True)   
    monitor_id: Mapped[int] = mapped_column(ForeignKey("monitors.monitor_id")) 
    status_code : Mapped[int] = mapped_column()
    response_time: Mapped[float] = mapped_column()
    success: Mapped[bool] = mapped_column()
    checked_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(timezone.utc))