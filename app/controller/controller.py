import time

from PySide6.QtCore import QObject, Slot

import app.model.model
import app.camera_driver.camera_driver


Model = app.model.model.Model
CameraDriver = app.camera_driver.camera_driver.CameraDriver


class MainController(QObject):
    def __init__(self, model: Model):
        super().__init__()
        self._model = model
        self._camera = CameraDriver()
        self._model.camera_model = self._camera.camera_model
        self._model.shutter_speeds = self._camera.shutter_speed_choices
        self._model.apertures = self._camera.aperture_choices
        self._model.iso_speeds = self._camera.iso_choices
        self._model.maximum_number_images = 0

    def capture(self):
        if self._model.use_shutter_speed:
            self._camera.set_shutter_speed(self._model.shutter_speed)
        if self._model.use_aperture:
            self._camera.set_aperture(self._model.aperture)
        if self._model.use_iso_speed:
            self._camera.set_iso(self._model.iso_speed)
        self._camera.disable_autofocus()
        self._camera.change_live_view_modus(1)

        for i in range(self._model.number_images):
            self._camera.enable_viewfinder()
            if i > 0:
                self._camera.change_focus(self._model.focus_change)
                self._model.current_focus += self._model.focus_change
            self._camera.capture_and_save_photo(
                file_path=(
                    f"{self._model.folder_path}/"
                    f"{self._model.image_series_name}_{i}.jpg"
                )
            )
            time.sleep(0.1)

        self._camera.disable_viewfinder()
        self._camera.change_live_view_modus(0)

    def initialize_focus(self):
        self._camera.initialize_focus()
        self._model.maximum_focus = self._camera.maximum_focus
        self._model.minimum_focus = 0
        self._model.current_focus = self._camera.current_focus
        self.focus_change(self._model.focus_change)

    @Slot(int)
    def focus_change(self, value):
        self._model.focus_change = value
        if value == 0:
            max_img = 999
        elif value > 0:
            max_img = (
                self._model.maximum_focus - self._model.current_focus
            ) // value
        else:
            max_img = -self._model.current_focus // value
        self._model.maximum_number_images = max_img

    @Slot(int)
    def number_images_change(self, value):
        self._model.number_images = value

    @Slot(str)
    def shutter_speed_change(self, value):
        self._model.shutter_speed = value

    @Slot(str)
    def aperture_change(self, value):
        self._model.aperture = value

    @Slot(str)
    def iso_speed_change(self, value):
        self._model.iso_speed = value

    @Slot(str)
    def image_series_name_change(self, value):
        self._model.image_series_name = value

    @Slot(bool)
    def use_shutter_speed_change(self, value):
        self._model.use_shutter_speed = value

    @Slot(bool)
    def use_aperture_change(self, value):
        self._model.use_aperture = value

    @Slot(bool)
    def use_iso_speed_change(self, value):
        self._model.use_iso_speed = value
