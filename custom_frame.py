from PyQt5.QtWidgets import (QVBoxLayout,QHBoxLayout,QPushButton)
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (
    QDialog,
    QLabel
)
from PyQt5.QtCore import Qt, QRect

#from PySide import QtGui

TITLEBAR_COLOR = 'rgba(117,125,90,1)'
FRAME_COLOR = 'rgba(117,125,90,1)' #Green military
#FRAME_COLOR = 'rgba(200,125,90,1)' #pink-orange
WIN_MAIN_COLOR = 'rgba(40,40,40,0)'
MAIN_LABEL_COLOR = 'rgba(40,40,40,1)'
MIN_WIN_BTN_HOVER_COLOR = 'rgb(80,80,80)'

CSS = \
    {
        'QLabel#win_title_lbl':
            {
                'color': 'rgb(244,244,244)',
                'background':TITLEBAR_COLOR,
                'font-size': '14px',
            },
        'QLabel#bkgrnd_lbl_frame':
            {
                'background':FRAME_COLOR,
            },
        'QLabel#bkgrnd_lbl2':
            {
                'background': WIN_MAIN_COLOR,
            },
        'QLabel#frame_resize_label_left':
            {
                'background':  'rgb(255,255,255,0)',
            },
        'QLabel#frame_resize_label_left:hover':
            {
                'background': 'rgb(255,255,255,0)',
            },
        'QLabel#frame_resize_label_right':
            {
                'background': 'rgb(255,255,255,0)',
            },
        'QLabel#frame_resize_label_right:hover':
            {
                'background': 'rgb(255,255,255,0)',
            },
        'QLabel#frame_resize_label_bottom':
            {
                'background': 'rgb(255,255,255,0)',
            },
        'QLabel#frame_resize_label_bottom:hover':
            {
                'background': 'rgb(255,255,255,0)',
            },
        'QLabel#frame_resize_label_bottom_left':
            {
                'background': 'rgb(255,255,255,0)',
            },
        'QLabel#frame_resize_label_bottom_left:hover':
            {
                'background': 'rgb(255,255,255,0)',
            },
        'QLabel#frame_resize_label_bottom_right':
            {
                'background': 'rgb(255,255,255,0)',
            },
        'QLabel#frame_resize_label_bottom_right:hover':
            {
                'background': 'rgb(255,255,255,0)',
            },
        'QPushButton':
            {
                'color': '#888888',
                'background-color': TITLEBAR_COLOR,
                'font-weight': 'bold',
                'border': 'none',
                'padding': '5px',
            },
        'QPushButton:active':
            {
                'color': '#ffffff',
            },
        'QPushButton:!active':
            {
                'color': 'rgba(255, 255, 255, 1)',
            },
        'QPushButton:hover':
            {
                'color': 'rgba(255, 255, 255, 1)',
                'background-color': 'rgba(255, 85, 45, 1)',
            },
        'QPushButton#minimize_win_btn:hover':
            {
                'color': 'rgba(255, 255, 255, 1)',
                'background-color': MIN_WIN_BTN_HOVER_COLOR,
            },
        'QPushButton#custom_btn1':
            {
                'font-size':'20px',
                'border': '2px solid',
                'border-color': TITLEBAR_COLOR,
                'border-radius':'20',
                'padding': '5px',
            },
        'QPushButton#custom_btn1:!hover':
            {
                'color': 'rgba(255, 255, 255, 1)',
                'background-color': WIN_MAIN_COLOR,
            },
        'QPushButton#custom_btn1:hover':
            {
                'color': 'rgba(255, 255, 255, 1)',
                'background-color': WIN_MAIN_COLOR,
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


class custom_frame_dialog(QDialog):

    def __init__(self,parent=None,screen_height=1200):
        super(custom_frame_dialog, self).__init__(parent)

        self.frame_color = FRAME_COLOR
        self.titlebar_color = TITLEBAR_COLOR
        self.css_sheet = CSS
        self.frame_wid = 3
        self.mouse_edge_resize_sensitivity = 5 # pixels
        self.title_bar_height = int(0.025 * screen_height)

        self.setStyleSheet(dictToCSS(self.css_sheet))
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.title_bar = top_frame_layout(parent=self, screen_height = screen_height)
        self.background_label_frame = QLabel('',self,objectName='bkgrnd_lbl_frame')
        self.background_label2 = QLabel('',self,objectName='bkgrnd_lbl2')

        # To be able to resize the window:
        self.frame_resize_label_left = QLabel('',self,objectName='frame_resize_label_left')
        self.frame_resize_label_right = QLabel('', self, objectName='frame_resize_label_right')
        self.frame_resize_label_bottom = QLabel('', self, objectName='frame_resize_label_bottom')
        self.frame_resize_label_bottom_left = QLabel('', self, objectName='frame_resize_label_bottom_left')
        self.frame_resize_label_bottom_right = QLabel('', self, objectName='frame_resize_label_bottom_right')

        self.setMouseTracking(True)
        self.background_label_frame.setMouseTracking(True)
        self.background_label2.setMouseTracking(True)
        self.title_bar.win_title_lbl.setMouseTracking(True)
        self.title_bar.close_btn.setMouseTracking(True)
        self.frame_resize_label_left.setMouseTracking(True)
        self.frame_resize_label_right.setMouseTracking(True)
        self.frame_resize_label_bottom.setMouseTracking(True)
        self.frame_resize_label_bottom_left.setMouseTracking(True)
        self.frame_resize_label_bottom_right.setMouseTracking(True)

        self.drag_setting = False

    def resizeEvent(self, event):
        self.title_bar.set_width(self.frameGeometry().width())
        self.background_label_frame.setFixedSize(self.frameGeometry().width(),self.frameGeometry().height()-self.title_bar_height)
        self.background_label_frame.move(0,self.title_bar_height)
        self.background_label2.setFixedSize(self.frameGeometry().width()-2*self.frame_wid,self.frameGeometry().height()-self.title_bar_height-self.frame_wid)
        self.background_label2.move(self.frame_wid,self.title_bar_height)

        # Resize window labels on the frame edge:
        self.frame_resize_label_left.setFixedSize(self.frame_wid,self.frameGeometry().height()-self.title_bar_height-self.frame_wid)
        self.frame_resize_label_left.move(0,self.title_bar_height)

        self.frame_resize_label_right.setFixedSize(self.frame_wid,self.frameGeometry().height()-self.title_bar_height-self.frame_wid)
        self.frame_resize_label_right.move(self.frameGeometry().width()-self.frame_wid,self.title_bar_height)

        self.frame_resize_label_bottom.setFixedSize(self.frameGeometry().width()-2*self.frame_wid,self.frame_wid)
        self.frame_resize_label_bottom.move(self.frame_wid,self.frameGeometry().height()-self.frame_wid)

        self.frame_resize_label_bottom_left.setFixedSize(self.frame_wid,self.frame_wid)
        self.frame_resize_label_bottom_left.move(0, self.frameGeometry().height() - self.frame_wid)

        self.frame_resize_label_bottom_right.setFixedSize(self.frame_wid, self.frame_wid)
        self.frame_resize_label_bottom_right.move(self.frameGeometry().width()-self.frame_wid, self.frameGeometry().height() - self.frame_wid)


        try:
            child_btns_added = [w for w in self.children() if w.objectName() == 'custom_btn1']

            for i,but in enumerate(child_btns_added):
                but.setGeometry(self.frameGeometry().width() * 0.5 - but.geometry().width() * 0.5, self.frameGeometry().height()*0.5-60*len(child_btns_added)+i*120, but.geometry().width(), but.geometry().height())
            self.setMinimumHeight(len(child_btns_added)*120+80)
        except:
            pass


    def set_button_border_radius(self,r):
        self.css_sheet['QPushButton#custom_btn1']['border-radius'] = r
        self.setStyleSheet(dictToCSS(self.css_sheet))

    def set_btn_background_color(self,color_in):
        self.css_sheet['QPushButton#custom_btn1:!hover']['background'] = color_in
        self.css_sheet['QPushButton#custom_btn1:hover']['background'] = color_in
        self.setStyleSheet(dictToCSS(self.css_sheet))

    def set_frame_color(self,color_in):
        self.css_sheet['QLabel#bkgrnd_lbl_frame']['background'] = color_in
        self.css_sheet['QPushButton#custom_btn1']['border-color'] = color_in
        self.css_sheet['QPushButton#custom_btn1:!hover']['color'] = color_in
        self.setStyleSheet(dictToCSS(self.css_sheet))

    def set_titlebar_color(self,color_in):
        self.css_sheet['QLabel#win_title_lbl']['background'] = color_in
        self.css_sheet['QPushButton']['background-color'] = color_in
        self.setStyleSheet(dictToCSS(self.css_sheet))

    def set_win_main_color(self,color_in):
        self.css_sheet['QLabel#bkgrnd_lbl2']['background'] = color_in
        self.setStyleSheet(dictToCSS(self.css_sheet))

    def set_frame_width(self,nr_pixels=3):
        self.frame_wid = nr_pixels
        self.resizeEvent(0)

    def set_mouse_resize_sensibility(self,nr_pixels = 3):
        self.mouse_edge_resize_sensitivity = nr_pixels

    def setWindowTitle(self,str_):
        self.title_bar.win_title_lbl.setText(' ' + str_ + '   ')

    def set_win_title_botton_side(self,where_ = 'right'):
        self.title_bar.set_titlebar_buttons(where_)

    # Mose events for moving window and hovering:
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            if self.drag_setting == 'move':
                self.move(event.globalPos() - self.mousePosition)
                event.accept()
            else:
                # Check if we are going to resize the window manually
                if self.drag_setting == 'left_resize':
                    if ((self.frame_orig_pos.x()+self.frame_orig_width) - event.globalPos().x()) >= self.minimumWidth():
                        w = (self.frame_orig_pos.x()+self.frame_orig_width) - event.globalPos().x()
                        h = self.frameGeometry().height()
                        self.setGeometry(event.globalPos().x(), self.frame_orig_pos.y(), w, h)
                elif self.drag_setting == 'right_resize':
                    if (event.globalPos().x() - self.frame_orig_pos.x()) >= self.minimumWidth():
                        w = (event.globalPos().x() - self.frame_orig_pos.x())
                        h = self.frameGeometry().height()
                        self.setGeometry(self.frame_orig_pos.x(), self.frame_orig_pos.y(), w, h)
                elif self.drag_setting == 'bottom_resize':
                    if (event.globalPos().y()-self.frame_orig_pos.y()) >= self.minimumHeight():
                        w = self.frameGeometry().width()
                        h = (event.globalPos().y()-self.frame_orig_pos.y())
                        self.setGeometry(self.frame_orig_pos.x(), self.frame_orig_pos.y(), w, h)
                elif self.drag_setting == 'bottom_left_resize':
                    w = self.frame_orig_width
                    h = self.frame_orig_height
                    if ((self.frame_orig_pos.x()+self.frame_orig_width) - event.globalPos().x()) >= self.minimumWidth():
                        w = (self.frame_orig_pos.x() + self.frame_orig_width) - event.globalPos().x()
                    if (event.globalPos().y() - self.frame_orig_pos.y()) >= self.minimumHeight():
                        h = (event.globalPos().y() - self.frame_orig_pos.y())
                    self.setGeometry(event.globalPos().x(), self.frame_orig_pos.y(), w, h)
                elif self.drag_setting == 'bottom_right_resize':
                    w = self.frame_orig_width
                    h = self.frame_orig_height
                    if (event.globalPos().x() - self.frame_orig_pos.x()) >= self.minimumWidth():
                        w = (event.globalPos().x() - self.frame_orig_pos.x())
                    if (event.globalPos().y()-self.frame_orig_pos.y()) >= self.minimumHeight():
                        h = (event.globalPos().y()-self.frame_orig_pos.y())
                    self.setGeometry(self.frame_orig_pos.x(), self.frame_orig_pos.y(), w, h)

        if event.buttons() == QtCore.Qt.NoButton:
            # If hovering with mouse close to edges, update cursor.
            self.mousePosition = event.globalPos() - self.frameGeometry().topLeft()
            x = self.mousePosition.x()
            y = self.mousePosition.y()
            if x < self.mouse_edge_resize_sensitivity and y > self.title_bar_height and y < (self.frameGeometry().height()-self.mouse_edge_resize_sensitivity):
                self.setCursor(Qt.SizeHorCursor)
            elif x > self.frameGeometry().width()-self.mouse_edge_resize_sensitivity and y > self.title_bar_height and y < (self.frameGeometry().height()-self.mouse_edge_resize_sensitivity):
                self.setCursor(Qt.SizeHorCursor)
            elif x > self.mouse_edge_resize_sensitivity and x < self.frameGeometry().width()-self.mouse_edge_resize_sensitivity and y > (self.frameGeometry().height()-self.mouse_edge_resize_sensitivity):
                self.setCursor(Qt.SizeVerCursor)
            elif x < self.mouse_edge_resize_sensitivity and y > (self.frameGeometry().height()-self.mouse_edge_resize_sensitivity):
                self.setCursor(Qt.SizeBDiagCursor)
            elif x > self.frameGeometry().width()-self.mouse_edge_resize_sensitivity and y > (self.frameGeometry().height()-self.mouse_edge_resize_sensitivity):
                self.setCursor(Qt.SizeFDiagCursor)
            else:
                self.setCursor(Qt.ArrowCursor)

    def mouseReleaseEvent(self, event):
        self.drag_setting = ''

    def mousePressEvent(self, event):
        # Enable mouse dragging
        if event.button() == QtCore.Qt.LeftButton:
            self.mousePosition = event.globalPos() - self.frameGeometry().topLeft()
            if self.mousePosition.y() < self.title_bar_height:
                self.drag_setting = 'move'
            else:
                # Resize mode
                x = self.mousePosition.x()
                y = self.mousePosition.y()
                if x < self.mouse_edge_resize_sensitivity and y < (self.frameGeometry().height() - self.mouse_edge_resize_sensitivity):
                    self.drag_setting = 'left_resize'
                    self.frame_orig_pos = self.frameGeometry().topLeft()
                    self.frame_orig_width = self.frameGeometry().width()
                    self.frame_orig_right_x = self.frame_orig_pos.x() + self.frame_orig_width
                elif x > self.frameGeometry().width() - self.mouse_edge_resize_sensitivity and y > self.title_bar_height and y < (self.frameGeometry().height() - self.mouse_edge_resize_sensitivity):
                    self.drag_setting = 'right_resize'
                    self.frame_orig_pos = self.frameGeometry().topLeft()
                    self.frame_orig_width = self.frameGeometry().width()
                elif x > self.mouse_edge_resize_sensitivity and x < self.frameGeometry().width() - self.mouse_edge_resize_sensitivity and y > (self.frameGeometry().height() - self.mouse_edge_resize_sensitivity):
                    self.drag_setting = 'bottom_resize'
                    self.frame_orig_pos = self.frameGeometry().topLeft()
                    self.frame_orig_height = self.frameGeometry().height()
                elif x < self.mouse_edge_resize_sensitivity and y > (self.frameGeometry().height() - self.mouse_edge_resize_sensitivity):
                    self.drag_setting = 'bottom_left_resize'
                    self.frame_orig_pos = self.frameGeometry().topLeft()
                    self.frame_orig_width = self.frameGeometry().width()
                    self.frame_orig_height = self.frameGeometry().height()
                elif x > self.frameGeometry().width() - self.mouse_edge_resize_sensitivity and y > (self.frameGeometry().height() - self.mouse_edge_resize_sensitivity):
                    self.drag_setting = 'bottom_right_resize'
                    self.frame_orig_pos = self.frameGeometry().topLeft()
                    self.frame_orig_width = self.frameGeometry().width()
                    self.frame_orig_height = self.frameGeometry().height()

class top_frame_layout(QHBoxLayout):
    def __init__(self, parent=None,screen_height=1200):
        super(top_frame_layout,self).__init__()
        self.parent=parent
        self.close_button_slignment = 'right'

        self.title_bar_height = int(0.025 * screen_height)
        self.buttons_width = int(4*self.title_bar_height/3)

        self.layput_ = QHBoxLayout()
        self.dummy_lbl = QLabel("")
        self.dummy_lbl.setFixedSize(1, self.title_bar_height)
        self.layput_.addWidget(self.dummy_lbl)

        self.win_title_lbl = QtWidgets.QLabel('',self.parent)
        self.win_title_lbl.setObjectName("win_title_lbl")
        self.win_title_lbl.setFocusPolicy(QtCore.Qt.NoFocus)
        self.win_title_lbl.move(0, 0)

        self.close_btn = QtWidgets.QPushButton('X',self.parent)
        self.close_btn.setFixedSize(self.buttons_width, self.title_bar_height)
        self.close_btn.clicked.connect(self.parent.close)
        self.close_btn.setFocusPolicy(QtCore.Qt.NoFocus)

        self.minimize_btn = QtWidgets.QPushButton("-",self.parent)
        self.minimize_btn.setFixedSize(self.buttons_width, self.title_bar_height)
        self.minimize_btn.clicked.connect(self.parent.showMinimized)
        self.minimize_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.minimize_btn.setObjectName('minimize_win_btn')

    def set_titlebar_buttons(self,where_):
        if where_ == 'left':
            self.close_button_slignment = where_
        else:
            self.close_button_slignment = 'right'
        self.set_width(self.parent.frameGeometry().width())


    def set_width(self,new_wid):
        if self.close_button_slignment == 'right':
            self.close_btn.move(new_wid-self.buttons_width, 0)
            self.minimize_btn.move(new_wid - 2*self.buttons_width, 0)
            self.win_title_lbl.setFixedSize(new_wid-2*self.buttons_width, self.title_bar_height )
            self.win_title_lbl.move(0,0)
            self.win_title_lbl.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        elif self.close_button_slignment == 'left':
            self.close_btn.move(0, 0)
            self.minimize_btn.move(self.buttons_width, 0)
            self.win_title_lbl.setFixedSize(new_wid-2*self.buttons_width, self.title_bar_height )
            self.win_title_lbl.move(2*self.buttons_width,0)
            self.win_title_lbl.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)