from abc import ABC, abstractmethod

"""
Design pattern - Abstract Factory Pattern

Abstract class -> egy abstract classból nem tudsz példányt létrehozni,
                  őt arra használod, hogy ős osztály legyen
"""

class CoreBase(ABC):
    
    @abstractmethod
    def list_files_from_folder(self):
        ...

    @abstractmethod
    def generate_orm_object_from_data(self):
        ...

