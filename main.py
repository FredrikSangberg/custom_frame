import sys,os
#from annotation_main import open_gui
#from sortfiles_main import sortfiles_gui
#from search_main import searchfiles_gui

from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget, QFrame, QColorDialog, QInputDialog
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtWidgets import (
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QListWidget,
    QAbstractItemView,
    QComboBox,
    QDialog,
    QLabel,
    QListWidgetItem,
    QCheckBox
)

from custom_frame import *

CSS = \
    {
        'QDialog':
            {
                'background-color': 'rgb(250,240,230)',
            },
        'QLineEdit':
            {
                'background':'rgb(200,200,200)',
            },
    }

def dictToCSS(dictionnary):
    stylesheet = ""
    for item in dictionnary:
        stylesheet += item + "\n{\n"
        for attribute in dictionnary[item]:
            stylesheet += "  " + attribute + ": " + dictionnary[item][attribute] + ";\n"
        stylesheet += "}\n"
    return stylesheet

class open_main_gui(QDialog):

    def __init__(self,parent=None, screen_height=1200):
        super(open_main_gui, self).__init__(parent)

        self.screen_height = screen_height

        self.tmp = custom_frame_dialog(screen_height=self.screen_height)
        self.tmp.setMinimumHeight(50)
        self.tmp.setMinimumWidth(50)
        self.tmp.move(100,100)
        self.tmp.setWindowTitle('This is a test GUI')
        self.tmp.set_titlebar_color('rgba(117,159,120,1)')
        self.tmp.set_frame_color('rgba(117,159,120,1)')
        self.tmp.set_win_main_color('rgba(79,79,79,1)')
        self.tmp.set_frame_width(3)
        self.tmp.set_mouse_resize_sensibility(10)
        self.tmp.show()

        month_rent = 1.0011594
        amort_rent_each_month = 1.001655
        total_loan = 3332000
        total_rent = 0
        for k in range(0,21):
            total_rent += total_loan*(month_rent-1)
            total_loan -= total_loan*(amort_rent_each_month-1)

        print(total_loan)
        print(total_rent)

        new_rent_from_now = 1.00042
        total_rent = 0
        total_rent_new = 0
        total_loan_new = total_loan-2000000
        for k in range(21,36):
            total_rent_new += total_loan_new*(new_rent_from_now-1)
            total_rent += total_loan*(month_rent-1)
            total_loan -= total_loan*(amort_rent_each_month-1)

        amortering = 2000000
        rent_each_month = 1.0024
        vinst_for_bank = amortering*(rent_each_month**15) - amortering
        vinst_for_bank = vinst_for_bank - total_rent



        # This folder is the root of all file storage
        self.ground_base_folder = r'F:\desktop\FileAnnotator\alla_filer'

        self.setStyleSheet(dictToCSS(CSS))

        min_btb_h = 50
        min_btn_w = 250
        css_ = """
            QPushButton {
                background-color: rgb(255,255,255); 
                border: 1px solid black;
                font-size: 20px;
            }
            QPushButton:hover {
                background-color: rgb(250,230,240); 
                color: rgb(0,0,0);
                font-size: 22px;
                border-color: rgb(150,100,120);
            }
        """

        self.titlebar_btn = QPushButton('Titlebar color')
        self.titlebar_btn.setMinimumHeight(min_btb_h)
        self.titlebar_btn.setMinimumWidth(min_btn_w)
        self.titlebar_btn.setDisabled(False)
        self.titlebar_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.titlebar_btn.setStyleSheet(css_)
        self.titlebar_btn.clicked.connect(self.select_titlebar_color)


        self.frame_col_btn = QPushButton('Frame color')
        self.frame_col_btn.setMinimumHeight(min_btb_h)
        self.frame_col_btn.setMinimumWidth(min_btn_w)
        self.frame_col_btn.setDisabled(False)
        self.frame_col_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.frame_col_btn.setStyleSheet("font-size: 20px;")
        self.frame_col_btn.setStyleSheet(css_)
        self.frame_col_btn.clicked.connect(self.select_frame_color)


        self.main_background_btn = QPushButton('Main background color')
        self.main_background_btn.setMinimumHeight(min_btb_h)
        self.main_background_btn.setMinimumWidth(min_btn_w)
        self.main_background_btn.setDisabled(False)
        self.main_background_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.main_background_btn.setStyleSheet(css_)
        self.main_background_btn.clicked.connect(self.select_main_color)

        self.framewidth_btn = QPushButton('Frame width')
        self.framewidth_btn.setMinimumHeight(min_btb_h)
        self.framewidth_btn.setMinimumWidth(min_btn_w)
        self.framewidth_btn.setDisabled(False)
        self.framewidth_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.framewidth_btn.setStyleSheet(css_)
        self.framewidth_btn.clicked.connect(self.set_frame_width)

        self.resize_senitivity_btn = QPushButton('Resize sensitivity')
        self.resize_senitivity_btn.setMinimumHeight(min_btb_h)
        self.resize_senitivity_btn.setMinimumWidth(min_btn_w)
        self.resize_senitivity_btn.setDisabled(False)
        self.resize_senitivity_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.resize_senitivity_btn.setStyleSheet(css_)
        self.resize_senitivity_btn.clicked.connect(self.set_resize_sensitivity)

        self.titlebar_lbl = QLineEdit('')
        self.frame_col_lbl = QLineEdit('')
        self.main_background_lbl = QLineEdit('')
        self.framewidth_lbl = QLineEdit('')
        self.resize_senitivity_lbl = QLineEdit('')



        all_layouts = QVBoxLayout()
        layout1 = QHBoxLayout()
        layout1.addWidget(self.titlebar_btn)
        layout1.addWidget(self.titlebar_lbl)
        layout2 = QHBoxLayout()
        layout2.addWidget(self.frame_col_btn)
        layout2.addWidget(self.frame_col_lbl)
        layout3 = QHBoxLayout()
        layout3.addWidget(self.main_background_btn)
        layout3.addWidget(self.main_background_lbl)
        layout4 = QHBoxLayout()
        layout4.addWidget(self.framewidth_btn)
        layout4.addWidget(self.framewidth_lbl)
        layout5 = QHBoxLayout()
        layout5.addWidget(self.resize_senitivity_btn)
        layout5.addWidget(self.resize_senitivity_lbl)

        all_buttons_layout = QVBoxLayout()
        all_buttons_layout.addLayout(layout1)
        all_buttons_layout.addLayout(layout2)
        all_buttons_layout.addLayout(layout3)
        all_buttons_layout.addLayout(layout4)
        all_buttons_layout.addLayout(layout5)

        # Add everything to the main layout:
        main_layout = QVBoxLayout()
        main_layout.addLayout(all_buttons_layout)

        self.setLayout(main_layout)

        self.setWindowTitle("This is a test GUI")
        self.setMinimumWidth(400)
        self.setMinimumHeight(500)

        self.annotation_window_exists = False
        self.sort_window_exists = False
        self.search_window_exists = False

        self.annotate_main_gui = False
        self.sort_main_gui = False
        self.search_main_gui = False

    def select_titlebar_color(self):
        color = QColorDialog.getColor().getRgb()
        self.tmp.set_titlebar_color('rgba('+str(color[0])+','+str(color[1])+','+str(color[2])+',1)')
        self.titlebar_lbl.setText("'" + 'rgba('+str(color[0])+','+str(color[1])+','+str(color[2])+',1)' + "'")

    def select_frame_color(self):
        color = QColorDialog.getColor().getRgb()
        self.tmp.set_frame_color('rgba('+str(color[0])+','+str(color[1])+','+str(color[2])+',1)')
        self.frame_col_lbl.setText("'" + 'rgba('+str(color[0])+','+str(color[1])+','+str(color[2])+',1)' + "'")

    def select_main_color(self):
        color = QColorDialog.getColor().getRgb()
        self.tmp.set_win_main_color('rgba('+str(color[0])+','+str(color[1])+','+str(color[2])+',1)')
        self.main_background_lbl.setText("'" + 'rgba('+str(color[0])+','+str(color[1])+','+str(color[2])+',1)' + "'")

    def set_frame_width(self):
        nr_pixels, ok = QInputDialog.getText(self, 'set frame width', 'Type nr pixels width:')
        if ok:
            try:
                nr_pixels = int(nr_pixels)
                self.tmp.set_frame_width(nr_pixels)
                self.framewidth_lbl.setText(str(nr_pixels))

            except:
                print('dfgh')
    def set_resize_sensitivity(self):
        nr_pixels, ok = QInputDialog.getText(self, 'set frame width', 'Type nr pixels width:')
        if ok:
            try:
                nr_pixels = int(nr_pixels)
                self.tmp.set_mouse_resize_sensibility(nr_pixels)
                self.resize_senitivity_lbl.setText(str(nr_pixels))
            except:
                print('dfgh')



if __name__ == '__main__':
    app = QApplication([])
    screen_resolution = app.desktop().screenGeometry()
    width, height = screen_resolution.width(), screen_resolution.height()
    gui = open_main_gui(screen_height = height)
    gui.show()
    sys.exit(app.exec_())