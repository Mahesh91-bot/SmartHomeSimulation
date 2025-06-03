from abc import ABC, abstractmethod

class SmartDevice(ABC):
    def __init__(self, name):
        self._name = name
        self.__is_on = False  # Private attribute

    @abstractmethod
    def operate(self):
        pass

    def turn_on(self):
        self.__is_on = True
        print(f"{self._name} is now ON.")

    def turn_off(self):
        self.__is_on = False
        print(f"{self._name} is now OFF.")

    def show_status(self):
        status = "ON" if self.__is_on else "OFF"
        print(f"{self._name} status: {status}")

    def is_device_on(self):
        return self.__is_on


class SmartLight(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.__brightness = 70  # Default brightness

    def operate(self):
        self.turn_on()
        print(f"{self._name} brightness set to {self.__brightness}%")

    def set_brightness(self, value):
        if 0 <= value <= 100:
            self.__brightness = value
        else:
            print("Brightness must be between 0 and 100.")

    def get_brightness(self):
        return self.__brightness


class SmartFan(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.__speed = "Medium"

    def operate(self):
        self.turn_on()
        print(f"{self._name} speed set to {self.__speed}")

    def set_speed(self, speed):
        if speed in ["Low", "Medium", "High"]:
            self.__speed = speed
        else:
            print("Speed must be 'Low', 'Medium', or 'High'.")

    def get_speed(self):
        return self.__speed


class SmartAC(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.__temperature = 24  # Default temperature

    def operate(self):
        self.turn_on()
        print(f"{self._name} temperature set to {self.__temperature}°C")

    def set_temperature(self, temp):
        if 16 <= temp <= 30:
            self.__temperature = temp
        else:
            print("Temperature must be between 16°C and 30°C.")

    def get_temperature(self):
        return self.__temperature


# =============================
# Demonstration
# =============================

light = SmartLight("Living Room Light")
fan = SmartFan("Ceiling Fan")
ac = SmartAC("Bedroom AC")

# Operate and show status
devices = [light, fan, ac]
for device in devices:
    device.operate()
    device.show_status()
    print()

# Try to access private attributes (should raise AttributeError)
try:
    print(light.__brightness)
except AttributeError:
    print("Direct access to private attribute __brightness is not allowed.")

try:
    print(fan.__speed)
except AttributeError:
    print("Direct access to private attribute __speed is not allowed.")

try:
    print(ac.__temperature)
except AttributeError:
    print("Direct access to private attribute __temperature is not allowed.")

print()

# Use setters to change values and display updated values
light.set_brightness(85)
print(f"Updated brightness: {light.get_brightness()}%")

fan.set_speed("High")
print(f"Updated speed: {fan.get_speed()}")

ac.set_temperature(22)
print(f"Updated temperature: {ac.get_temperature()}°C")
