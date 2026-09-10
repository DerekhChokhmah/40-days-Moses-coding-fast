from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import ForeignKey
from datetime import datetime, timezone
from sqlalchemy.orm import relationship
class Base(DeclarativeBase):
    pass

class Monitor(Base):
    __tablename__ = "monitors"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    url: Mapped[str] = mapped_column()
    active: Mapped[bool] = mapped_column(default=True)
    method: Mapped[str] = mapped_column()
    expected_status: Mapped[int] = mapped_column()
    interval_value: Mapped[int] = mapped_column()
    monitor_results: Mapped[list["MonitoringResult"]] = relationship(back_populates="monitor") 

class MonitoringResult(Base):
    __tablename__ = "monitoring_results"
    id: Mapped[int] = mapped_column(primary_key=True)   
    monitor_id: Mapped[int] = mapped_column(ForeignKey("monitors.id")) 
    status_code : Mapped[int] = mapped_column()
    response_time: Mapped[float] = mapped_column()
    success: Mapped[bool] = mapped_column()
    checked_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(timezone.utc))
    monitor: Mapped[Monitor] = relationship(back_populates="monitor_results")