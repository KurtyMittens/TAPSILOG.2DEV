import folium
import io
from PyQt5 import QtWidgets, QtWebEngineWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView


class JavaScriptMaps(QtWidgets.QWidget):
    def __init__(self, frame):
        super().__init__()
        self.coordinate = (14.625780006444936, 121.06172716017973)
        # MY HOUSE = 14.6660256, 121.1405483
        # TIP QC = 14.625780006444936, 121.06172716017973
        self.map = folium.Map(
            tiles="https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}",
            attr="Google",
            name="Google Satellite",
            overlay=False,
            control=True,
            location=self.coordinate,
            zoom_start=17
        )

        # save map data to data object
        data = io.BytesIO()
        self.map.save(data, close_file=False)

        self.webView = QWebEngineView()
        self.webView.setHtml(data.getvalue().decode())

        frame.addWidget(self.webView)
