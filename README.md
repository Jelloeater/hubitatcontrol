# Hubitat Elevation Maker API Interface

[![Test](https://github.com/Jelloeater/hubitatcontrol/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/Jelloeater/hubitatcontrol/actions/workflows/test.yml)
[![CodeQL](https://github.com/Jelloeater/hubitatcontrol/actions/workflows/codeql.yml/badge.svg?branch=main)](https://github.com/Jelloeater/hubitatcontrol/actions/workflows/codeql.yml)
[![Libraries.io dependency status for latest release](https://img.shields.io/librariesio/release/pypi/hubitatcontrol)](https://libraries.io/pypi/hubitatcontrol)

![PyPI - Status](https://img.shields.io/pypi/status/hubitatcontrol)
[![PyPI](https://img.shields.io/pypi/v/hubitatcontrol)](https://pypi.org/project/hubitatcontrol/)
[![GitHub](https://img.shields.io/github/license/jelloeater/hubitatcontrol)](https://github.com/Jelloeater/hubitatcontrol/blob/main/LICENSE)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org)

## Usage

```shell
pip install hubitatcontrol
```

**Or if you want a copy direct from source**

```shell
pip install git+https://github.com/Jelloeater/hubitatcontrol.git
```

```python
import hubitatcontrol as hc

hub = hc.get_hub(host='Hubitat_IP_or_Hostname', token='Maker_Token', app_id='Maker_App_ID')
device = hc.lookup_device(hub, 'Device_Name')

print(device.switch)
device.turn_on()
print(device.switch)
```

## Docs

[Located in /docs folder](docs)

You will need a .dot file browser for the class diagrams

## Roadmap

### v0.5

- [X] Advanced Zigbee RGBW Bulb

### v0.7

- [X] Generic Zigbee Outlet

### v0.8

- [X] Leviton DZ6HD Z-Wave Dimmer

### v1.0

- [ ] hueBridgeBulb

### v1.1

- [ ] hueBridgeBulbCT

### v1.2

- [ ] hueBridgeBulbRGBW

### v1.5

- [ ] Ecobee Thermostat

### v2.0

- [ ] Generic Z-Wave Lock

### v2.5

- [ ] Generic Z-Wave Plus Scene Switch

### v2.6

- [ ] Generic Zigbee Contact Sensor (no temp)
- [ ] Sonoff Zigbee Button Controller

## Structure

**Class Model**

```mermaid
flowchart LR
Specific_Device --> Abstract_Device_Class --> Device--> Hub
```

**Capability Model**

*Bulb*

```mermaid
flowchart TD
subgraph Advanced_Zigbee_RGBW_Bulb
ColorControl & ColorMode
end
subgraph ColorTempBulb
end
ColorTemperature
subgraph Bulb
ChangeLevel
end

Advanced_Zigbee_RGBW_Bulb --> ColorTempBulb --> Bulb
```

*Outlet*

```mermaid
flowchart TD
Outlet & Actuator & Switch
```


## Development setup

Testing is done with PyTest, you will need to set up the correct env vars for your local (or cloud) Hubitat API
See `.env.example`

**Setup**

Install Go-Task --> <https://taskfile.dev/installation/>

```shell
task setup
task
```
