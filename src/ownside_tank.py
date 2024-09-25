import math
from PIL import Image, ImageTk
class ownside_tank_function():
    def __init__(self, canvas, windows):
        self.root=windows
        self.black_canvas=canvas
        self.image_to_tkinter=None
        self.image_diaplay=None
        self.mouse_go=self.black_canvas.bind("<Motion>", self.on_mouse_move)
        self.tank_image = Image.open(r".\img\tank.png")
        self.resize_image = self.tank_image.resize((40, 14))
        self.image_to_tkinter = ImageTk.PhotoImage(self.resize_image)
        self.image_display = self.black_canvas.create_image(42, 30, image=self.image_to_tkinter)
    def on_mouse_move(self):
        self.mouse_x, self.mouse_y=self.root.winfo_pointerxy()
        self.image_center_x=self.mouse_x-21
        self.image_center_y=self.mouse_y-8
        self.go_point=(self.image_center_x, self.image_center_y)
        self.img_position=self.black_canvas.coords(self.image_display)
        self.delta_x=self.mouse_x-self.image_center_x
        self.delta_y=self.mouse_y-self.image_center_y
        self.angle = math.degrees(math.atan2(self.delta_x, self.delta_y))
        self.update_image_rotation(self.angle)
        self.root.after(100, self.on_mouse_move)
    def update_image_rotation(self, angle):
        self.rotated_image = self.resize_image.rotate(-angle, expand=True)
        self.image_tk = ImageTk.PhotoImage(self.rotated_image)
        self.black_canvas.itemconfig(self.image_display, image=self.image_tk)



r"""
TypeError: ownside_tank_function.on_mouse_move() takes 1 positional argument but 2 were given
Exception in Tkinter callback
Traceback (most recent call last):
  File "D:\Software\python\Lib\tkinter\__init__.py", line 1968, in __call__
    return self.func(*args)
           ^^^^^^^^^^^^^^^^
TypeError: ownside_tank_function.on_mouse_move() takes 1 positional argument but 2 were given
"""














