class Phone():
    def __init__(self,wifi,battery):
        self.wificonntected = wifi
        self.batterypercentage = battery
        self.running_apps = []
        self.ischarging = False

    def charging(self):
        self.ischarging = True
    
    def notcharging(self):
        self.ischarging = False

    def run_app(self, app_name):
        self.running_apps.append(app_name)
        print(f"Running app: {app_name}")
    
    def display_apps(self):
        i=0
        for item in self.running_apps:
            i= i+1
            print(i, end=". ")
            print(item)


    def connected_to_wifi(self):
        if self.wificonntected == True:
            print("Phone is connected to WiFi")
        else:
            print("No wifi connection")

    def display_info(self):
        
        print(self.connected_to_wifi())
        print(self.batterypercentage, end="%")
        print()
        print(f"Currently running apps: ")
        print(self.display_apps())
        if self.ischarging == True:
            print("The phone is currently charging")
        else:
            print("The phone is currently not charging")
        

def main():
    smartphone = Phone(True, 86)
    
    smartphone.charging()
    smartphone.run_app("Tiktok")
    smartphone.run_app("Twitter")
    smartphone.display_info()
    smartphone.notcharging()


if __name__ =="__main__":
    main()