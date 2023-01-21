# Hubitat Elevation Maker API Interface (with Requests)

![GitHub Workflow Status (with branch)](https://img.shields.io/github/actions/workflow/status/jelloeater/hubitatcontrol/test.yml?branch=main)
![GitHub issues by-label](https://img.shields.io/github/issues/jelloeater/hubitatcontrol/bug)
![GitHub pull requests](https://img.shields.io/github/issues-pr/jelloeater/hubitatcontrol)
[![Libraries.io dependency status for latest release](https://img.shields.io/librariesio/release/pypi/hubitatcontrol)](https://libraries.io/pypi/hubitatcontrol)
![GitHub](https://img.shields.io/github/license/jelloeater/hubitatcontrol)

[![Packaged with Poetry](https://img.shields.io/badge/packaging-poetry-cyan.svg)](https://python-poetry.org/)
[![PyPI version](https://badge.fury.io/py/hubitatcontrol.svg)](https://badge.fury.io/py/hubitatcontrol)
![PyPI - Format](https://img.shields.io/pypi/format/hubitatcontrol)
![PyPI - Status](https://img.shields.io/pypi/status/hubitatcontrol)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org)
![GitHub top language](https://img.shields.io/github/languages/top/jelloeater/hubitatcontrol)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/jelloeater/hubitatcontrol)
![Lines of code](https://img.shields.io/tokei/lines/github/jelloeater/hubitatcontrol)


## Usage
```shell
pip install hubitatcontrol
```

```python
import hubitatcontrol as hc

hub = hc.get_hub(host='Hubitat_IP_or_Hostname', token='Maker_Token', app_id='Maker_App_ID')
device = hc.lookup_device(hub, 'Device_Name')

print(device.switch)
device.turn_on()
print(device.switch)
```

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

```mermaid
flowchart LR
Specific_Device --> Abstract_Device_Class --> Device--> Hub
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
