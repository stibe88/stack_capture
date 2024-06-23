from PySide6.QtWidgets import QMainWindow, QFileDialog
from PySide6.QtCore import Slot

import app.view.ui_main_window
import app.model.model
import app.controller.controller


UiMainWindow = app.view.ui_main_window.Ui_MainWindow
Model = app.model.model.Model
Controller = app.controller.controller.MainController


class MainView(QMainWindow):
    def __init__(self, model: Model, controller: Controller):
        super().__init__()
        self._model = model
        self._controller = controller
        self._ui = UiMainWindow()
        self._ui.setupUi(self)

        # buttons
        self._ui.PB_capture.clicked.connect(
            self._controller.capture
        )
        self._ui.TB_file_path.clicked.connect(
            self.folder_dialog
        )
        self._ui.PB_initialize_focus.clicked.connect(
            self._controller.initialize_focus
        )

        # spin boxes
        self._ui.SB_focus_change.valueChanged.connect(
            self._controller.focus_change
        )
        self._ui.SB_number_images.valueChanged.connect(
            self._controller.number_images_change
        )

        # combo boxes
        self._ui.COB_shutter_speed.currentTextChanged.connect(
            self._controller.shutter_speed_change
        )
        self._ui.COB_aperture.currentTextChanged.connect(
            self._controller.aperture_change
        )
        self._ui.COB_iso.currentTextChanged.connect(
            self._controller.iso_speed_change
        )

        # line edits
        self._ui.LE_serie_name.textChanged.connect(
            self._controller.image_series_name_change
        )

        # check boxes
        self._ui.CB_shutter_speed.checkStateChanged.connect(
            self._controller.use_shutter_speed_change
        )
        self._ui.CB_aperture.checkStateChanged.connect(
            self._controller.use_aperture_change
        )
        self._ui.CB_iso.checkStateChanged.connect(
            self._controller.use_iso_speed_change
        )

        # apply model changes
        self._model.camera_model_changed.connect(
            self.camera_model_changed
        )
        self._model.shutter_speed_changed.connect(
            self.shutter_speed_changed
        )
        self._model.shutter_speeds_changed.connect(
            self.shutter_speeds_changed
        )
        self._model.use_shutter_speed_changed.connect(
            self.use_shutter_speed_changed
        )
        self._model.aperture_changed.connect(
            self.aperture_changed
        )
        self._model.apertures_changed.connect(
            self.apertures_changed
        )
        self._model.use_aperture_changed.connect(
            self.use_aperture_changed
        )
        self._model.iso_speed_changed.connect(
            self.iso_speed_changed
        )
        self._model.iso_speeds_changed.connect(
            self.iso_speeds_changed
        )
        self._model.use_iso_speed_changed.connect(
            self.use_iso_speed_changed
        )
        self._model.minimum_focus_changed.connect(
            self.minimum_focus_changed
        )
        self._model.current_focus_changed.connect(
            self.current_focus_changed
        )
        self._model.maximum_focus_changed.connect(
            self.maximum_focus_changed
        )
        self._model.folder_path_changed.connect(
            self.folder_path_changed
        )
        self._model.image_series_name_changed.connect(
            self.image_series_name_changed
        )
        self._model.focus_change_changed.connect(
            self.focus_change_changed
        )
        self._model.number_images_changed.connect(
            self.number_images_changed
        )
        self._model.maximum_number_images_changed.connect(
            self.maximum_number_images_changed
        )

        # set initial values
        self.camera_model_changed(self._model.camera_model)
        self.shutter_speeds_changed(self._model.shutter_speeds)
        self.apertures_changed(self._model.apertures)
        self.iso_speeds_changed(self._model.iso_speeds)
        self.maximum_number_images_changed(self._model.number_images)

    def folder_dialog(self) -> None:
        folder_path = QFileDialog.getExistingDirectory(
            parent=self,
            caption="Bitte Ordner auswählen",
            options=QFileDialog.Option.ShowDirsOnly,
        )
        if folder_path != -1:
            self._model.folder_path = folder_path

    @Slot(str)
    def camera_model_changed(self, value: str) -> None:
        self._ui.LED_camera.setText(value)

    @Slot(str)
    def shutter_speed_changed(self, value: str) -> None:
        self._ui.COB_shutter_speed.setCurrentText(value)

    @Slot(list)
    def shutter_speeds_changed(self, value: list) -> None:
        while self._ui.COB_shutter_speed.count():
            self._ui.COB_shutter_speed.removeItem(0)
        self._ui.COB_shutter_speed.addItems(value)

    @Slot(bool)
    def use_shutter_speed_changed(self, value: bool) -> None:
        self._ui.CB_shutter_speed.setChecked(value)
        self._ui.COB_shutter_speed.setEnabled(value)
        self.shutter_speeds_changed(
            self._model.shutter_speeds if value else []
        )

    @Slot(int)
    def aperture_changed(self, value: str) -> None:
        self._ui.COB_aperture.setCurrentText(value)

    @Slot(list)
    def apertures_changed(self, value: list) -> None:
        while self._ui.COB_aperture.count():
            self._ui.COB_aperture.removeItem(0)
        self._ui.COB_aperture.addItems(value)

    @Slot(bool)
    def use_aperture_changed(self, value: bool) -> None:
        self._ui.CB_aperture.setChecked(value)
        self._ui.COB_aperture.setEnabled(value)
        self.apertures_changed(
            self._model.apertures if value else []
        )

    @Slot(int)
    def iso_speed_changed(self, value: str) -> None:
        self._ui.COB_iso.setCurrentText(value)

    @Slot(list)
    def iso_speeds_changed(self, value: list) -> None:
        while self._ui.COB_iso.count():
            self._ui.COB_iso.removeItem(0)
        self._ui.COB_iso.addItems(value)

    @Slot(bool)
    def use_iso_speed_changed(self, value: bool) -> None:
        self._ui.CB_iso.setChecked(value)
        self._ui.COB_iso.setEnabled(value)
        self.iso_speeds_changed(
            self._model.iso_speeds if value else []
        )

    @Slot(int)
    def minimum_focus_changed(self, value: int) -> None:
        self._ui.LED_min_focus.setDisabled(False)
        self._ui.LED_min_focus.setText(str(value))
        self._ui.HSL_focus.setMinimum(value)

    @Slot(int)
    def current_focus_changed(self, value: int) -> None:
        self._ui.LED_current_focus.setDisabled(False)
        self._ui.LED_current_focus.setText(str(value))
        self._ui.HSL_focus.setValue(value)

    @Slot(int)
    def maximum_focus_changed(self, value: int) -> None:
        self._ui.LED_max_focus.setDisabled(False)
        self._ui.LED_max_focus.setText(str(value))
        self._ui.HSL_focus.setMaximum(value)

    @Slot(str)
    def folder_path_changed(self, value: str) -> None:
        self._ui.LE_file_path.setText(value)

    @Slot(str)
    def image_series_name_changed(self, value: str) -> None:
        self._ui.LE_serie_name.setText(value)

    @Slot(int)
    def focus_change_changed(self, value: int) -> None:
        self._ui.SB_focus_change.setValue(value)

    @Slot(int)
    def number_images_changed(self, value: int) -> None:
        self._ui.SB_number_images.setValue(value)
        if value == 0:
            self._ui.PB_capture.setEnabled(False)
        else:
            self._ui.PB_capture.setEnabled(True)

    @Slot(int)
    def maximum_number_images_changed(self, value: int) -> None:
        self._ui.SB_number_images.setMaximum(value)
