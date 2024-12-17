class TV():
    def __init__(self, is_on):
        self.is_on = is_on
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False

    def show_status(self):
        if self.is_on == True:
            return "The TV is on"
        else:
            return "The TV is off"