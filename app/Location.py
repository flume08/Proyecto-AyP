class Location:
    def __init__(self,lat,long,locality,country):
        self.lat = lat
        self.long = long
        self.locality = locality
        self.country = country
    def show_attributes(self):
        print('\n')
        print(f'Latitude ==> {self.lat}')
        print(f'Long ==> {self.long}')
        print(f'Locality ==> {self.locality}')
        print(f'Country ==> {self.country}')
 