class Task:
    def __init__(self, id, title, description, is_completed=False) -> None:
        self.id = id 
        self.title = title 
        self.description = description
        self.is_completed = is_completed
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "is_completed": self.is_completed
        }