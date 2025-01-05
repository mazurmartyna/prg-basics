class TV():
    def __init__(self, is_on, channel_no):
        self.is_on = is_on
        self.channel_no = channel_no
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False

    def show_status(self):
        if self.is_on == True:
            return "The TV is on, channel " + str(self.channel_no)
        else:
            return "The TV is off"