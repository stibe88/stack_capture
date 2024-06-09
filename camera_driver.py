import os

import time

import gphoto2 as gp


class CameraDriver(object):
    maximum_focus: int = 0
    current_focus: int = 0

    def __init__(self):
        os.popen("gphoto2 --capture-movie=1s")
        time.sleep(3)
        os.popen("pkill -f gphoto2")  # noqa
        self.context = gp.Context()
        self.camera = gp.Camera()
        self.camera.init(self.context)
        abilities = self.camera.get_abilities()
        self.camera_model = abilities.model
        if abilities.model != "Nikon DSC D300s (PTP mode)":
            raise ValueError(
                f"Camera model {abilities.model} is not supported."
                f"supported camera models:\n"
                f"Nikon DSC D300s (PTP mode)"
            )

    def __del__(self):
        self.camera.exit(self.context)

    @property
    def summary_as_text(self) -> str:
        return str(self.camera.get_summary(self.context))

    @property
    def iso_choices(self) -> list:
        return self._choices_list(
            self.camera.get_single_config("iso", self.context)
        )

    @property
    def shutter_speed_choices(self) -> list:
        return self._choices_list(
            self.camera.get_single_config("shutterspeed2", self.context)
        )

    @property
    def aperture_choices(self) -> list:
        return self._choices_list(
            self.camera.get_single_config("f-number", self.context)
        )

    @staticmethod
    def _choices_list(config: gp.CameraWidget) -> list:
        return [
            config.get_choice(idx) for idx
            in range(config.count_choices())
        ]

    def _get_max_focus_change(
        self,
        step: int = 50,
        change_limit: int = 32767,
    ) -> int:
        changed_focus = 0
        try:
            while abs(changed_focus) < change_limit:
                self.change_focus(step)
                changed_focus += step
        except gp.GPhoto2Error:
            return changed_focus
        return 0

    def initialize_focus(self, step: int = 50) -> None:
        self.disable_autofocus()
        self.change_live_view_modus(1)
        self.enable_viewfinder()
        self.current_focus = -self._get_max_focus_change(-step)
        self.maximum_focus = self._get_max_focus_change(step)
        to_original_focus = -self.maximum_focus + self.current_focus
        self.change_focus(to_original_focus)
        self.disable_viewfinder()
        self.change_live_view_modus(0)

    def change_live_view_modus(self, choice: int):
        d1a0 = self.camera.get_single_config("d1a0", self.context)
        d1a0.set_value(str(choice))
        self.camera.set_single_config("d1a0", d1a0, self.context)

    def enable_viewfinder(self):
        view_finder = self.camera.get_single_config("viewfinder", self.context)
        view_finder.set_value(1)
        self.camera.set_single_config("viewfinder", view_finder, self.context)

    def disable_viewfinder(self):
        view_finder = self.camera.get_single_config("viewfinder", self.context)
        view_finder.set_value(0)
        self.camera.set_single_config("viewfinder", view_finder, self.context)

    def disable_autofocus(self):
        auto_focus = self.camera.get_single_config("autofocus", self.context)
        auto_focus.set_value("Aus")
        self.camera.set_single_config("autofocus", auto_focus, self.context)

    def set_iso(self, value: str):
        iso = self.camera.get_single_config("iso", self.context)
        iso.set_value(value)
        self.camera.set_single_config("iso", iso, self.context)

    def set_aperture(self, value: str):
        aperture = self.camera.get_single_config("f-number", self.context)
        aperture.set_value(value)
        self.camera.set_single_config("f-number", aperture, self.context)

    def set_shutter_speed(self, value: str):
        shutter_speed = self.camera.get_single_config("shutterspeed2", self.context)
        shutter_speed.set_value(value)
        self.camera.set_single_config("shutterspeed2", shutter_speed, self.context)

    def change_focus(self, change_value: int):
        manual_focus_drive = self.camera.get_single_config("manualfocusdrive", self.context)
        manual_focus_drive.set_value(change_value)
        self.camera.set_single_config("manualfocusdrive", manual_focus_drive, self.context)

    def capture_and_save_photo(self, file_path: str) -> None:
        camera_path = self.camera.capture(gp.GP_CAPTURE_IMAGE, self.context)
        camera_file = self.camera.file_get(
            camera_path.folder,
            camera_path.name,
            gp.GP_FILE_TYPE_NORMAL,
            None,
            self.context
        )
        camera_file.save(file_path)
