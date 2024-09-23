from PIL import Image, ImageTk
class ownside_tank_function():
    def __init__(self, canvas):
        self.black_canvas=canvas
        self.image_to_tkinter=None
        self.image_diaplay=None
    def tank_ownside_func(self):
        self.tank_image=Image.open(r".\img\tank.png")
        self.resize_image=self.tank_image.resize((40, 14))
        self.image_to_tkinter=ImageTk.PhotoImage(self.resize_image)
        self.image_diaplay=self.black_canvas.create_image(42, 30, image=self.image_to_tkinter)


















