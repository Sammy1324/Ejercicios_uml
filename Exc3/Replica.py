from Painting import Painting

class Replica(Painting):
    def __init__(self, title, author, chronological_ascription, technique, sub_technique, support_material, description, original_author, original_technique, original_sub_technique, original_support_material, original_location):
        super().__init__(title, author, chronological_ascription, technique, sub_technique, support_material, description)
        self.original_author = original_author
        self.original_technique = original_technique
        self.original_sub_technique = original_sub_technique
        self.original_support_material = original_support_material
        self.original_location = original_location
