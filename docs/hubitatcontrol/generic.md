Module hubitatcontrol.generic
=============================

Classes
-------

`Switch(hub: hubitatcontrol.hub.Hub, device_from_hub: dict)`
:   

    ### Ancestors (in MRO)

    * hubitatcontrol.hub.Device

    ### Descendants

    * hubitatcontrol.generic.ZigbeeOutlet
    * hubitatcontrol.lights.Dimmer

    ### Instance variables

    `switch: str`
    :   Returns either (on or off)

    ### Methods

    `turn_off(self)`
    :

    `turn_on(self)`
    :

`ZigbeeOutlet(hub: hubitatcontrol.hub.Hub, device_from_hub: dict)`
:   

    ### Ancestors (in MRO)

    * hubitatcontrol.generic.Switch
    * hubitatcontrol.hub.Device

    ### Instance variables

    `power: int`
    :   Returns power usage