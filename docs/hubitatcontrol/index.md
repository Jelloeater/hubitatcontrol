# Module hubitatcontrol

Hubitat Maker API

## Sub-modules

- hubitatcontrol.environment
- hubitatcontrol.generic
- hubitatcontrol.hub
- hubitatcontrol.lights
- hubitatcontrol.sensors

## Functions

`get_hub_envs() ‑> hubitatcontrol.hub.Hub`
:   Generates a Hub object from local environmental variables

## Classes

`DeviceInit(hub_in: hubitatcontrol.hub.Hub, device_in: hubitatcontrol.hub.Device)`
:   This class is normally not used, as it's for dynamically casting devices

```
### Methods

`cast_device(self)`
:   The order here is very important that we cast the device properly based on increasing complexity /
    functionality
```

`GetDevices(hub_in: hubitatcontrol.hub.Hub)`
:   Get a list of pre-casted devices you can search though

```
### Methods

`Bulb(self) ‑> list[hubitatcontrol.lights.Bulb]`
:

`ColorTempBulb(self) ‑> list[hubitatcontrol.lights.ColorTempBulb]`
:

`Dimmer(self) ‑> list[hubitatcontrol.lights.Dimmer]`
:

`EnvironmentalSensor(self) ‑> list[hubitatcontrol.sensors.EnvironmentalSensor]`
:

`Outlet(self) ‑> list[hubitatcontrol.generic.ZigbeeOutlet]`
:

`RGBWBulb(self) ‑> list[hubitatcontrol.lights.RGBWBulb]`
:

`Switch(self) ‑> list[hubitatcontrol.generic.Switch]`
:

`TemperatureSensor(self) ‑> list[hubitatcontrol.sensors.TemperatureSensor]`
:
```

`GetSingleDevice(hub_in: hubitatcontrol.hub.Hub)`
:   Used to get a single device based on lookup

```
### Methods

`id(self, device_id: int)`
:   Get a device by id and cast to the matched spec

`name(self, device_name: str)`
:   Get a device by name and cast to the matched spec
```
