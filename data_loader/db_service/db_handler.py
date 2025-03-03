"""
statusId,status
1,"Finished"
2,"Disqualified"
3,"Accident"
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBHandler:

    def __init__(self):
        self.engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
        self.session = sessionmaker(bind=self.engine)
        self.db_session = self.session()

    """
    kelleni fog egy olyan megoldás, ahol a self.engine által létrehozott kapcsolatot megszűntetem
    """

    def session_generator(self):
        """
        Generator függvény, amely létrehoz egy SQLAlchemy session-t,
        és biztosítja annak megfelelő bezárását.
        """
        session = self.session
        try:
            yield session
            session.commit() 
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def bulk_data_loader(self, data: list):
        with self.db_session as session:
            session.add_all(data)
            session.commit()


if __name__ == '__main__':
    import sys 
    # sys.path.append(r"C:\WORK\Prooktatas\2024-november-project")
    from data_loader.models.data_model import Status
    db = DBHandler()

    t1 = Status(statusid=1, status="Finished")
    t2 = Status(statusid=2, status="Disqualified")
    t3 = Status(statusid=3, status="Accident")
    
    objects = [t1, t2, t3]

    db.bulk_data_loader(objects)