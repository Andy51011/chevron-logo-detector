import sys
from detector_ui import DetectorUi
from PyQt6.QtWidgets import QApplication
from process_image import ProcessImage
from detector_controller import DetectorController


def main():
    app = QApplication([])
    detector_ui = DetectorUi()
    process_img = ProcessImage()
    detector_ui.show()
    detector_controller = DetectorController(model=process_img, view=detector_ui)
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
