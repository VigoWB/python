import time
import datetime
import zoneinfo

class ListaNotatek:
    def __init__(self):
        self.id = 0
        self.title: str = ''
        self.created_at: str = "2020-05-02 10:00:00"
        self.updated_at: str = "2023-09-15 15:22:33"
        self.pin = True
        self.color: str = 'red'
        self.timestamp = time.time()

    def set_timestamp(self):
        self.timestamp = time.time()

    def czytelna_data(self):
        dt = datetime.datetime.fromtimestamp(self.timestamp, tz=zoneinfo.ZoneInfo("Europe/Warsaw"))
        return dt.strftime("%Y-%m-%d %H:%M:%S %Z")

    def response(self):
        return {
            "id": self.id,
            "title": self.title,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "pin": self.pin,
            "color": self.color,
            "timestamp": self.timestamp,
            "ludzka_godzina": self.czytelna_data()
        }
