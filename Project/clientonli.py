import pyscreenshot
from client import Client
# import pygame
import socket
import pyHook
import pythoncom
from simulateInput import PressKey, ReleaseKey
import win32api
import ctypes
import time
import pyautogui
import threading

RESOLUTION = 0
SERVER_IP = "127.0.0.1"
PORT = 8820


my_socket = socket.socket()
my_socket.connect((SERVER_IP, PORT))
client = Client(my_socket, my_socket.recv(1024))


class inputEvent:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        # return "(" + repr(self.type) + ",\'" + str(self.value) + ")"
        return repr(self.type) + "^" + str(self.value)

    def __repr__(self):
        return str(self)


def record():
    global pressedKeys
    global instructions
    pressedKeys = []
    instructions = []
    hooks_manager = pyHook.HookManager()
    hooks_manager.KeyAll = OnKeyboardEvent
    hooks_manager.HookKeyboard()
    mouse_hook_manager = pyHook.HookManager()
    mouse_hook_manager.MouseAll = OnMouseEvent
    mouse_hook_manager.HookMouse()
    pythoncom.PumpMessages()


def OnKeyboardEvent(event):
    # instructions.append(inputEvent(event.MessageName, event.KeyID))
    stuff = (inputEvent(event.MessageName, event.KeyID)).__str__()
    print stuff
    client.my_socket.send(stuff)
    return True


def OnMouseEvent(event):
    if event.MessageName == 'mouse wheel':
        # instructions.append(inputEvent(event.MessageName, event.Wheel))
        stuff = (inputEvent(event.MessageName, event.Wheel)).__str__()
        print stuff
        client.my_socket.send(stuff)
    else:
        # instructions.append(inputEvent(event.MessageName, (event.Position[0], event.Position[1])))
        stuff = (inputEvent(event.MessageName, (event.Position[0], event.Position[1]))).__str__()
        print stuff
        client.my_socket.send(stuff)

    return True


def screenshot():
    im = pyscreenshot.grab()
    im.save('image.jpg')


def send_screenshot():
    """
    sends a screenshot
    """
    pass

def receive_screenshot():
    # while True:
    pass

def wrap_command():
    """
    prepares the command for sending
    """
    pass

def handle_command():
    """
    executes sent commands
    """
    pass


def send_command():
    """
    sends a command
    """
    pass


def resolution():
    """
    changes screen resolution to a default resolution
    """
    pass


def randomize_password():
    """
    randomizes a user password
    """
    pass


def menu():
    pass


def operate():
    while True:
        try:
            input = client.my_socket.recv(1024)
            input = input.replace('\'', '')
            input = input.split("^")
            print input[0]
            print input[1]
            if input[0] == 'key down' or input[0] == 'key sys down':
                # pyautogui.keyDown(input[1].lower())
                PressKey(int(input[1]))
                print 'down'
            elif input[0] == 'key up' or input[0] == 'key sys up':
                ReleaseKey(int(input[1]))
                print 'up'
            elif input[0] == 'mouse move':
                cords = eval(input[1])
                # pyautogui.moveTo(x = cords[0], y = cords[1])
                win32api.SetCursorPos((int(cords[0]), int(cords[1])))
            elif input[0] == 'mouse left down':
                ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)  # left down
            elif input[0] == 'mouse left up':

                ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)  # left up
            elif input[0] == 'mouse right down':
                print 'down'
                ctypes.windll.user32.mouse_event(8, 0, 0, 0, 0)  # left down

            elif input[0] == 'mouse right up':
                print 'up'
                ctypes.windll.user32.mouse_event(16, 0, 0, 0, 0)  # left up
            elif input[0] == 'mouse wheel':
                print "wheel"
                ctypes.windll.user32.mouse_event(0x0800, 0, 0, 120 * int(input[1]), 0)  # left up
            # print command
        except:
            pass



def main():
    print client.type
    if client.type == "A":
        record()

    if client.type == "B":
        operate()




if __name__ == '__main__':
    main()