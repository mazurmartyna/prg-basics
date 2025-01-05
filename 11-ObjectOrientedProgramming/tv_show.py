# tv_show.py file
# main program
#import tv.py

class TV():
    def __init__(self, is_on, channel_no, channel_list, volume):
        self.is_on = is_on
        self.channel_no = channel_no
        self.channel_list = channel_list
        self.volume = volume
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False

    def set_channels(self):
        choice = 'y'
        while choice == 'y':
            new_channel = input("Enter the channel name:")
            self.channel_list.append(new_channel)
            choice = input("Do you wanna add next channel? y/n ")

    def show_channels(self):
        
        if len(self.channel_list) == 0:
            print("TV not set")
        else:
            n=1
            for item in self.channel_list:
                item = str(n)+". "+item
                print(item)
                n +=1

    def set_channel(self, new_channel_no):
        new_channel_no = input("Enter the channel number: ")
        self.channel_no = new_channel_no

    def increase_volume(self):
        if self.volume <10:
            self.volume += 1
    def decrease_volume(self):
        if self.volume >1:
            self.volume -= 1

    def show_status(self):
        name = ''
        if self.is_on == True:
            if int(self.channel_no) > len(self.channel_list):
                return "The TV is on, channel " + str(self.channel_no) + ", volume is: " + str(self.volume)
            else:
                name = self.channel_list[int(self.channel_no)-1]
                return "The TV is on, channel " + str(self.channel_no) + "("+name +")" + ", volume is: " + str(self.volume)
        else:
            return "The TV is off"

def main():
    x = 0
    # object creation
    televisor = TV(False,1,[],0)

    # object usage
    print("1 --> show status")
    print("2 --> turn on")
    print("3 --> set tv channels")
    print("4 --> show channel list")
    print("5 --> change channel")
    print("6 --> turn off")
    print("+ --> increase volume")
    print("- --> decrease volume")

    action = ''
    while action != "6":
        action = input("Press number: ")
        if action == "1":
            print(TV.show_status(televisor))
        elif action == "2":
            TV.turn_on(televisor)
        elif action == "3":
            TV.set_channels(televisor)
        elif action == "4":
            TV.show_channels(televisor)
        elif action == "5":
            TV.set_channel(televisor, x)
        elif action == "+":
            TV.increase_volume(televisor)
        elif action == "-":
            TV.decrease_volume(televisor)

        elif action == "6":
            TV.turn_off(televisor)
            print(TV.show_status(televisor))
            break
        else:
            print("Incorrect number!")

if __name__ == "__main__":
   main() 