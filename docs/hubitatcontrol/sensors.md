Module hubitatcontrol.sensors
=============================

Classes
-------

`ContactSensor(hub: hubitatcontrol.hub.Hub, device_from_hub: dict)`
:   

    ### Ancestors (in MRO)

    * hubitatcontrol.hub.Device

`EnvironmentalSensor(hub: hubitatcontrol.hub.Hub, device_from_hub: dict)`
:   

    ### Ancestors (in MRO)

    * hubitatcontrol.sensors.TemperatureSensor
    * hubitatcontrol.hub.Device

    ### Class variables

    `spec`
    :

    ### Instance variables

    `humidity: int`
    :

`TemperatureSensor(hub: hubitatcontrol.hub.Hub, device_from_hub: dict)`
:   

    ### Ancestors (in MRO)

    * hubitatcontrol.hub.Device

    ### Descendants

    * hubitatcontrol.environment.Thermostat
    * hubitatcontrol.sensors.EnvironmentalSensor

    ### Class variables

    `spec`
    :

    ### Instance variables

    `temperature: int`
    :