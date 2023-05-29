Module hubitatcontrol.lights
============================

Classes
-------

`Bulb(hub: hubitatcontrol.hub.Hub, device_from_hub: dict)`
:   

    ### Ancestors (in MRO)

    * hubitatcontrol.lights.Dimmer
    * hubitatcontrol.generic.Switch
    * hubitatcontrol.hub.Device

    ### Descendants

    * hubitatcontrol.lights.ColorTempBulb
    * hubitatcontrol.lights.ZWavePlusSceneSwitch

    ### Class variables

    `spec`
    :

`ColorTempBulb(hub: hubitatcontrol.hub.Hub, device_from_hub: dict)`
:   

    ### Ancestors (in MRO)

    * hubitatcontrol.lights.Bulb
    * hubitatcontrol.lights.Dimmer
    * hubitatcontrol.generic.Switch
    * hubitatcontrol.hub.Device

    ### Descendants

    * hubitatcontrol.lights.RGBWBulb

    ### Class variables

    `spec`
    :

    ### Instance variables

    `color_temp: int`
    :

    ### Methods

    `set_color_temp(self, level: int)`
    :   Degrees Kelvin

`Dimmer(hub: hubitatcontrol.hub.Hub, device_from_hub: dict)`
:   

    ### Ancestors (in MRO)

    * hubitatcontrol.generic.Switch
    * hubitatcontrol.hub.Device

    ### Descendants

    * hubitatcontrol.lights.Bulb

    ### Class variables

    `spec`
    :

    ### Instance variables

    `level: int`
    :

    ### Methods

    `set_level(self, level: int)`
    :   0-100 valid range

`RGBWBulb(hub: hubitatcontrol.hub.Hub, device_from_hub: dict)`
:   

    ### Ancestors (in MRO)

    * hubitatcontrol.lights.ColorTempBulb
    * hubitatcontrol.lights.Bulb
    * hubitatcontrol.lights.Dimmer
    * hubitatcontrol.generic.Switch
    * hubitatcontrol.hub.Device

    ### Class variables

    `spec`
    :

    ### Instance variables

    `color: str`
    :

    `color_mode: str`
    :

    `color_name: str`
    :

    `hue: int`
    :

    `saturation: str`
    :

    ### Methods

    `set_color(self, hue: int, saturation: int, level: int)`
    :

    `set_hue(self, hue: int)`
    :   0-100 valid range

    `set_saturation(self, saturation: int)`
    :   0-100 valid range

`ZWavePlusSceneSwitch(hub: hubitatcontrol.hub.Hub, device_from_hub: dict)`
:   

    ### Ancestors (in MRO)

    * hubitatcontrol.lights.Bulb
    * hubitatcontrol.lights.Dimmer
    * hubitatcontrol.generic.Switch
    * hubitatcontrol.hub.Device