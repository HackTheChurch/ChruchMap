import pandas as pd

class Database:
    def __init__(self, filename: str = 'churches.csv'):
        churches_dicts = pd.read_csv(filename).to_dict(orient='records')
        self.churches = []
        for church in churches_dicts:
            self.churches.append(Church.from_dict(church))

        # for church in self.churches:
        #     print(church)

        # print(self.db)
    
    def get_list(self):
        return self.churches

class Church:
    def __init__(self, name: str, lat: float, lon: float, closest_mass: str):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.closest_mass = closest_mass

    def to_dict(self):
        return {
            'name': self.name,
            'lat': self.lat,
            'lon': self.lon,
            'closest_mass': self.closest_mass
        }

    def __str__(self):
        return f'{self.name} - {self.lat} - {self.lon} - {self.closest_mass}'

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data['name'], data['lat'], data['lon'], data['closest_mass'])

def test_database():
    db = Database()
    # print(db.get_list())
    churches = db.get_list()
    for church in churches:
        print(church)

if __name__ == '__main__':
    test_database()