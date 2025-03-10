import os

from .core_base_class import CoreBase

class CoreLoader(CoreBase):

    def __init__(self, folder_path, mapping, file_handler, db_handler, log_handler):
        self.folder_path = folder_path
        self.mapping = mapping
        # Depedency Injection
        self.file_handler = file_handler
        self.db_handler = db_handler
        self.log = log_handler

    def list_files_from_folder(self):
        return os.listdir(self.folder_path)

    def generate_orm_object_from_data(self, file_name):
        orm_objects = []

        orm_class = self.mapping[file_name]
        file_path = f"{self.folder_path}/{file_name}"
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
                self.log.insert_log(log_status="Success",
                                log_entity=file_name)

        except Exception as e:
            self.log.insert_log(log_status="Error",
                                log_entity=file_name,
                                error_message=f"Hiba történt a feldolgozásnál, minden további feldolgozást leállítok: {e}")
