''' Kivy Widget that accepts data and displays qrcode
'''

from threading import Thread
from functools import partial

import qrcode 
from qrcode import exceptions

# kivy cant give to pyqt5 threads
#from PyQt5.QtWidgets import (
#    QApplication, QVBoxLayout, QTextEdit, QHBoxLayout, QPushButton, QWidget,
#    QFileDialog,
#)

import threading


from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics.texture import Texture
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty, StringProperty, ListProperty,\
    BooleanProperty
from kivy.lang import Builder
from kivy.clock import Clock

import random
import string
import time

Builder.load_string('''
<QRCodeWidget>
    canvas.before:
        # Draw white Rectangle
        Color:
            rgba: root.background_color
        Rectangle:
            size: self.size
            pos: self.pos
    canvas.after:
        Color:
            rgba: root.foreground_color
        Rectangle:
            size: self.size
            pos: self.pos
    Image
        id: qrimage
        pos_hint: {'center_x': .5, 'center_y': .5}
        allow_stretch: True
        size_hint: None, None
        size: root.width * .9, root.height * .9
''')

#def thread(function):
#    def wrap(*args, **kwargs):
#        t = threading.Thread(target=function, args=args, kwargs=kwargs, daemon=True)
#        t.start()
#
#        return t
#    return wrap

class QRCodeWidget(FloatLayout):

    data = StringProperty(None, allow_none=True)
    background_color = ListProperty((1, 1, 1, 1))
    foreground_color = ListProperty((0, 0, 0, 0))

    stop = threading.Event()

#    def start_second_thread(self, l_text):
#        threading.Thread(target=self.update_qr_ran, args=(l_text,)).start()

    def __init__(self, **kwargs):
        super(QRCodeWidget, self).__init__(**kwargs)
        self.data = None
        self.qr = None
        self._qrtexture = None
        self.failure_cb = None

    def on_data(self, instance, value):
        if not (self.canvas or value):
            return
        try:
            self.update_qr()
        except qrcode.exceptions.DataOverflowError:
            if self.failure_cb:
                self.failure_cb()
            else:
                raise

    def set_data(self, data, failure_cb=None):
        if self.data == data:
            return
        self.failure_cb = failure_cb
        MinSize = 210 if len(data) < 128 else 500
        self.setMinimumSize((MinSize, MinSize))
        self.data = data
        self.qr = None

#    @thread
    def update_qr(self, *args):
        if not self.data and self.qr:
            return
        L = qrcode.constants.ERROR_CORRECT_L
#        H = qrcode.constants.ERROR_CORRECT_H
        data = self.data
        self.qr = qr = qrcode.QRCode(
            version=None,
            error_correction=L,
            box_size=10,
            border=0,
        )
        S = 5  # 5 random characters
        ran = ''.join(random.choices(
              string.digits, k=S))
        qr.add_data(data)
        qr.make(fit=True)
        self.update_texture()
        time.sleep(0.8)
#        Clock.schedule_interval(self.update_qr_ran, 1.0/33.0)
        Clock.schedule_once(self.update_qr_ran)

    def update_qr_ran(self, *args):
        if not self.data and self.qr:
            return
        L = qrcode.constants.ERROR_CORRECT_L
#        H = qrcode.constants.ERROR_CORRECT_H
        data = self.data
        self.qr = qr = qrcode.QRCode(
            version=None,
            error_correction=L,
            box_size=10,
            border=0,
        )
        S = 5  # 5 random characters
        ran = ''.join(random.choices(
              string.digits, k=S))
        qr.add_data(data+ran)
        time.sleep(0.4)
        qr.make(fit=True)
        self.update_texture()
#        Clock.schedule_interval(self.update_qr, 1.0/33.0)
        Clock.schedule_once(self.update_qr)

    def setMinimumSize(self, size):
        # currently unused, do we need this?
        self._texture_size = size

    def _create_texture(self, k):
        self._qrtexture = texture = Texture.create(size=(k,k), colorfmt='rgb')
        # don't interpolate texture
        texture.min_filter = 'nearest'
        texture.mag_filter = 'nearest'

    def update_texture(self):
        if not self.qr:
            return
        matrix = self.qr.get_matrix()
        k = len(matrix)
        # create the texture
        self._create_texture(k)
        buff = []
        bext = buff.extend
        cr, cg, cb, ca = self.background_color[:]
        cr, cg, cb = cr*255, cg*255, cb*255
        for r in range(k):
            for c in range(k):
                bext([0, 0, 0] if matrix[k-1-r][c] else [cr, cg, cb])
        # then blit the buffer
        buff = bytes(buff)
        # update texture
        self._upd_texture(buff)

    def _upd_texture(self, buff):
        texture = self._qrtexture
        texture.blit_buffer(buff, colorfmt='rgb', bufferfmt='ubyte')
        img = self.ids.qrimage
        img.anim_delay = -1
        img.texture = texture
        img.canvas.ask_update()

    def infinite_loop(self):
        iteration = 0
        while True:
            if self.stop.is_set():
                # Stop running this thread so the main Python process can exit.
                return
            iteration += 1
            print('Infinite loop, iteration {}.'.format(iteration))
            H = qrcode.constants.ERROR_CORRECT_H
            data = self.data
            self.qr = qr = qrcode.QRCode(
                version=None,
                error_correction=H,
                box_size=10,
                border=0,
            )
            S = 5  # 5 random characters
            ran = ''.join(random.choices(
               string.digits, k=S))
#        self.receive_qr.setData(uri+ran)
            time.sleep(0.8)
            qr.add_data(data)
            qr.make(fit=True)
            self.update_texture()



class ThreadedApp(App):

    def on_stop(self):
        # The Kivy event loop is about to stop, set a stop signal;
        # otherwise the app window will close, but the Python process will
        # keep running until all secondary threads exit.
        self.root.stop.set()

    def build(self):
        return QRCodeWidget()

if __name__ == '__main__':
    from kivy.app import runTouchApp
    import sys
    data = str(sys.argv[1:])
    runTouchApp(QRCodeWidget(data=data))


