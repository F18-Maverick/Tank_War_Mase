import math
from PIL import Image, ImageTk
class Bullets:
    def __init__(self, canvas, windows, mousex, mousey, tankx, tanky):
        self.root=windows
        self.tank_x=tankx
        self.tank_y=tanky
        self.mouse_x=mousex
        self.mouse_y=mousey
        self.black_canvas = canvas
        self.bullet_image=Image.open(r".\img\bullet.png")
        self.resize_img=self.bullet_image.resize((18, 6))
        self.image_to_tkinter = ImageTk.PhotoImage(self.resize_img)
        self.bullets_go=self.black_canvas.bind("<Button-1>", self.BulletsGo)
    def BulletsGo(self, event):
        self.bullet_turn=self.control_bullet
    def on_mouse_move(self):
        self.image_display = self.black_canvas.create_image(
            self.tank_x+9, self.tank_y+3, image=self.image_to_tkinter)
        self.img_position = self.black_canvas.coords(self.image_display)
        self.image_center_x = self.img_position[0]
        self.image_center_y = self.img_position[1]
        self.delta_x = self.mouse_x - self.image_center_x
        self.delta_y = self.mouse_y - self.image_center_y
        self.angle = math.degrees(math.atan2(self.delta_y, self.delta_x))
        self.update_image_rotation(self.angle)
    def update_image_rotation(self, angle):
        self.rotated_image = self.resize_img.rotate(-angle, expand=True)
        self.image_tk = ImageTk.PhotoImage(self.rotated_image)
        self.black_canvas.itemconfig(self.image_display, image=self.image_tk)
    def control_bullet(self):
        self.on_mouse_move()










