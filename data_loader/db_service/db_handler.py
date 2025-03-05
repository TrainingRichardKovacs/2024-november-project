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
        try:
            with self.db_session as session:
                session.add_all(data)
                session.commit()
        except Exception as err:
            # ide kellene egy logolás
            raise err


    def initialize_tables_from_orm(self, base):
        base.metadata.create_all(self.engine)
        


if __name__ == '__main__':
    from data_loader.models.data_models import Base
    db = DBHandler()

    db.initialize_tables_from_orm(Base)