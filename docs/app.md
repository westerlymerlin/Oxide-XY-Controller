# Contents for: app

* [app](#app)
  * [subprocess](#app.subprocess)
  * [enumerate\_threads](#app.enumerate_threads)
  * [Flask](#app.Flask)
  * [render\_template](#app.render_template)
  * [jsonify](#app.jsonify)
  * [request](#app.request)
  * [statusmessage](#app.statusmessage)
  * [parsecontrol](#app.parsecontrol)
  * [VERSION](#app.VERSION)
  * [settings](#app.settings)
  * [logger](#app.logger)
  * [app](#app.app)
  * [read\_log\_from\_file](#app.read_log_from_file)
  * [read\_cpu\_temperature](#app.read_cpu_temperature)
  * [threadlister](#app.threadlister)
  * [index](#app.index)
  * [statusdata](#app.statusdata)
  * [api](#app.api)
  * [showplogs](#app.showplogs)
  * [showgalogs](#app.showgalogs)
  * [showgelogs](#app.showgelogs)
  * [showslogs](#app.showslogs)

<a id="app"></a>

# app

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

<a id="app.subprocess"></a>

## subprocess

<a id="app.enumerate_threads"></a>

## enumerate\_threads

<a id="app.Flask"></a>

## Flask

<a id="app.render_template"></a>

## render\_template

<a id="app.jsonify"></a>

## jsonify

<a id="app.request"></a>

## request

<a id="app.statusmessage"></a>

## statusmessage

<a id="app.parsecontrol"></a>

## parsecontrol

<a id="app.VERSION"></a>

## VERSION

<a id="app.settings"></a>

## settings

<a id="app.logger"></a>

## logger

<a id="app.app"></a>

#### app

<a id="app.read_log_from_file"></a>

#### read\_log\_from\_file

```python
def read_log_from_file(file_path)
```

Read a log from a file and reverse the order of the lines so newest is at the top

<a id="app.read_cpu_temperature"></a>

#### read\_cpu\_temperature

```python
def read_cpu_temperature()
```

Read the CPU temperature and teturns in in Celcius

<a id="app.threadlister"></a>

#### threadlister

```python
def threadlister()
```

Get a list of all threads running

<a id="app.index"></a>

#### index

```python
@app.route('/')
def index()
```

Main web status page

<a id="app.statusdata"></a>

#### statusdata

```python
@app.route('/statusdata', methods=['GET'])
def statusdata()
```

Status data read by javascript on default website so the page shows near live values

<a id="app.api"></a>

#### api

```python
@app.route('/api', methods=['POST'])
def api()
```

API Endpoint for programatic access - needs request data to be posted in a json file. Contains a check for a
valid API key.

<a id="app.showplogs"></a>

#### showplogs

```python
@app.route('/pylog')
def showplogs()
```

Show the Application log web page

<a id="app.showgalogs"></a>

#### showgalogs

```python
@app.route('/guaccesslog')
def showgalogs()
```

"Show the Gunicorn Access Log web page

<a id="app.showgelogs"></a>

#### showgelogs

```python
@app.route('/guerrorlog')
def showgelogs()
```

"Show the Gunicorn Errors Log web page

<a id="app.showslogs"></a>

#### showslogs

```python
@app.route('/syslog')
def showslogs()
```

Show the last 2000 lines from the system log on a web page

