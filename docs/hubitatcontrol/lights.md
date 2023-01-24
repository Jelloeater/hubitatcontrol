Module hubitatcontrol.lights
============================

Classes
-------

`Bulb(hub: hubitatcontrol.hub.Hub, device_from_hub: dict)`
:   

    ### Ancestors (in MRO)

    * hubitatcontrol.generic.Switch
    * hubitatcontrol.hub.Device

    ### Descendants

    * hubitatcontrol.lights.ColorTempBulb

    ### Instance variables

    `level: int`
    :

    ### Methods

    `set_level(self, level: int)`
    :

`ColorTempBulb(hub: hubitatcontrol.hub.Hub, device_from_hub: dict)`
:   

    ### Ancestors (in MRO)

    * hubitatcontrol.lights.Bulb
    * hubitatcontrol.generic.Switch
    * hubitatcontrol.hub.Device

    ### Descendants

    * hubitatcontrol.lights.RGBWBulb

    ### Instance variables

    `color_temp: int`
    :

    ### Methods

    `set_color_temp(self, level: int)`
    :

`RGBWBulb(hub: hubitatcontrol.hub.Hub, device_from_hub: dict)`
:   

    ### Ancestors (in MRO)

    * hubitatcontrol.lights.ColorTempBulb
    * hubitatcontrol.lights.Bulb
    * hubitatcontrol.generic.Switch
    * hubitatcontrol.hub.Device

    ### Instance variables

    `color: str`
    :

    `color_mode: str`
    :

    `color_name: str`
    :

    `hue: int`
    :

    ### Methods

    `set_color(self, level: str)`
    :

    `set_hue(self, level: int)`
    :

    `set_saturation(self, level: int)`
    :