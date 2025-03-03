import pandas as pd

class CSVHandler:
    
    @staticmethod
    def get_data_from_csv(csv_path):
        return pd.read_csv(csv_path)


if __name__ == '__main__':
    file_path = r"C:\WORK\Prooktatas\2024-november-project\data\constructor_results.csv"
    # file_path = r"C:\WORK\Prooktatas\2024-november-project\data\constructor_standings.csv"
    # file_path = r"C:\WORK\Prooktatas\2024-november-project\data\constructors.csv"
    # file_path = r"C:\WORK\Prooktatas\2024-november-project\data\driver_standings.csv"
    # file_path = r"C:\WORK\Prooktatas\2024-november-project\data\drivers.csv"
    # file_path = r"C:\WORK\Prooktatas\2024-november-project\data\lap_times.csv"
    # file_path = r"C:\WORK\Prooktatas\2024-november-project\data\pit_stops.csv"
    # file_path = r"C:\WORK\Prooktatas\2024-november-project\data\qualifying.csv"
    # file_path = r"C:\WORK\Prooktatas\2024-november-project\data\races.csv"
    # file_path = r"C:\WORK\Prooktatas\2024-november-project\data\results.csv"
    # file_path = r"C:\WORK\Prooktatas\2024-november-project\data\seasons.csv"
    # file_path = r"C:\WORK\Prooktatas\2024-november-project\data\sprint_results.csv"
    # file_path = r"C:\WORK\Prooktatas\2024-november-project\data\status.csv"



    data = CSVHandler.get_data_from_csv(file_path)

    print(data.head(3))