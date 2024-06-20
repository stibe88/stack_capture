import sys
from PySide6.QtWidgets import QApplication, QMessageBox, QWidget

import app.model.model
import app.view.main_view
import app.controller.controller


Model = app.model.model.Model
MainController = app.controller.controller.MainController
MainView = app.view.main_view.MainView


class StackCaptureApp(QApplication):
    def __init__(self, sys_argv):
        super(StackCaptureApp, self).__init__(sys_argv)
        try:
            self.model = Model()
            self.main_controller = MainController(self.model)
            self.main_view = MainView(self.model, self.main_controller)
            self.main_view.show()
        except Exception as e:
            QMessageBox.critical(
                QWidget(),
                f"{type(e).__name__}",
                f"{e}"
            )


if __name__ == "__main__":
    stack_capture_app = StackCaptureApp(sys.argv)
    sys.exit(stack_capture_app.exec())
