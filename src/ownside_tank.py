import math
from PIL import Image, ImageTk
class ownside_tank_function():
    def __init__(self, canvas, windows):
        self.mouse_x=0
        self.mouse_y=0
        self.imagex=0
        self.imagey=0
        self.step_size=1
        self.image_center_x=0
        self.image_center_y=0
        self.root=windows
        self.act_step_size=1
        self.black_canvas=canvas
        self.image_to_tkinter=None
        self.image_diaplay=None
        self.tank_image = Image.open(r".\img\tank.png")
        self.resize_image = self.tank_image.resize((40, 14))
        self.image_to_tkinter = ImageTk.PhotoImage(self.resize_image)
        self.image_display = self.black_canvas.create_image(42, 30, image=self.image_to_tkinter)
        self.mouse_go=self.black_canvas.bind("<Motion>", self.on_mouse_move)
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
        self.time = self.move_time()
        self.x_move_step = float(self.buttom_length / self.time)
        self.y_move_step = float(self.straight_length / self.time)
        self.image_position=self.black_canvas.coords(self.image_display)
        self.imagex=self.image_position[0]
        self.imagey=self.image_position[1]
        if abs(self.mouse_x-self.imagex)>self.step_size or abs(self.mouse_y-self.imagey)>self.step_size:
            if self.mouse_x<self.imagex:
                self.imagex-=self.x_move_step
            elif self.mouse_x>self.imagex:
                self.imagex+=self.x_move_step
            if self.mouse_y<self.imagey:
                self.imagey-=self.y_move_step
            elif self.mouse_y>self.imagey:
                self.imagey+=self.y_move_step
            self.move_img=self.black_canvas.coords(self.image_display, self.imagex, self.imagey)
    def move_time(self):
        self.buttom_length=abs(self.imagex-self.mouse_x)
        self.straight_length=abs(self.imagey-self.mouse_y)
        self.power = self.buttom_length ** 2 + self.straight_length ** 2
        self.bevel_edge_length = int(pow(self.power, 0.5))
        self.time = int(self.bevel_edge_length / self.act_step_size)
        return self.time
    def control_moving(self, event):
        self.tank_move(event)



















