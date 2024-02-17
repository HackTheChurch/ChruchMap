import pandas as pd

class Database:
    def __init__(self, filename: str = 'churches.csv'):
        self.db = pd.read_csv(filename)

    def get(self):
        return self.db
    
    def get_list(self):
        return self.db.to_dict(orient='records')

class Church:
    def __init__(self, name: str, lat: float, lon: float):
        self.name = name
        self.lat = lat
        self.lon = lon

    def to_dict(self):
        return {
            'name': self.name,
            'lat': self.lat,
            'lon': self.lon
        }

