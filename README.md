# PyMS  XY Controller Service
A Flask-based control system for managing an X-Y stage using a Raspberry Pi. This application provides precise control over two-axis movement through a web interface and API endpoints.

## Features

- Real-time X-Y stage position control
- REST API for automated control
- GPIO-based stepper motor control
- Secure API key authentication
- Configurable movement parameters

## Setup information
The functional description and setup instructions are available in the file: [manual.pdf](./manual.pdf)

## Documentation
Python module documentation can be found in the folder: [docs](./docs/readme.md)
Change log can be found in the file [changelog.txt](./changelog.txt)


## Usage
The api is managed by sending the following json messages in a [POST] to  serveraddress/api

| Command | Description                                                     |
|---|-----------------------------------------------------------------|
| `{"getxystatus", 1}` | Return the current locations of the x and y steppers            |
| `{"xmove", n}` | move x stepper n steps (-n for backwards) (if n=0 then stop)    |
| `{"ymove", n}` | move y stepper n steps (-n for backwards) (if n=0 then stop)    |
| `{"xmoveto", n}`| move x stepper to position n (int)                              |
| `{"ymoveto", n}` | move y stepper to position n (int)                              |
| `{"xcalibrate", True}` | Calibrate the x axis                                            |
| `{"ycalibrate", True}` | Calibrate the y axis                                            |
| `{"calibrate-all", True}` | Calibrate the both axes                                         |
| `{"getsettings", True}` | Return the current running settings values                      |
| `{"updatesetting", {"item": "setting name" : "value": "new value"}}` | Update the settings for the "setting name" with the "new value" |



&nbsp;   
&nbsp;    
&nbsp;  
&nbsp;   
&nbsp;   
&nbsp;   
--------------

#### Copyright (C) 2025 Gary Twinn

This program is free software: you can redistribute it and/or modify  
it under the terms of the GNU General Public License as published by  
the Free Software Foundation, either version 3 of the License, or  
(at your option) any later version.  

This program is distributed in the hope that it will be useful,  
but WITHOUT ANY WARRANTY; without even the implied warranty of  
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the  
GNU General Public License for more details.  

You should have received a copy of the GNU General Public License  
along with this program. If not, see <https://www.gnu.org/licenses/>.


Author:  Gary Twinn  
Repository:  [github.com/westerlymerlin](https://github)

-------------

