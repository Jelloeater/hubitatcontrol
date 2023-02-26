# Module hubitatcontrol.generic

## Classes

`Button(hub: hubitatcontrol.hub.Hub, device_from_hub: dict)`
:

```
### Ancestors (in MRO)

* hubitatcontrol.hub.Device

### Descendants

* hubitatcontrol.generic.SonoffZigbeeButtonController
```

`EcoBee(hub: hubitatcontrol.hub.Hub, device_from_hub: dict)`
:

```
### Ancestors (in MRO)

* hubitatcontrol.generic.Thermostat
* hubitatcontrol.hub.Device
```

`GenericZWaveLock(hub: hubitatcontrol.hub.Hub, device_from_hub: dict)`
:

```
### Ancestors (in MRO)

* hubitatcontrol.hub.Device

### Methods

`lock(self)`
:

`unlock(self)`
:
```

`SonoffZigbeeButtonController(hub: hubitatcontrol.hub.Hub, device_from_hub: dict)`
:

```
### Ancestors (in MRO)

* hubitatcontrol.generic.Button
* hubitatcontrol.hub.Device
```

`Switch(hub: hubitatcontrol.hub.Hub, device_from_hub: dict)`
:

```
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
```

`Thermostat(hub: hubitatcontrol.hub.Hub, device_from_hub: dict)`
:

```
### Ancestors (in MRO)

* hubitatcontrol.hub.Device

### Descendants

* hubitatcontrol.generic.EcoBee

### Methods

`set_temperature(self)`
:
```

`ZigbeeOutlet(hub: hubitatcontrol.hub.Hub, device_from_hub: dict)`
:

```
### Ancestors (in MRO)

* hubitatcontrol.generic.Switch
* hubitatcontrol.hub.Device

### Instance variables

`power: int`
:   Returns power usage
```
