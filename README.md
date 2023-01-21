# Hubitat Elevation Maker API Interface (with Requests)

![GitHub Workflow Status (with branch)](https://img.shields.io/github/actions/workflow/status/jelloeater/hubitatcontrol/test.yml?branch=main)
![GitHub issues by-label](https://img.shields.io/github/issues/jelloeater/hubitatcontrol/bug)
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
```python
from hubitatcontrol import *
h = get_hub(host='Hubitat_IP_or_Hostname', token='Maker_Token', app_id='Maker_App_ID')
d = lookup_device(h, 'Device_Name')
print(d.switch)
d.turn_on()
print(d.switch)
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


## Development setup
**Tooling**
- Need Python > 3.10 Installed
- Doc gen w/ pdoc3 and pyreverse
- Poetry for package management + Build
- Code Complexity with Radon and Xenon
- isort for imports
- Black for formatting
- Vulture for dead code
- Bandit for security
- Testing with PyTest

- **Setup**
- Install Go-Task (<https://taskfile.dev/>)(Optional, it's NEAT!)
  - Linux (`sudo snap install task --classic`)

## Structure

```mermaid
flowchart LR
Hub --> Device --> Abstract_Device_Class --> Specific_Device
```
## Test

```sh
task
```
