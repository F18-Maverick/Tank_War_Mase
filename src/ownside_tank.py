import math
from PIL import Image, ImageTk
class ownside_tank_function():
    def __init__(self, canvas, windows):
        self.root=windows
        self.black_canvas=canvas
        self.image_to_tkinter=None
        self.image_diaplay=None
        self.tank_image = Image.open(r".\img\tank.png")
        self.resize_image = self.tank_image.resize((40, 14))
        self.image_to_tkinter = ImageTk.PhotoImage(self.resize_image)
        self.image_display = self.black_canvas.create_image(42, 30, image=self.image_to_tkinter)
        self.mouse_go=self.black_canvas.bind("<Motion>", self.on_mouse_move)
        self.mouse_x=0
        self.mouse_y=0
        self.step_size=1
        self.tank_moving=self.root.bind("<w>", self.control_moving)
    def on_mouse_move(self, event):
        self.mouse_x = event.x
        self.mouse_y = event.y
        self.img_position = self.black_canvas.coords(self.image_display)
        self.image_center_x = self.img_position[0]
        self.image_center_y = self.img_position[1]
        self.delta_x = self.mouse_x - self.image_center_x
        self.delta_y = self.mouse_y - self.image_center_y
        self.angle = math.degrees(math.atan2(self.delta_y, self.delta_x))
        self.update_image_rotation(self.angle)
    def update_image_rotation(self, angle):
        self.rotated_image = self.resize_image.rotate(-angle, expand=True)
        self.image_tk = ImageTk.PhotoImage(self.rotated_image)
        self.black_canvas.itemconfig(self.image_display, image=self.image_tk)
    def tank_move(self, event):
        self.image_position=self.black_canvas.coords(self.image_display)
        self.imagex=self.image_position[0]
        self.imagey=self.image_position[1]
        if abs(self.mouse_x-self.imagex)>self.step_size or abs(self.mouse_y-self.imagey)>self.step_size:
            if self.mouse_x<self.imagex:
                self.imagex-=self.step_size
            elif self.mouse_x>self.imagex:
                self.imagex+=self.step_size
            if self.mouse_y<self.imagey:
                self.imagey-=self.step_size
            elif self.mouse_y>self.imagey:
                self.imagey+=self.step_size
            self.move_img=self.black_canvas.coords(self.image_display, self.imagex, self.imagey)
    def control_moving(self, event):
        self.tank_move(event)



r"""
     
"""














