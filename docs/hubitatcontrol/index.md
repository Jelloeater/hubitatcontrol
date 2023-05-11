# Module hubitatcontrol

Hubitat Maker API

## Sub-modules

- hubitatcontrol.environment
- hubitatcontrol.generic
- hubitatcontrol.hub
- hubitatcontrol.lights
- hubitatcontrol.sensors

## Functions

`get_all_environmental_sensors(hub_in: <module 'hubitatcontrol.hub' from '/home/jesse/CodingWorkspace/hubitatcontrol/hubitatcontrol/hub.py'>) ‑> list[hubitatcontrol.sensors.EnvironmentalSensor]`
:   Returns list of all hub devices with associated helper functions

`get_all_temperature_sensors(hub_in: <module 'hubitatcontrol.hub' from '/home/jesse/CodingWorkspace/hubitatcontrol/hubitatcontrol/hub.py'>) ‑> list[hubitatcontrol.sensors.TemperatureSensor]`
:   Returns list of all hub devices with associated helper functions

`get_device_type(device_in: hubitatcontrol.hub.Device, hub_in: <module 'hubitatcontrol.hub' from '/home/jesse/CodingWorkspace/hubitatcontrol/hubitatcontrol/hub.py'>)`
:

`get_hub(host, token, app_id, cloud_token=None) ‑> hubitatcontrol.hub.Hub`
:

`lookup_device(hub_in, device_lookup)`
:   Takes device NAME, not ID for lookup

`lookup_device_id(hub_in, device_id)`
:   Takes device ID for lookup
