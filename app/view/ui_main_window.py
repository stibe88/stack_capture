# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSlider, QSpinBox,
    QStatusBar, QToolButton, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(516, 561)
        icon = QIcon()
        icon.addFile(u"icon_stack_capture.jpg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.GB_camera_settings = QGroupBox(self.centralwidget)
        self.GB_camera_settings.setObjectName(u"GB_camera_settings")
        self.gridLayout = QGridLayout(self.GB_camera_settings)
        self.gridLayout.setObjectName(u"gridLayout")
        self.CB_aperture = QCheckBox(self.GB_camera_settings)
        self.CB_aperture.setObjectName(u"CB_aperture")
        self.CB_aperture.setChecked(True)

        self.gridLayout.addWidget(self.CB_aperture, 2, 0, 1, 1)

        self.L_shutter_speed = QLabel(self.GB_camera_settings)
        self.L_shutter_speed.setObjectName(u"L_shutter_speed")

        self.gridLayout.addWidget(self.L_shutter_speed, 1, 2, 1, 1)

        self.CB_iso = QCheckBox(self.GB_camera_settings)
        self.CB_iso.setObjectName(u"CB_iso")
        self.CB_iso.setChecked(True)

        self.gridLayout.addWidget(self.CB_iso, 3, 0, 1, 1)

        self.CB_shutter_speed = QCheckBox(self.GB_camera_settings)
        self.CB_shutter_speed.setObjectName(u"CB_shutter_speed")
        self.CB_shutter_speed.setChecked(True)

        self.gridLayout.addWidget(self.CB_shutter_speed, 1, 0, 1, 1)

        self.COB_iso = QComboBox(self.GB_camera_settings)
        self.COB_iso.setObjectName(u"COB_iso")

        self.gridLayout.addWidget(self.COB_iso, 3, 1, 1, 1)

        self.COB_aperture = QComboBox(self.GB_camera_settings)
        self.COB_aperture.setObjectName(u"COB_aperture")

        self.gridLayout.addWidget(self.COB_aperture, 2, 1, 1, 1)

        self.COB_shutter_speed = QComboBox(self.GB_camera_settings)
        self.COB_shutter_speed.setObjectName(u"COB_shutter_speed")

        self.gridLayout.addWidget(self.COB_shutter_speed, 1, 1, 1, 1)

        self.L_camera_name = QLabel(self.GB_camera_settings)
        self.L_camera_name.setObjectName(u"L_camera_name")

        self.gridLayout.addWidget(self.L_camera_name, 0, 0, 1, 1)

        self.LED_camera = QLineEdit(self.GB_camera_settings)
        self.LED_camera.setObjectName(u"LED_camera")
        self.LED_camera.setReadOnly(True)

        self.gridLayout.addWidget(self.LED_camera, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.GB_camera_settings, 0, 0, 1, 1)

        self.GB_focus = QGroupBox(self.centralwidget)
        self.GB_focus.setObjectName(u"GB_focus")
        self.gridLayout_4 = QGridLayout(self.GB_focus)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.HSL_focus = QSlider(self.GB_focus)
        self.HSL_focus.setObjectName(u"HSL_focus")
        self.HSL_focus.setEnabled(False)
        self.HSL_focus.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.HSL_focus, 1, 0, 1, 3)

        self.L_new_focus = QLabel(self.GB_focus)
        self.L_new_focus.setObjectName(u"L_new_focus")

        self.gridLayout_4.addWidget(self.L_new_focus, 2, 0, 1, 1)

        self.L_current_focus = QLabel(self.GB_focus)
        self.L_current_focus.setObjectName(u"L_current_focus")

        self.gridLayout_4.addWidget(self.L_current_focus, 2, 1, 1, 1)

        self.L_current_focus_2 = QLabel(self.GB_focus)
        self.L_current_focus_2.setObjectName(u"L_current_focus_2")

        self.gridLayout_4.addWidget(self.L_current_focus_2, 2, 2, 1, 1)

        self.LED_min_focus = QLineEdit(self.GB_focus)
        self.LED_min_focus.setObjectName(u"LED_min_focus")
        self.LED_min_focus.setEnabled(False)

        self.gridLayout_4.addWidget(self.LED_min_focus, 3, 0, 1, 1)

        self.LED_current_focus = QLineEdit(self.GB_focus)
        self.LED_current_focus.setObjectName(u"LED_current_focus")
        self.LED_current_focus.setEnabled(False)
        self.LED_current_focus.setReadOnly(True)

        self.gridLayout_4.addWidget(self.LED_current_focus, 3, 1, 1, 1)

        self.LED_max_focus = QLineEdit(self.GB_focus)
        self.LED_max_focus.setObjectName(u"LED_max_focus")
        self.LED_max_focus.setEnabled(False)
        self.LED_max_focus.setDragEnabled(False)
        self.LED_max_focus.setReadOnly(True)

        self.gridLayout_4.addWidget(self.LED_max_focus, 3, 2, 1, 1)

        self.PB_initialize_focus = QPushButton(self.GB_focus)
        self.PB_initialize_focus.setObjectName(u"PB_initialize_focus")

        self.gridLayout_4.addWidget(self.PB_initialize_focus, 0, 0, 1, 3)


        self.gridLayout_2.addWidget(self.GB_focus, 1, 0, 1, 1)

        self.GB_focus_stacker = QGroupBox(self.centralwidget)
        self.GB_focus_stacker.setObjectName(u"GB_focus_stacker")
        self.gridLayout_3 = QGridLayout(self.GB_focus_stacker)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.L_file_path = QLabel(self.GB_focus_stacker)
        self.L_file_path.setObjectName(u"L_file_path")

        self.gridLayout_3.addWidget(self.L_file_path, 0, 0, 1, 1)

        self.LE_file_path = QLineEdit(self.GB_focus_stacker)
        self.LE_file_path.setObjectName(u"LE_file_path")
        self.LE_file_path.setReadOnly(True)

        self.gridLayout_3.addWidget(self.LE_file_path, 0, 1, 1, 3)

        self.TB_file_path = QToolButton(self.GB_focus_stacker)
        self.TB_file_path.setObjectName(u"TB_file_path")

        self.gridLayout_3.addWidget(self.TB_file_path, 0, 4, 1, 1)

        self.L_name = QLabel(self.GB_focus_stacker)
        self.L_name.setObjectName(u"L_name")

        self.gridLayout_3.addWidget(self.L_name, 1, 0, 1, 1)

        self.LE_serie_name = QLineEdit(self.GB_focus_stacker)
        self.LE_serie_name.setObjectName(u"LE_serie_name")

        self.gridLayout_3.addWidget(self.LE_serie_name, 1, 1, 1, 4)

        self.L_focus_step = QLabel(self.GB_focus_stacker)
        self.L_focus_step.setObjectName(u"L_focus_step")

        self.gridLayout_3.addWidget(self.L_focus_step, 2, 0, 1, 1)

        self.SB_focus_change = QSpinBox(self.GB_focus_stacker)
        self.SB_focus_change.setObjectName(u"SB_focus_change")
        self.SB_focus_change.setMinimum(-32767)
        self.SB_focus_change.setMaximum(32767)
        self.SB_focus_change.setSingleStep(10)
        self.SB_focus_change.setValue(50)

        self.gridLayout_3.addWidget(self.SB_focus_change, 2, 1, 1, 1)

        self.L_number_images = QLabel(self.GB_focus_stacker)
        self.L_number_images.setObjectName(u"L_number_images")

        self.gridLayout_3.addWidget(self.L_number_images, 2, 2, 1, 1)

        self.SB_number_images = QSpinBox(self.GB_focus_stacker)
        self.SB_number_images.setObjectName(u"SB_number_images")
        self.SB_number_images.setMinimum(1)
        self.SB_number_images.setMaximum(200)
        self.SB_number_images.setValue(1)

        self.gridLayout_3.addWidget(self.SB_number_images, 2, 3, 1, 2)

        self.PB_capture = QPushButton(self.GB_focus_stacker)
        self.PB_capture.setObjectName(u"PB_capture")

        self.gridLayout_3.addWidget(self.PB_capture, 3, 0, 1, 5)


        self.gridLayout_2.addWidget(self.GB_focus_stacker, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Stack Capture", None))
        self.GB_camera_settings.setTitle(QCoreApplication.translate("MainWindow", u"Kameraeinstellungen", None))
        self.CB_aperture.setText(QCoreApplication.translate("MainWindow", u"Blende", None))
        self.L_shutter_speed.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.CB_iso.setText(QCoreApplication.translate("MainWindow", u"ISO", None))
        self.CB_shutter_speed.setText(QCoreApplication.translate("MainWindow", u"Belichtungszeit", None))
        self.L_camera_name.setText(QCoreApplication.translate("MainWindow", u"Kamera", None))
        self.GB_focus.setTitle(QCoreApplication.translate("MainWindow", u"Fokus", None))
        self.L_new_focus.setText(QCoreApplication.translate("MainWindow", u"Minimum", None))
        self.L_current_focus.setText(QCoreApplication.translate("MainWindow", u"Aktuell", None))
        self.L_current_focus_2.setText(QCoreApplication.translate("MainWindow", u"Maximum", None))
        self.LED_min_focus.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.PB_initialize_focus.setText(QCoreApplication.translate("MainWindow", u"Fokus-Initialisierung", None))
        self.GB_focus_stacker.setTitle(QCoreApplication.translate("MainWindow", u"Fokusserie", None))
        self.L_file_path.setText(QCoreApplication.translate("MainWindow", u"Ordnerpfad", None))
        self.TB_file_path.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.L_name.setText(QCoreApplication.translate("MainWindow", u"Name Bildserie", None))
        self.L_focus_step.setText(QCoreApplication.translate("MainWindow", u"Fokus\u00e4nderung", None))
        self.L_number_images.setText(QCoreApplication.translate("MainWindow", u"Anzahl Fotos", None))
        self.PB_capture.setText(QCoreApplication.translate("MainWindow", u"Aufnahme", None))
    # retranslateUi

