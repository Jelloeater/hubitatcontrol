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
:

```
### Methods

`cast_device(self)`
:   The order here is very important that we cast the device properly based on increasing complexity /
    functionality
```

`GetDevices(hub_in: hubitatcontrol.hub.Hub)`
:

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

`GetSingleDevice()`
:

```
### Static methods

`name(device_name: str)`
:
```
