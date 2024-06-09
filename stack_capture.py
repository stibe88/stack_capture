import sys
import os
import time
import camera_driver

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtCore import QFile, Qt
from PySide6.QtUiTools import QUiLoader


class MainWindow(QMainWindow):
    w = None
    camera_driver = None

    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.load_ui()

    def load_ui(self) -> None:
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "stack_capture.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        self.w = loader.load(ui_file, self)
        ui_file.close()
        try:
            self.camera_driver = camera_driver.CameraDriver()
            self.w.LED_camera.setText(self.camera_driver.camera_model)
        except Exception as e:
            QMessageBox.critical(
                self.w,
                "Wrong camera model",
                str(e)
            )

        self.w.COB_shutter_speed.addItems(self.camera_driver.shutter_speed_choices)
        self.w.COB_aperture.addItems(self.camera_driver.aperture_choices)
        self.w.COB_iso.addItems(self.camera_driver.iso_choices)
        self.w.PB_capture.clicked.connect(self.capture)
        self.w.TB_file_path.clicked.connect(self.folder_dialog)
        self.w.PB_initialize_focus.clicked.connect(self.initialize_focus)
        self.w.SB_focus_change.valueChanged.connect(self.new_focus_change)

    def folder_dialog(self):
        folder_name = QFileDialog.getExistingDirectory(
            parent=self,
            caption="Bitte Ordner auswählen",
            options=QFileDialog.Option.ShowDirsOnly,
        )
        if folder_name != 1:
            self.w.LE_file_path.setText(folder_name)

    def initialize_focus(self):
        self.camera_driver.initialize_focus()
        self.w.LED_max_focus.setDisabled(False)
        self.w.LED_max_focus.setText(
            str(self.camera_driver.maximum_focus)
        )
        self.w.LED_current_focus.setDisabled(False)
        self.w.LED_current_focus.setText(
            str(self.camera_driver.current_focus)
        )
        self.w.LED_min_focus.setDisabled(False)
        self.w.LED_min_focus.setText(str(0))
        self.w.HSL_focus.setMaximum(self.camera_driver.maximum_focus)
        self.w.HSL_focus.setValue(self.camera_driver.current_focus)
        self.new_focus_change()

    def new_focus_change(self):
        focus_change = self.w.SB_focus_change.value()
        current_focus = self.camera_driver.current_focus
        maximum_focus = self.camera_driver.maximum_focus
        if focus_change == 0:
            number_images = 999
        elif focus_change > 0:
            number_images = maximum_focus // focus_change
        else:
            number_images = -current_focus // focus_change
        self.w.SB_number_images.setMaximum(number_images)

    def capture(self):
        folder_path = self.w.LE_file_path.text()
        name = self.w.LE_serie_name.text()
        focus_change = self.w.SB_focus_change.value()
        number_images = self.w.SB_number_images.value()

        shutter_speed = str(self.w.COB_shutter_speed.currentText())
        aperture = str(self.w.COB_aperture.currentText())
        iso = str(self.w.COB_iso.currentText())

        camera = self.camera_driver
        if self.w.CB_shutter_speed.isChecked():
            camera.set_shutter_speed(shutter_speed)
        if self.w.CB_aperture.isChecked():
            camera.set_aperture(aperture)
        if self.w.CB_iso.isChecked():
            camera.set_iso(iso)
        camera.disable_autofocus()
        camera.change_live_view_modus(1)
        camera.enable_viewfinder()

        for i in range(number_images):
            camera.change_focus(focus_change)
            camera.current_focus += focus_change
            self.w.LED_current_focus.setText(
                str(self.camera_driver.current_focus)
            )
            self.w.HSL_focus.setValue(self.camera_driver.current_focus)
            camera.capture_and_save_photo(f'{folder_path}/{name}_{i}.jpg')
            time.sleep(0.1)
            camera.enable_viewfinder()

        camera.disable_viewfinder()
        camera.change_live_view_modus(0)


if __name__ == "__main__":
    QApplication.setAttribute(Qt.ApplicationAttribute.AA_ShareOpenGLContexts)
    app = QApplication([])
    widget = MainWindow()
    widget.w.show()
    del widget.camera_driver
    sys.exit(app.exec())
