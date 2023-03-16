# Module hubitatcontrol.hub

## Classes

`Device(hub: hubitatcontrol.hub.Hub, device_from_hub: dict)`
:

```
### Descendants

* hubitatcontrol.generic.Button
* hubitatcontrol.generic.GenericZWaveLock
* hubitatcontrol.generic.Switch
* hubitatcontrol.generic.Thermostat
* hubitatcontrol.sensors.ContactSensor
* hubitatcontrol.sensors.TemperatureSensor

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
```

`Hub(host, token, app_id, cloud_token=None)`
:

```
### Instance variables

`devices: list`
:

### Methods

`get_device(self, name: str)`
:
```
