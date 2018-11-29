#!/usr/bin/python3
# _-_encoding: utf-8_-_
import signal
import sys
import time

from asciimatics.exceptions import ResizeScreenError, StopApplication
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.widgets import Background, Layout, Frame, Label


class DemoFrame(Frame):
    def __init__(self, screen):
        super(DemoFrame, self).__init__(screen,
                                        int(screen.height * 2 // 3),
                                        int(screen.width * 2 // 3),
                                        has_shadow=True,
                                        name="My Form")
        layout = Layout([1], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(Label("这是一个很长的标签控件！这是一个很长的标签控件！这是一个很长的标签控件！这是一个很长的标签控件！这是一个很长的标签控件！这是一个很长的标签控件！这是一个很长的标签控件！这是一个很长的标签控件！这是一个很长的标签控件！这是一个很长的标签控件！这是一个很长的标签控件！这是一个很长的标签控件！这是一个很长的标签控件！这是一个很长的标签控件！"))
        self.fix()


def demo(screen, scene):
    screen.play([Scene([
        Background(screen),
        DemoFrame(screen)
    ], -1)], stop_on_resize=True, start_scene=scene)


def run():
    last_scene = None
    while True:
        try:
            Screen.wrapper(demo, catch_interrupt=False, arguments=[last_scene])
            sys.exit(0)
        except ResizeScreenError as e:
            last_scene = e.scene


def exit_app(signal, frame):
    print("exit")


if __name__ == '__main__':
    signal.signal(signal.SIGINT, exit_app)
    run()
