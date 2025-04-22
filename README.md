# UCL-Oxide-XY-Controller
Python project to control an X-Y stage from a raspberry pi computer. 

Functional description and setup instructions are available in the file: [manual.pdf](./manual.pdf)

Python module documentation can be found in the folder: [docs](./docs/readme.md)

Change log can be found in the file [changelog.txt](./changelog.txt)


### JSON Commands

| Command | Description                                                  |
|---|--------------------------------------------------------------|
| `{"getxystatus", 1}` | Return the current locations of the x and y steppers         |
| `{"xmove", n}` | move x stepper n steps (-n for backwards) (if n=0 then stop) |
| `{"ymove", n}` | move y stepper n steps (-n for backwards) (if n=0 then stop) |
| `{"xmoveto", n}`| move x stepper to position n (int)                           |
| `{"ymoveto", n}` | move y stepper to position n (int)                      |
| `{"xcalibrate", True}` | Calibrate the x axis |
| `{"ycalibrate", True}` | Calibrate the y axis |
| `{"calibrate-all", True}` | Calibrate the both axes |
| `{"getsettings", True}` | Return the current running settings values |
| `{"updatesetting", {"item": "setting name" : "value": "new value"}}` | Update the settings for the "setting name" with the "new value" |
| `{'restart', 'pi'}` | Restart the raspberry pi after a 15 secodn delay |

