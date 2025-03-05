# from ..db_service import DBHandler
from data_loader import DBHandler

class DBLog(DBHandler):

    def __init__(self, orm_model):
        super().__init__()
        self.orm_model = orm_model
    
    def insert_log(self, log_status, log_entity, error_message=None):
        log_record = self.orm_model(log_status=log_status,
                                    log_entity=log_entity,
                                    error_message=error_message)
        self.db_session.add(log_record)
        self.db_session.commit()

if __name__ == '__main__':
    from data_loader import Base
    from data_loader import LoaderLog
    db = DBLog(LoaderLog)

    db.insert_log(log_status="Started", log_entity="circuit.csv", error_message=None)
    db.insert_log(log_status="Warning", log_entity="circuit.csv", error_message='There is some warning')
    db.insert_log(log_status="Error", log_entity="circuit.csv", error_message="No data found")