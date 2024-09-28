from bullets import Bullets
from tank_war_mase import Mase
from tank_war_interface import windows
from ownside_tank import ownside_tank_function
class main_loop:
    def __init__(self):
        self.Windows=windows()
        self.mase=Mase(self.Windows.black_canves)
        self.owntank=ownside_tank_function(self.Windows.black_canves, self.Windows.window)
        self.bullets=Bullets(
            self.Windows.black_canves, self.Windows.window, self.owntank.image_display)
        self.MainLoop=self.Windows.window.mainloop()









