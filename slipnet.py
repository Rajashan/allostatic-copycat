class Slipnet:
    def __init__(self):
        self.nodes = {}
        self.links = {}
        
        # Create nodes for each concept
        self.add_node("letter similarity", 1)
        self.add_node("direction", 1)
        self.add_node("speed", 1)
        self.add_node("structure", 1)
        self.add_node("pattern", 1)
        
        # Create links between related concepts
        self.add_link("letter similarity", "structure", 1)
        self.add_link("letter similarity", "pattern", 1)
        self.add_link("direction", "pattern", 1)
        self.add_link("speed", "pattern", 1)
        self.add_link("structure", "pattern", 1)
        
    def add_node(self, name, activation):
        self.nodes[name] = {
            "activation": activation
        }
        
    def add_link(self, from_node, to_node, strength):
        if from_node not in self.links:
            self.links[from_node] = {}
        self.links[from_node][to_node] = strength
    
    def activate(self, concept, amount):
        self.nodes[concept]["activation"] += amount
    
    def spread_activation(self, concept, amount):
        self.activate(concept, amount)
        for to_node, strength in self.links[concept].items():
            self.activate(to_node, amount * strength)
            
    def get_activation(self, concept):
        return self.nodes[concept]["activation"]


