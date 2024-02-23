class Interaction:
    def __init__(self, substance: str, contrainte: str, com1: str) -> None:
        self.substance = substance
        self.contrainte = contrainte
        self.com1 = com1

    def __str__(self) -> str:
        return f"{self.substance} \n {self.contrainte} \n {self.com1}"
    
    def to_json(self) -> str:
        return f'{{"substance": "{self.substance}", "contrainte": "{self.contrainte}", "com1": "{self.com1}"}}'

class InteractionManager:
    def __init__(self, substance: str, com = "") -> None:
        self.subtance = substance
        self.com = com
        self.interactions = []

    def add_interaction(self, interaction: Interaction) -> None:
        self.interactions.append(interaction)

    def get_interactions(self) -> list:
        return self.interactions

    def to_json(self) -> str:
        interactions = "[" + ", ".join([i.to_json() for i in self.interactions]) + "]"
        return f'{{"subtance": "{self.subtance}", "com": "{self.com}", "interactions": {interactions}}}'
    
    def __str__(self) -> str:
        return f"{str(self.subtance)}\n{str(self.com)}\n {str(self.interactions)}"
