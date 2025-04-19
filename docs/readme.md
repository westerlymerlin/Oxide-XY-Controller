# Module Documentation


This document contains the documentation for all the modules in the **Oxide X-Y Stage Controler** version 1.0.6 application.

---

## Contents


[app](./app.md)  
This is the main flask applicaton, on the Raspberry Pi it runs on Gunicorn.

[app_control](./app_control.md)  
Settings module, reads the settings from a settings.json file. If it does not exist or a new setting
has appeared it will create from the defaults in the initialise function.

[logmanager](./logmanager.md)  
Sets up the application logging. if it does not exist it creates a logs folder and a log file.
Log files are rotated at 1Mbyte intervals and the past 10 files are retained.

[steppercontrol](./steppercontrol.md)  
Main controller classes. Has a class to manage a single stepper so is called twice once for X and once for Y.
It also contains an API Request parser that directs messages to the correct function and stepper based on the
API request.


---

