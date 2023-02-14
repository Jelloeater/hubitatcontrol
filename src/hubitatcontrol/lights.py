from time import sleep

from hubitatcontrol.generic import Switch


class Dimmer(Switch):
    @property
    def level(self) -> int:
        return [x for x in self.attributes if "level" in x["name"]][0]["currentValue"]

    def set_level(self, level: int):
        self.send_device_command(command="setLevel", secondary_command=str(level))
        sleep(2.5)


class Bulb(Dimmer):
    pass


class ColorTempBulb(Bulb):
    @property
    def color_temp(self) -> int:
        return [x for x in self.attributes if "colorTemperature" in x["name"]][0]["currentValue"]

    def set_color_temp(self, level: int):
        self.send_device_command(command="setColorTemperature", secondary_command=str(level))
        sleep(2)


class RGBWBulb(ColorTempBulb):
    @property
    def color(self) -> str:
        return [x for x in self.attributes if "color" in x["name"]][0]["currentValue"]

    @property
    def hue(self) -> int:
        return [x for x in self.attributes if "hue" in x["name"]][0]["currentValue"]

    @property
    def color_mode(self) -> str:
        return [x for x in self.attributes if "colorMode" in x["name"]][0]["currentValue"]

    @property
    def color_name(self) -> str:
        return [x for x in self.attributes if "colorName" in x["name"]][0]["currentValue"]

    @property
    def saturation(self) -> str:
        return [x for x in self.attributes if "saturation" in x["name"]][0]["currentValue"]

    def set_hue(self, level: int):
        self.send_device_command(command="setHue", secondary_command=str(level))
        sleep(2)

    def set_saturation(self, level: int):
        self.send_device_command(command="setSaturation", secondary_command=str(level))
        sleep(2)

    def set_color(self, level: str):
        self.send_device_command(command="setColor", secondary_command=str(level))
        sleep(2)
