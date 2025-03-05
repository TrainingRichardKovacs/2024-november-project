# from ..models import Base
from data_loader.models import Base
from sqlalchemy import Column, Integer, String, Text, DateTime, func

class LoaderLog(Base):
    __tablename__ = 'loader_logs'
    __table_args__ = {'schema': 'project'}

    log_id = Column(Integer, primary_key=True)
    log_status = Column(String(50))
    log_entity = Column(String(100))
    error_message = Column(Text)
    log_timestamp = Column(DateTime, server_default=func.now())
