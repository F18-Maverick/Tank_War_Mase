import math
from PIL import Image, ImageTk
class Bullets:
    def __init__(self, canvas, windows, tank_img):
        self.mouse_x=0
        self.mouse_y=0
        self.root=windows
        self.act_step_size=2
        self.image_center_x=0
        self.image_center_y=0
        self.bullet_display=None
        self.tank_image=tank_img
        self.black_canvas = canvas
        self.bullet_image=Image.open(r".\img\bullet.png")
        self.resize_img=self.bullet_image.resize((18, 6))
        self.image_to_tkinter = ImageTk.PhotoImage(self.resize_img)
        self.bullets_go=self.black_canvas.bind("<Button-1>", self.BulletsGo)
    def BulletsGo(self, event):
        self.mouse_x=event.x
        self.mouse_y=event.y
        self.bullet_display = self.black_canvas.create_image(
            self.image_center_x, self.image_center_y, image=self.image_to_tkinter)
        self.bullet_turn=self.control_bullet()
    def on_mouse_move(self):
        self.tank_position=self.black_canvas.coords(self.tank_image)
        self.tank_x=self.tank_position[0]
        self.tank_y=self.tank_position[1]
        self.image_display = self.black_canvas.create_image(
            self.tank_x, self.tank_y, image=self.image_to_tkinter)
        self.img_position = self.black_canvas.coords(self.image_display)
        self.image_center_x = self.img_position[0]
        self.image_center_y = self.img_position[1]
        self.delta_x = self.mouse_x - self.image_center_x
        self.delta_y = self.mouse_y - self.image_center_y
        self.angle = math.degrees(math.atan2(self.delta_y, self.delta_x))
        print(self.angle)
        self.update_image_rotation(self.angle)
    def update_image_rotation(self, angle):
        self.rotated_image = self.resize_img.rotate(-angle, expand=True)
        self.image_tk = ImageTk.PhotoImage(self.rotated_image)
        self.black_canvas.itemconfig(self.image_display, image=self.image_tk)
    def bullet_move(self):
        self.time=self.move_time()
        self.x_move_step=int(self.buttom_length/self.time)
        self.y_move_step=int(self.straight_length/self.time)
        if self.mouse_x < self.image_center_x:
            self.image_center_x -= self.x_move_step
        elif self.mouse_x > self.image_center_x:
            self.image_center_x += self.x_move_step
        if self.mouse_y < self.image_center_y:
            self.image_center_y -= self.y_move_step
        elif self.mouse_y > self.image_center_y:
            self.image_center_y += self.y_move_step
        self.move_img = self.black_canvas.coords(self.image_display, self.image_center_x, self.image_center_y)
    def move_time(self):
        self.buttom_length=abs(self.image_center_x-self.mouse_x)
        self.straight_length=abs(self.image_center_y-self.mouse_y)
        self.power=self.buttom_length**2+self.straight_length**2
        self.bevel_edge_length=int(pow(self.power, 0.5))
        self.time=int(self.bevel_edge_length/self.act_step_size)
        return self.time
    def control_bullet(self):
        self.on_mouse_move()
        self.bullet_move()
        self.update=self.root.after(1000, self.control_bullet)










