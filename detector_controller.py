class DetectorController:

    def __init__(self, model, view):
        self._imgProcess = model
        self._view = view
        self._connectButtons()

    def _process_images(self):
        user_path = self._view.getDirectory()
        self._imgProcess.directory = user_path
        self._imgProcess.detect_logos()
        self._imgProcess.filter_img()

    def _closeApp(self):
        self._view.close()

    def _connectButtons(self):
        self._view.startBtn.clicked.connect(self._process_images)
        self._view.cancelBtn.clicked.connect(self._closeApp)
