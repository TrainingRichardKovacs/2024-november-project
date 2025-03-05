

"""
A modulok felhasználásával az alábbi feladatokat kellene itt elvégeznem

1. data mappában milyen csv-k vannak
2. a csv-ken végig iterálva kiolvasni az adatokat -> egyesévelű
3. a kialkavasott adatokból példányosítani az ORM model-eket
    - itt meg kell tudnom mondani, hogy melyik file-hoz, melyik model tartozik
4. be kell töltenem az adatot
5. minden lépést, ami fontos: sikeres futás, hiba stb. adatbázisba be kell logolni

"""

from data_loader import DBHandler, file_orm_mapping, CSVHandler, CoreLoader

def main():
    folder_path = r"C:\WORK\Prooktatas\2024-november-project\data"
    loader = CoreLoader(folder_path=folder_path,
                        mapping=file_orm_mapping,
                        file_handler=CSVHandler(),
                        db_handler=DBHandler())
    loader.run()


if __name__ == '__main__':
    main()
