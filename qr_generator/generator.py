import time
import qrcode
from database import ICE
from database import tapsi_sql


class GenerateQR:
    def __init__(self):
        self.eyes = ICE.ICE()
        self.sql = tapsi_sql.TapsilogSql()
        self.homeowners = self.sql.show_homeowners_wICE()
        self.today_date = time.strftime("%m-%d-%Y")

    def generate(self):
        for index, array in enumerate(self.homeowners):
                file = f"{array[0]},{array[1]},{self.eyes.encode(self.today_date)}"
                img = qrcode.make(file)
                img.save(f"qr_generator/qr_homeowner/trial{self.eyes.decode(array[1])}.png")

