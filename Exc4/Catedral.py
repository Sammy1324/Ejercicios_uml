class Catedral:
    def __init__(self, name, city, community, construction_beginning_year, construction_material, consecration_official_date):
        self.name = name
        self.city = city
        self.community = community
        self.construction_beginning_year = construction_beginning_year
        self.construction_material = construction_material
        self.consecration_official_date = consecration_official_date

    def __str__(self):
        return f"{self.name} - {self.city} - {self.construction_beginning_year} - {self.construction_material} - {self.consecration_official_date}"
    def __repr__(self):
        return f"{self.name} - {self.city} - {self.construction_beginning_year} - {self.construction_material} - {self.consecration_official_date}"