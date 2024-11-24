import math
from PIL import Image, ImageTk
class Bullets:
    def __init__(self, canvas, windows, tank_img):
        self.bullets = []
        self.img_position=0
        self.delta_x=0
        self.delta_y=0
        self.root = windows
        self.act_step_size = 2
        self.tank_image = tank_img
        self.black_canvas = canvas
        self.bullet_image = Image.open(r".\img\bullet.png")
        self.resize_img_tank = self.bullet_image.resize((18, 6))
        self.image_to_tkinter_tank = ImageTk.PhotoImage(self.resize_img_tank)
        self.explore_image = Image.open(r".\img\explore.png")
        self.resize_img_explore = self.explore_image.resize((18, 6))
        self.image_to_tkinter_explore = ImageTk.PhotoImage(self.resize_img)
        self.black_canvas.bind("<Button-1>", self.bullets_go)
    def rotate(self, bullet):
        self.angle = math.degrees(math.atan2(bullet["direction_y"], bullet["direction_x"]))
        self.update_image_rotation(self.angle, bullet)
    def update_image_rotation(self, angle, bullet):
        self.rotated_image = self.resize_img.rotate(-angle, expand=True)
        self.image_tk = ImageTk.PhotoImage(self.rotated_image)
        self.black_canvas.itemconfig(bullet["display"], image=self.image_tk)
        bullet['image_tk'] = self.image_tk
    def bullets_go(self, event):
        self.mouse_x = event.x
        self.mouse_y = event.y
        self.img_position = self.black_canvas.coords(self.tank_image)
        bullet_display = self.black_canvas.create_image(self.img_position[0], self.img_position[1], image=self.image_to_tkinter_tank)
        self.delta_x = self.mouse_x - self.img_position[0]
        self.delta_y = self.mouse_y - self.img_position[1]
        self.distance = math.sqrt(self.delta_x ** 2 + self.delta_y ** 2)
        if self.distance == 0:
            return
        self.direction_x = (self.delta_x / self.distance) * self.act_step_size
        self.direction_y = (self.delta_y / self.distance) * self.act_step_size
        self.bullet = {
            'display': bullet_display,
            'center_x': self.img_position[0],
            'center_y': self.img_position[1],
            'direction_x': self.direction_x,
            'direction_y': self.direction_y,
            "image_tk": None
        }
        self.bullets.append(self.bullet)
        self.control_bullet(self.bullet)
    def control_bullet(self, bullet):
        self.bullet_move(bullet)
        self.root.after(30, self.control_bullet, bullet)
    def bullet_move(self, bullet):
        self.rotate(bullet)
        bullet['center_x'] += bullet['direction_x']
        bullet['center_y'] += bullet['direction_y']
        if (bullet['center_x'] < 0 or bullet['center_x'] > self.black_canvas.winfo_width() or
            bullet['center_y'] < 0 or bullet['center_y'] > self.black_canvas.winfo_height()):
            self.black_canvas.delete(bullet['display'])
            self.bullets.remove(bullet)
            return
        if self.check_collision(bullet["center_x"], bullet["center_y"]):
            self.black_canvas.delete(bullet['display'])
            self.bullets.remove(bullet)
            self.black_canvas.create_image(self.img_position[0], self.img_position[1], image=self.image_to_tkinter_explore)
            return
        self.black_canvas.coords(bullet['display'], bullet['center_x'], bullet['center_y'])
























