import json
from time import sleep

from hubitatcontrol.generic import Switch


class Dimmer(Switch):
    @property
    def level(self) -> int:
        return [x for x in self.attributes if "level" in x["name"]][0]["currentValue"]

    def set_level(self, level: int):
        """0-100 valid range"""
        if level < 0 or level > 100:
            raise Exception("Invalid range")
        self.send_device_command(command="setLevel", secondary_command=str(level))
        sleep(2.5)


class Bulb(Dimmer):
    pass
    # TODO May need to add more methods, as bulbs might have more functionality


class ColorTempBulb(Bulb):
    @property
    def color_temp(self) -> int:
        return [x for x in self.attributes if "colorTemperature" in x["name"]][0]["currentValue"]

    def set_color_temp(self, level: int):
        """Degrees Kelvin"""
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

    def set_hue(self, hue: int):
        """0-100 valid range"""
        if hue < 0 or hue > 100:
            raise Exception("Invalid range")
        self.send_device_command(command="setHue", secondary_command=str(hue))
        sleep(2)

    def set_saturation(self, saturation: int):
        """0-100 valid range"""
        if saturation < 0 or saturation > 100:
            raise Exception("Invalid range")
        self.send_device_command(command="setSaturation", secondary_command=str(saturation))
        sleep(2)

    def set_color(self, hue: int, saturation: int, level: int):
        if saturation < 0 or saturation > 100:
            raise Exception("Invalid range")
        if level < 0 or level > 100:
            raise Exception("Invalid range")
        if hue < 0 or hue > 100:
            raise Exception("Invalid range")

        color_map = json.dumps({"hue": hue, "saturation": saturation, "level": level})
        self.send_device_command(command="setColor", secondary_command=str(color_map))
        sleep(2)


class ZWavePlusSceneSwitch(Bulb):
    # TODO Add ZWave Plus Scene Switch
    pass
