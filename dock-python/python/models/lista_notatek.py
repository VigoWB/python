class ListaNotatek:
    def __init__(self, id: int):
        self.id = id
        self.title: str = ''
        self.created_at: str = "2020-05-02 10:00:00"
        self.updated_at: str = "2023-09-15 15:22:33"
        self.pin = True
        self.color: str = 'red'
        pass

    def response(self):
        return {
            "id": self.id,
            "title": self.title,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "pin": self.pin,
            "color": self.color,
        }
