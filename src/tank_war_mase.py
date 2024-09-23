import random
class Mase():
    def __init__(self, canvas):
        self.black_canvas=canvas
        self.origin_x = 0
        self.origin_y = 0
        self.step = 0
        self.num_step = 0
        while True:
            self.origin = [self.origin_x, self.origin_y]
            self.right = [self.origin[0] + 50, self.origin[1], "right"]
            self.left = [self.origin[0] - 50, self.origin[1], "left"]
            self.down = [self.origin[0], self.origin[1] + 50, "down"]
            self.up = [self.origin[0], self.origin[1] - 50, "up"]
            self.step_all = [self.right, self.left, self.down, self.up]
            self.Next_step=random.choice(self.step_all)
            self.direct_list=[]
            self.Next_step_list=[]
            if self.Next_step[0]<0 or self.Next_step[1]<0 or self.Next_step[0]>1300 or self.Next_step[1]>600:
                continue
            else:
                self.Next_step_list.append(self.Next_step)
                self.direct_list.append(self.Next_step[2])
                if self.Next_step[2]=="right":
                    self.origin_x+=50
                elif self.Next_step[2]=="left":
                    self.origin_x-=50
                elif self.Next_step[2]=="down":
                    self.origin_y+=50
                elif self.Next_step[2]=="up":
                    self.origin_y-=50
                else:
                    print("error")
            print(self.Next_step_list, ".............", self.direct_list)
            self.creat_mase_road = self.black_canvas.create_line(
                self.origin[0], self.origin[1], self.Next_step[0], self.Next_step[1], fill="white", width=50)
            if self.origin_x == 1300:
                break
            self.num_step+=1












