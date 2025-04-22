# Module Documentation


This document contains the documentation for all the modules in the **Oxide X-Y Stage Controler** version 1.0.6 application.

---

## Contents


[app](./app.md)  
Flask web application for Raspberry Pi system monitoring and control.

This module provides a web interface and API endpoints for monitoring and controlling
a Raspberry Pi system. It includes features for:
- System status monitoring (CPU temperature, running threads)
- Log viewing (Application, Gunicorn, System logs)
- RESTful API endpoints with authentication
- Real-time status updates via JavaScript

The application runs on Gunicorn when deployed on Raspberry Pi and includes
various endpoints for both web interface and programmatic access.

Routes:
    / : Main status page
    /statusdata : JSON endpoint for live status updates
    /api : Protected API endpoint for system control
    /pylog : Application log viewer
    /guaccesslog : Gunicorn access log viewer
    /guerrorlog : Gunicorn error log viewer
    /syslog : System log viewer

Authentication:
    API endpoints require a valid API key passed in the 'Api-Key' header.

[app_control](./app_control.md)  
Application control and configuration management for the Raspberry Pi control system.

This module manages core application configuration, settings, and version information
for the Flask-based control system. It handles loading and maintaining application-wide
settings that define crucial operational parameters.

Attributes:
    VERSION (str): The current version of the application
    settings (dict): Application-wide configuration dictionary containing:
        - app-name (str): Application identifier used in logging and display
        - api-key (str): Authentication key for API access control
        - cputemp (str): File path for CPU temperature readings
        - logfilepath (str): Path to application log file
        - gunicornpath (str): Base directory for Gunicorn log files

Note:
    This module is a central configuration point for the application and should
    be imported by other modules that need access to global settings or version
    information.

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
Stepper motor control interface for Raspberry Pi hardware control system.

This module provides functionality to control and monitor stepper motors connected
to the Raspberry Pi. It handles both status reporting and command parsing for
motor control operations.

Functions:
    statusmessage() -> dict:
        Returns the current status of all stepper motors in the system.
        The status includes position, state, and other relevant motor parameters.
        Returns:
            dict: Current status of the stepper motors

    parsecontrol(item: str, command: str) -> dict:
        Parses and executes control commands for specified stepper motor.

        Args:
            item (str): The identifier of the stepper motor to control
            command (str): The control command to execute

        Returns:
            dict: Result of the control operation including status and any error messages

Note:
    This module interfaces directly with hardware components and should be used
    with appropriate driver board to prevent mechanical issues.


---

