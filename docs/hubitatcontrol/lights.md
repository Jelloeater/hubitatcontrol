Module hubitatcontrol.lights
============================

Classes
-------

`Advanced_Zigbee_RGBW_Bulb(hub: hubitatcontrol.hub.Hub, device_from_hub: dict)`
:   

    ### Ancestors (in MRO)

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

    `color_temp: int`
    :

    `hue: int`
    :

`Bulb(hub: hubitatcontrol.hub.Hub, device_from_hub: dict)`
:   

    ### Ancestors (in MRO)

    * hubitatcontrol.generic.Switch
    * hubitatcontrol.hub.Device

    ### Descendants

    * hubitatcontrol.lights.Advanced_Zigbee_RGBW_Bulb

    ### Instance variables

    `level: int`
    :

    ### Methods

    `flash(self)`
    :

    `set_level(self, level: int)`
    :