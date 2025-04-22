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
Logging Configuration and Management

This module provides centralized logging configuration and management for the application.
Configures logging formats, handlers, and log file management to ensure consistent
logging across all application components.

Features:
    - Standardized log formatting
    - File-based logging with rotation
    - Log level management
    - Thread-safe logging operations

Exports:
    logger: Configured logger instance for use across the application

Usage:
    from logmanager import logger

    logger.info('Operation completed successfully')
    logger.warning('Resource threshold reached')
    logger.error('Failed to complete operation')

Log Format:
    Timestamps, log levels, and contextual information are automatically included
    in each log entry for effective debugging and monitoring.

Log Files:
    Logs are stored with automatic rotation to prevent excessive disk usage
    while maintaining historical records.

[steppercontrol](./steppercontrol.md)  
Main controller classes. Has a class to manage a single stepper so is called twice once for X and once for Y.
It also contains an API Request parser that directs messages to the correct function and stepper based on the
API request.


---

