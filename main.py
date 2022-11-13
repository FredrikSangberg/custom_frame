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
        self.tmp.setMinimumHeight(250)
        self.tmp.setMinimumWidth(350)
        self.tmp.move(100,100)
        self.tmp.setWindowTitle('This is a test GUI')
        self.tmp.set_titlebar_color('rgba(117,159,120,1)')
        self.tmp.set_frame_color('rgba(117,159,120,1)')
        self.tmp.set_win_main_color('rgba(79,79,79,1)')
        self.tmp.set_frame_width(3)
        self.tmp.set_mouse_resize_sensibility(10)
        self.tmp.set_win_title_botton_side('right')
        self.tmp.show()

        self.test_btn_1 = QPushButton('test button 1',self.tmp)
        self.test_btn_1.setObjectName('custom_btn1')
        self.test_btn_1.setFixedSize(300,100)
        self.test_btn_1.move(100,200)
        self.test_btn_2 = QPushButton('test button 2',self.tmp)
        self.test_btn_2.setObjectName('custom_btn1')
        self.test_btn_2.setFixedSize(300, 100)

        self.test_btn_1.show()
        self.test_btn_2.show()
        self.tmp.resizeEvent(0)
        #dummy_layput = QVBoxLayout()
        #dummy_layput.addWidget(self.test_btn_1)
        #dummy_layput.addWidget(self.test_btn_2)
        #self.tmp.setLayout(dummy_layput)


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

        self.set_win_title_bat_button_side_btn = QPushButton('Titlebar buttons (right)')
        self.set_win_title_bat_button_side_btn.setMinimumHeight(min_btb_h)
        self.set_win_title_bat_button_side_btn.setMinimumWidth(min_btn_w)
        self.set_win_title_bat_button_side_btn.setDisabled(False)
        self.set_win_title_bat_button_side_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.set_win_title_bat_button_side_btn.setStyleSheet(css_)
        self.set_win_title_bat_button_side_btn.clicked.connect(self.shift_titlebar_button_side)

        self.set_btn_backgrnd_btn = QPushButton('Button background')
        self.set_btn_backgrnd_btn.setMinimumHeight(min_btb_h)
        self.set_btn_backgrnd_btn.setMinimumWidth(min_btn_w)
        self.set_btn_backgrnd_btn.setDisabled(False)
        self.set_btn_backgrnd_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.set_btn_backgrnd_btn.setStyleSheet(css_)
        self.set_btn_backgrnd_btn.clicked.connect(self.select_button_background)

        self.set_btn_radius_btn = QPushButton('Button border radius')
        self.set_btn_radius_btn.setMinimumHeight(min_btb_h)
        self.set_btn_radius_btn.setMinimumWidth(min_btn_w)
        self.set_btn_radius_btn.setDisabled(False)
        self.set_btn_radius_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.set_btn_radius_btn.setStyleSheet(css_)
        self.set_btn_radius_btn.clicked.connect(self.set_btn_radius)

        self.titlebar_lbl = QLineEdit('')
        self.titlebar_lbl.returnPressed.connect(self.select_titlebar_color_enter)
        self.frame_col_lbl = QLineEdit('')
        self.frame_col_lbl.returnPressed.connect(self.select_frame_color_enter)
        self.main_background_lbl = QLineEdit('')
        self.main_background_lbl.returnPressed.connect(self.main_background_lbl_enter)
        self.framewidth_lbl = QLineEdit('')
        self.framewidth_lbl.returnPressed.connect(self.main_background_lbl_enter)
        self.resize_senitivity_lbl = QLineEdit('')
        self.resize_senitivity_lbl.returnPressed.connect(self.set_resize_sensitivity_enter)
        self.set_btn_backgrnd_lbl = QLineEdit('')
        self.set_btn_backgrnd_lbl.returnPressed.connect(self.select_button_background_enter)
        self.set_btn_radius_lbl = QLineEdit('')
        self.set_btn_radius_lbl.returnPressed.connect(self.set_btn_radius_enter)


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
        layout6 = QHBoxLayout()
        layout6.addWidget(self.set_win_title_bat_button_side_btn)
        layout7 = QHBoxLayout()
        layout7.addWidget(self.set_btn_backgrnd_btn)
        layout7.addWidget(self.set_btn_backgrnd_lbl)
        layout8 = QHBoxLayout()
        layout8.addWidget(self.set_btn_radius_btn)
        layout8.addWidget(self.set_btn_radius_lbl)

        all_buttons_layout = QVBoxLayout()
        all_buttons_layout.addLayout(layout1)
        all_buttons_layout.addLayout(layout2)
        all_buttons_layout.addLayout(layout3)
        all_buttons_layout.addLayout(layout4)
        all_buttons_layout.addLayout(layout5)
        all_buttons_layout.addLayout(layout6)
        all_buttons_layout.addLayout(layout7)
        all_buttons_layout.addLayout(layout8)

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
    def select_titlebar_color_enter(self):
        txt = self.titlebar_lbl.text()
        if txt[0]=="'":
            self.tmp.set_titlebar_color(txt[1:len(txt)-1])
        else:
            self.tmp.set_titlebar_color(txt)

    def select_frame_color(self):
        color = QColorDialog.getColor().getRgb()
        self.tmp.set_frame_color('rgba('+str(color[0])+','+str(color[1])+','+str(color[2])+',1)')
        self.frame_col_lbl.setText("'" + 'rgba('+str(color[0])+','+str(color[1])+','+str(color[2])+',1)' + "'")
    def select_frame_color_enter(self):
        txt = self.frame_col_lbl.text()
        if txt[0]=="'":
            self.tmp.set_frame_color(txt[1:len(txt)-1])
        else:
            self.tmp.set_frame_color(txt)

    def select_main_color(self):
        color = QColorDialog.getColor().getRgb()
        self.tmp.set_win_main_color('rgba('+str(color[0])+','+str(color[1])+','+str(color[2])+',1)')
        self.main_background_lbl.setText("'" + 'rgba('+str(color[0])+','+str(color[1])+','+str(color[2])+',1)' + "'")
    def main_background_lbl_enter(self):
        txt = self.main_background_lbl.text()
        if txt[0]=="'":
            self.tmp.set_win_main_color(txt[1:len(txt)-1])
        else:
            self.tmp.set_win_main_color(txt)

    def set_frame_width(self):
        nr_pixels, ok = QInputDialog.getText(self, 'set frame width', 'Type nr pixels width:')
        if ok:
            try:
                nr_pixels = int(nr_pixels)
                self.tmp.set_frame_width(nr_pixels)
                self.framewidth_lbl.setText(str(nr_pixels))

            except:
                print('dfgh')
    def main_background_lbl_enter(self):
        nr_pixels = self.framewidth_lbl.text()
        try:
            nr_pixels = int(nr_pixels)
            self.tmp.set_frame_width(nr_pixels)
        except:
            print('dfgh')

    def set_resize_sensitivity(self):
        nr_pixels, ok = QInputDialog.getText(self, 'set resize sensitivity', 'Type nr pixels:')
        if ok:
            try:
                nr_pixels = int(nr_pixels)
                self.tmp.set_mouse_resize_sensibility(nr_pixels)
                self.resize_senitivity_lbl.setText(str(nr_pixels))
            except:
                print('dfgh')
    def set_resize_sensitivity_enter(self):
        nr_pixels = self.resize_senitivity_lbl.text()
        try:
            nr_pixels = int(nr_pixels)
            self.tmp.set_mouse_resize_sensibility(nr_pixels)
        except:
            print('dfgh')

    def shift_titlebar_button_side(self):
        if 'right' in self.set_win_title_bat_button_side_btn.text():
            self.set_win_title_bat_button_side_btn.setText('Titlebar buttons (left)')
            self.tmp.set_win_title_botton_side('left')

        else:
            self.set_win_title_bat_button_side_btn.setText('Titlebar buttons (right)')
            self.tmp.set_win_title_botton_side('right')

    def select_button_background(self):
        color = QColorDialog.getColor().getRgb()
        self.tmp.set_btn_background_color('rgba('+str(color[0])+','+str(color[1])+','+str(color[2])+',1)')
        self.set_btn_backgrnd_lbl.setText("'" + 'rgba('+str(color[0])+','+str(color[1])+','+str(color[2])+',1)' + "'")

    def select_button_background_enter(self):
        txt = self.set_btn_backgrnd_lbl.text()
        if txt[0]=="'":
            self.tmp.set_btn_background_color(txt[1:len(txt)-1])
        else:
            self.tmp.set_btn_background_color(txt)

    def set_btn_radius(self):
        nr_pixels, ok = QInputDialog.getText(self, 'set button radius', 'Type nr pixels:')
        if ok:
            try:
                nr_pixels = int(nr_pixels)
                self.tmp.set_button_border_radius(str(nr_pixels))
                self.set_btn_radius_lbl.setText(str(nr_pixels))
            except:
                print('dfgh')
    def set_btn_radius_enter(self):
        nr_pixels = self.set_btn_radius_lbl.text()
        try:
            nr_pixels = int(nr_pixels)
            self.tmp.set_button_border_radius(str(nr_pixels))
        except:
            print('dfgh')


if __name__ == '__main__':
    app = QApplication([])
    screen_resolution = app.desktop().screenGeometry()
    width, height = screen_resolution.width(), screen_resolution.height()
    gui = open_main_gui(screen_height = height)
    gui.show()
    sys.exit(app.exec_())