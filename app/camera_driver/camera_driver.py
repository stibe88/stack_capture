import os
import yaml
import time

import gphoto2 as gp


class CameraDriver(object):
    maximum_focus: int = 0
    current_focus: int = 0
    command_sets_file_name: str = "camera_command_sets.yml"

    def __init__(self):
        os.popen("pkill -f gphoto2")
        self.context = gp.Context()
        self.camera = gp.Camera()
        self.camera.init(self.context)
        abilities = self.camera.get_abilities()
        self.camera_model = abilities.model
        self.command_set = self._get_camera_command_set(
            command_sets_file_path=self.command_sets_file_path,
            camera_model=self.camera_model
        )

    def __del__(self):
        self.camera.exit(self.context)

    def _work_around(self):
        self.camera.exit(self.context)
        os.popen("gphoto2 --capture-movie=1s")
        time.sleep(3)
        os.popen("pkill -f gphoto2")
        self.camera.init(self.context)

    @property
    def command_sets_file_path(self) -> str:
        folder_path = os.path.dirname(
            os.path.abspath(__file__)
        )
        return os.path.join(folder_path, self.command_sets_file_name)

    @property
    def summary_as_text(self) -> str:
        return str(self.camera.get_summary(self.context))

    @property
    def iso_choices(self) -> list:
        command = self.command_set["iso"]["command"]
        return self._choices_list(
            self.camera.get_single_config(command, self.context)
        )

    @property
    def shutter_speed_choices(self) -> list:
        command = self.command_set["shutter_speed"]["command"]
        return self._choices_list(
            self.camera.get_single_config(command, self.context)
        )

    @property
    def aperture_choices(self) -> list:
        command = self.command_set["aperture"]["command"]
        return self._choices_list(
            self.camera.get_single_config(command, self.context)
        )

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

    def change_live_view_modus(self, choice: int) -> None:
        command_set = self.command_set["change_live_view_modus"]
        command_set["value"] = choice
        self._change_single_config(**command_set)

    def enable_viewfinder(self) -> None:
        command_set = self.command_set["enable_viewfinder"]
        try:
            self._change_single_config(**command_set)
        except gp.GPhoto2Error:
            self._work_around()
            self.enable_viewfinder()

    def disable_viewfinder(self) -> None:
        command_set = self.command_set["disable_viewfinder"]
        self._change_single_config(**command_set)

    def disable_autofocus(self) -> None:
        command_set = self.command_set["disable_autofocus"]
        self._change_single_config(**command_set)

    def set_iso(self, value: str) -> None:
        command_set = self.command_set["iso"]
        command_set["value"] = value
        self._change_single_config(**command_set)

    def set_aperture(self, value: str) -> None:
        command_set = self.command_set["aperture"]
        command_set["value"] = value
        self._change_single_config(**command_set)

    def set_shutter_speed(self, value: str) -> None:
        command_set = self.command_set["shutter_speed"]
        command_set["value"] = value
        self._change_single_config(**command_set)

    def change_focus(self, change_value: int) -> None:
        command_set = self.command_set["change_focus"]
        command_set["value"] = change_value
        self._change_single_config(**command_set)

    def capture_and_save_photo(self, file_path: str) -> None:
        camera_path = self.camera.capture(
            gp.GP_CAPTURE_IMAGE,
            self.context,
        )
        camera_file = self.camera.file_get(
            camera_path.folder,
            camera_path.name,
            gp.GP_FILE_TYPE_NORMAL,
            None,
            self.context
        )
        camera_file.save(file_path)

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

    def _change_single_config(
        self,
        command: str,
        datatype: str,
        value: str | int | float | bool | None
    ) -> None:
        configuration = self.camera.get_single_config(
            command,
            self.context,
        )
        configuration.set_value(
            self._convert_data_type(
                datatype,
                value,
            )
        )
        self.camera.set_single_config(
            command,
            configuration,
            self.context,
        )

    @staticmethod
    def _choices_list(config: gp.CameraWidget) -> list:
        return [
            config.get_choice(idx) for idx
            in range(config.count_choices())
        ]

    @staticmethod
    def _get_camera_command_set(
        command_sets_file_path: str,
        camera_model: str
    ) -> dict:
        with open(file=command_sets_file_path, mode="r") as f:
            content = yaml.full_load(f)
            command_sets = content["Camera Command Sets"]
        try:
            return next(
                cs for cs in command_sets
                if cs["model"] == camera_model
            )
        except StopIteration:
            cameras_supported = *(
                cs["model"] for cs in command_sets
            ),
            raise NotImplementedError(
                f"Camera model {camera_model} is not supported. "
                f"Supported camera models: {cameras_supported}."
            )

    @staticmethod
    def _convert_data_type(
        datatype: str,
        value: str | int | float | bool | None
    ) -> str | int | float | bool | None:
        match datatype:
            case "string":
                return str(value)
            case "integer":
                return int(value)
            case "float":
                return float(value)
            case "bool":
                return bool(value)
            case _:
                return None
