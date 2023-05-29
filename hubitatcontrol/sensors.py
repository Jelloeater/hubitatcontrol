from hubitatcontrol.hub import Device


class ContactSensor(Device):
    # TODO Add contact sensor properties
    pass


class TemperatureSensor(Device):
    spec = ["TemperatureMeasurement"]

    @property
    def temperature(self) -> int:
        return [x for x in self.attributes if "temperature" in x["name"]][0]["currentValue"]


class EnvironmentalSensor(TemperatureSensor):
    spec = ["RelativeHumidityMeasurement", "TemperatureMeasurement"]

    @property
    def humidity(self) -> int:
        return [x for x in self.attributes if "humidity" in x["name"]][0]["currentValue"]
