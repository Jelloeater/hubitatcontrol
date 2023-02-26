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


class Thermostat(Device):
    def set_temperature(self):
        raise NotImplementedError


class EcoBee(Thermostat):
    # TODO Need to implement generic and EcoBee specific functions
    pass


class GenericZWaveLock(Device):
    # TODO Add ZWave lock
    def lock(self):
        raise NotImplementedError

    def unlock(self):
        raise NotImplementedError


class Button(Device):
    pass


class SonoffZigbeeButtonController(Button):
    # TODO Add button properties
    pass
