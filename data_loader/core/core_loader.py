import os

from data_loader.core.core_base_class import CoreBase

class CoreLoader(CoreBase):

    def __init__(self, folder_path, mapping, file_handler, db_handler):
        self.folder_path = folder_path
        self.mapping = mapping
        # Depedency Injection
        self.file_handler = file_handler
        self.db_handler = db_handler

    def list_files_from_folder(self):
        return os.listdir(self.folder_path)

    def generate_orm_object_from_data(self, file_name):
        orm_objects = []

        orm_class = self.mapping[file_name]
        file_path = f"{folder_path}/{file_name}"
        file_data = self.file_handler.get_data_from_csv(file_path)
        cols = [item.lower() for item in file_data.columns]
        file_data.columns = cols            

        orm_objects.extend([orm_class(**item) for item in file_data.to_dict(orient="records")])

        return orm_objects
    
    def run(self):
        files = self.list_files_from_folder()

        try:
            for file_name, _ in self.mapping.items():
                if file_name not in files:
                    raise Exception(f"Missing file: {file_name}")
                
                orm_objects = self.generate_orm_object_from_data(file_name)
                self.db_handler.bulk_data_loader(orm_objects)

        except Exception as e:
            print(f"Hiba történt a feldolgozásnál, minden további feldolgozást leállítok: {e}")


if __name__ == '__main__':
    from data_loader.models.data_models import file_orm_mapping
    from data_loader.file_service.csv_handler import CSVHandler
    from data_loader.db_service.db_handler import DBHandler

    folder_path = r"C:\WORK\Prooktatas\2024-november-project\data"
    loader = CoreLoader(folder_path=folder_path, mapping=file_orm_mapping, file_handler=CSVHandler(), db_handler=DBHandler())

    loader.run()