import tkinter
class windows:
    def __init__(self):
        self.window=tkinter.Tk()
        self.window_title=self.window.title("坦克大战（测试版）")
        self.window_height=int(600)
        self.window_width=int(1320)
        self.computer_info_height = self.window.winfo_screenheight()
        self.computer_info_width = self.window.winfo_screenwidth()
        self.screen_x = int((self.computer_info_width - self.window_width) / 2)
        self.screen_y = int((self.computer_info_height - self.window_height) / 2)
        self.size_position_str = "{}x{}+{}+{}".format(self.window_width, self.window_height, self.screen_x, self.screen_y)
        self.New_Windows = self.window.geometry(self.size_position_str)
        self.unsizeable=self.window.resizable(width=False, height=False)
        self.black_canves = tkinter.Canvas(self.window, width=self.window_width, height=self.window_height, bg="black")
        self.pack = self.black_canves.pack()













