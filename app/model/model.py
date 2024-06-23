from PySide6.QtCore import QObject, Signal, Qt


class Model(QObject):
    camera_model_changed = Signal(str)
    _camera_model: str = ""
    shutter_speed_changed = Signal(str)
    _shutter_speed: str = ""
    shutter_speeds_changed = Signal(list)
    _shutter_speeds: list = []
    use_shutter_speed_changed = Signal(bool)
    _use_shutter_speed: bool = True
    apertures_changed = Signal(list)
    _apertures: list = []
    aperture_changed = Signal(str)
    _aperture: str = ""
    use_aperture_changed = Signal(bool)
    _use_aperture: bool = True
    iso_speed_changed = Signal(str)
    _iso_speed: str = ""
    iso_speeds_changed = Signal(list)
    _iso_speeds: list = []
    use_iso_speed_changed = Signal(bool)
    _use_iso_speed: bool = True
    minimum_focus_changed = Signal(int)
    _minimum_focus: int = 0
    current_focus_changed = Signal(int)
    _current_focus: int = 0
    maximum_focus_changed = Signal(int)
    _maximum_focus: int = 0
    folder_path_changed = Signal(str)
    _folder_path: str = ""
    image_series_name_changed = Signal(str)
    _image_series_name: str = ""
    focus_change_changed = Signal(int)
    _focus_change: int = 0
    number_images_changed = Signal(int)
    _number_images: int = 0
    maximum_number_images_changed = Signal(int)
    _maximum_number_images: int = 0
    message_changed = Signal(dict)
    _message: dict = {}

    @property
    def camera_model(self) -> str:
        return self._camera_model

    @camera_model.setter
    def camera_model(self, value: str) -> None:
        self._camera_model = value
        self.camera_model_changed.emit(value)

    @property
    def shutter_speed(self) -> str:
        return self._shutter_speed

    @shutter_speed.setter
    def shutter_speed(self, value: str) -> None:
        self._shutter_speed = value
        self.shutter_speed_changed.emit(value)

    @property
    def shutter_speeds(self) -> list:
        return self._shutter_speeds

    @shutter_speeds.setter
    def shutter_speeds(self, value: list) -> None:
        self._shutter_speeds = value
        self.shutter_speeds_changed.emit(value)

    @property
    def use_shutter_speed(self) -> bool:
        return self._use_shutter_speed

    @use_shutter_speed.setter
    def use_shutter_speed(self, value: Qt.CheckState) -> None:
        self._use_shutter_speed = value.value
        self.use_shutter_speed_changed.emit(value.value)

    @property
    def aperture(self) -> str:
        return self._aperture

    @aperture.setter
    def aperture(self, value: str) -> None:
        self._aperture = value
        self.aperture_changed.emit(value)

    @property
    def apertures(self) -> list:
        return self._apertures

    @apertures.setter
    def apertures(self, value: list) -> None:
        self._apertures = value
        self.apertures_changed.emit(value)

    @property
    def use_aperture(self) -> bool:
        return self._use_aperture

    @use_aperture.setter
    def use_aperture(self, value: Qt.CheckState) -> None:
        self._use_aperture = value.value
        self.use_aperture_changed.emit(value.value)

    @property
    def iso_speed(self) -> str:
        return self._iso_speed

    @iso_speed.setter
    def iso_speed(self, value: str) -> None:
        self._iso_speed = value
        self.iso_speed_changed.emit(value)

    @property
    def iso_speeds(self) -> list:
        return self._iso_speeds

    @iso_speeds.setter
    def iso_speeds(self, value: list) -> None:
        self._iso_speeds = value
        self.iso_speeds_changed.emit(value)

    @property
    def use_iso_speed(self) -> bool:
        return self._use_iso_speed

    @use_iso_speed.setter
    def use_iso_speed(self, value: Qt.CheckState) -> None:
        self._use_iso_speed = value.value
        self.use_iso_speed_changed.emit(value.value)

    @property
    def minimum_focus(self) -> int:
        return self._minimum_focus

    @minimum_focus.setter
    def minimum_focus(self, value: int) -> None:
        self._minimum_focus = value
        self.minimum_focus_changed.emit(value)

    @property
    def current_focus(self) -> int:
        return self._current_focus

    @current_focus.setter
    def current_focus(self, value: int) -> None:
        self._current_focus = value
        self.current_focus_changed.emit(value)

    @property
    def maximum_focus(self) -> int:
        return self._maximum_focus

    @maximum_focus.setter
    def maximum_focus(self, value: int) -> None:
        self._maximum_focus = value
        self.maximum_focus_changed.emit(value)

    @property
    def folder_path(self) -> str:
        return self._folder_path

    @folder_path.setter
    def folder_path(self, value: str) -> None:
        self._folder_path = value
        self.folder_path_changed.emit(value)

    @property
    def image_series_name(self) -> str:
        return self._image_series_name

    @image_series_name.setter
    def image_series_name(self, value: str) -> None:
        self._image_series_name = value
        self.image_series_name_changed.emit(value)

    @property
    def focus_change(self) -> int:
        return self._focus_change

    @focus_change.setter
    def focus_change(self, value: int) -> None:
        self._focus_change = value
        self.focus_change_changed.emit(value)

    @property
    def number_images(self) -> int:
        return self._number_images

    @number_images.setter
    def number_images(self, value: int) -> None:
        self._number_images = value
        self.number_images_changed.emit(value)

    @property
    def maximum_number_images(self) -> int:
        return self._maximum_number_images

    @maximum_number_images.setter
    def maximum_number_images(self, value: int) -> None:
        self._maximum_number_images = value
        self.maximum_number_images_changed.emit(value)

    @property
    def message(self) -> dict:
        return self._message

    @message.setter
    def message(self, value: dict) -> None:
        self._message = value
        self.message_changed.emit(value)
