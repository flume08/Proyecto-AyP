
class Map:
    def __init__(self,general,vip) -> None:
        self.general = general
        self.vip = vip
    def get_mapvip(self):
        map = []
        for row in range(self.vip[0]):
            row = []
            for value in range(self.vip[1]):
                value =0
                row.append(value)
            map.append(row)
        return map
    def get_mapgeneral(self):
        map = []
        for row in range(self.general[0]):
            row = []
            for value in range(self.general[1]):
                value =0
                row.append(value)
            map.append(row)
        return map
