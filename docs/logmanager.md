# Contents for: logmanager

* [logmanager](#logmanager)
  * [os](#logmanager.os)
  * [sys](#logmanager.sys)
  * [logging](#logmanager.logging)
  * [RotatingFileHandler](#logmanager.RotatingFileHandler)
  * [settings](#logmanager.settings)
  * [log\_dir](#logmanager.log_dir)
  * [logger](#logmanager.logger)
  * [LogFile](#logmanager.LogFile)
  * [formatter](#logmanager.formatter)

<a id="logmanager"></a>

# logmanager

Sets up the application logging. if it does not exist it creates a logs folder and a log file.
Log files are rotated at 1Mbyte intervals and the past 10 files are retained.

<a id="logmanager.os"></a>

## os

<a id="logmanager.sys"></a>

## sys

<a id="logmanager.logging"></a>

## logging

<a id="logmanager.RotatingFileHandler"></a>

## RotatingFileHandler

<a id="logmanager.settings"></a>

## settings

<a id="logmanager.log_dir"></a>

#### log\_dir

<a id="logmanager.logger"></a>

#### logger

Usage:

**logger.info('message')** for info messages

**logger.warning('message')** for warnings

**logger.error('message')** for errors

<a id="logmanager.LogFile"></a>

#### LogFile

<a id="logmanager.formatter"></a>

#### formatter

