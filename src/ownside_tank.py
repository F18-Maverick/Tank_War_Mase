import math
from PIL import Image, ImageTk
class ownside_tank_function():
    def __init__(self, canvas):
        self.black_canvas=canvas
        self.image_to_tkinter=None
        self.image_diaplay=None
        self.mouse_go=self.black_canvas.bind("<Motion>", self.on_mouse_move)
        self.tank_image = Image.open(r".\img\tank.png")
        self.resize_image = self.tank_image.resize((40, 14))
        self.image_to_tkinter = ImageTk.PhotoImage(self.resize_image)
        self.image_display = self.black_canvas.create_image(42, 30, image=self.image_to_tkinter)
    def on_mouse_move(self, event):
        self.mouse_x=event.x
        self.mouse_y=event.y
        self.image_center_x=self.mouse_x-21
        self.image_center_y=self.mouse_y-8
        self.new_place=self.black_canvas.coords(self.image_display, self.image_center_x, self.image_center_y)
        self.angle = math.degrees(math.atan2(self.mouse_y - 300, self.mouse_x - 400))
        self.update_image_rotation(self.angle)
    def update_image_rotation(self, angle):
        self.rotated_image = self.resize_image.rotate(-angle)
        self.image_tk = ImageTk.PhotoImage(self.rotated_image)
        self.black_canvas.itemconfig(self.image_display, image=self.image_tk)


















