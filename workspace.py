class Part:
    def __init__(self, shape):
        self.shape = shape
        self.relationships = set()
        
    def add_relationship(self, relationship):
        self.relationships.add(relationship)

class Workspace:
    def __init__(self):
        self.parts = []
        
    def add_part(self, part):
        self.parts.append(part)
        
    def display(self):
        print("Workspace:")
        for part in self.parts:
            print(f"Part {part.shape}: {part.relationships}")
