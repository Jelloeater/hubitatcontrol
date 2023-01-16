from hubitatcontrol.hub import Device


class Bulb(Device):
    @property
    def switch(self):
        return [x for x in self.attributes if "switch" in x["name"]][0]['currentValue']

    @property
    def level(self):
        return [x for x in self.attributes if "level" in x["name"]][0]['currentValue']

    def turn_on(self):
        self.send_device_command(command='on')

    def turn_off(self):
        self.send_device_command(command='off')


class Advanced_Zigbee_RGBW_Bulb(Bulb):
    @property
    def color_mode(self):
        return [x for x in self.attributes if "colorMode" in x["name"]][0]['currentValue']

    @property
    def color_name(self):
        return [x for x in self.attributes if "colorName" in x["name"]][0]['currentValue']

    @property
    def color(self):
        return [x for x in self.attributes if "color" in x["name"]][0]['currentValue']

    @property
    def color_temp(self):
        return [x for x in self.attributes if "colorTemperature" in x["name"]][0]['currentValue']

    @property
    def hue(self):
        return [x for x in self.attributes if "hue" in x["name"]][0]['currentValue']
