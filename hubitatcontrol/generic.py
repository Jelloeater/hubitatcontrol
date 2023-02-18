from hubitatcontrol.hub import Device


class Switch(Device):
    @property
    def switch(self) -> str:
        """Returns either (on or off)"""
        return [x for x in self.attributes if "switch" in x["name"]][0]["currentValue"]

    def turn_on(self):
        self.send_device_command(command="on")

    def turn_off(self):
        self.send_device_command(command="off")


class ZigbeeOutlet(Switch):
    @property
    def power(self) -> int:
        """Returns power usage"""
        return [x for x in self.attributes if "power" in x["name"]][0]["currentValue"]
