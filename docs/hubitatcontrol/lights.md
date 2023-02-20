# Module hubitatcontrol.lights

## Classes

`Bulb(hub: hubitatcontrol.hub.Hub, device_from_hub: dict)`
:

```
### Ancestors (in MRO)

* hubitatcontrol.lights.Dimmer
* hubitatcontrol.generic.Switch
* hubitatcontrol.hub.Device

### Descendants

* hubitatcontrol.lights.ColorTempBulb
```

`ColorTempBulb(hub: hubitatcontrol.hub.Hub, device_from_hub: dict)`
:

```
### Ancestors (in MRO)

* hubitatcontrol.lights.Bulb
* hubitatcontrol.lights.Dimmer
* hubitatcontrol.generic.Switch
* hubitatcontrol.hub.Device

### Descendants

* hubitatcontrol.lights.RGBWBulb

### Instance variables

`color_temp: int`
:

### Methods

`set_color_temp(self, level: int)`
<<<<<<< HEAD
:   Degrees Kelvin
=======
:
>>>>>>> d949ef7 (Rebase from main)
```

`Dimmer(hub: hubitatcontrol.hub.Hub, device_from_hub: dict)`
:

```
### Ancestors (in MRO)

* hubitatcontrol.generic.Switch
* hubitatcontrol.hub.Device

### Descendants

* hubitatcontrol.lights.Bulb

### Instance variables

`level: int`
:

### Methods

`set_level(self, level: int)`
<<<<<<< HEAD
:   0-100 valid range
=======
:
>>>>>>> d949ef7 (Rebase from main)
```

`RGBWBulb(hub: hubitatcontrol.hub.Hub, device_from_hub: dict)`
:

```
### Ancestors (in MRO)

* hubitatcontrol.lights.ColorTempBulb
* hubitatcontrol.lights.Bulb
* hubitatcontrol.lights.Dimmer
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

`saturation: str`
:

### Methods

<<<<<<< HEAD
`set_color(self)`
:

`set_hue(self, hue: int)`
:   0-100 valid range

`set_saturation(self, saturation: int)`
:   0-100 valid range
=======
`set_color(self, level: str)`
:

`set_hue(self, level: int)`
:

`set_saturation(self, level: int)`
:
>>>>>>> d949ef7 (Rebase from main)
```
