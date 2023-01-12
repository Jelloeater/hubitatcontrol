Module src.hubitatcontrol
=========================
Hubitat Maker API

Classes
-------

`Bulb(hub, device_from_hub)`
:   

    ### Ancestors (in MRO)

    * src.hubitatcontrol.Device

    ### Instance variables

    `switch`
    :

    ### Methods

    `turn_off(self)`
    :

    `turn_on(self)`
    :

`Device(hub: src.hubitatcontrol.Hub, device_from_hub: dict)`
:   

    ### Descendants

    * src.hubitatcontrol.Bulb

    ### Instance variables

    `attributes: requests.models.Response`
    :

    `capabilities`
    :

    `commands`
    :

    `history: requests.models.Response`
    :

    ### Methods

    `send_device_command(self, command: str, secondary_command: str = None) ‑> requests.models.Response`
    :

`Hub(host, token, app_id, cloud_id=None)`
:   

    ### Instance variables

    `devices: list`
    :

    ### Methods

    `get_device(self, name: str) ‑> dict`
    :