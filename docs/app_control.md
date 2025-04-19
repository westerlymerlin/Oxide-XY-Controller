# Contents for: app_control

* [app\_control](#app_control)
  * [random](#app_control.random)
  * [json](#app_control.json)
  * [datetime](#app_control.datetime)
  * [VERSION](#app_control.VERSION)
  * [initialise](#app_control.initialise)
  * [generate\_api\_key](#app_control.generate_api_key)
  * [writesettings](#app_control.writesettings)
  * [readsettings](#app_control.readsettings)
  * [loadsettings](#app_control.loadsettings)
  * [settings](#app_control.settings)

<a id="app_control"></a>

# app\_control

Settings module, reads the settings from a settings.json file. If it does not exist or a new setting
has appeared it will create from the defaults in the initialise function.

<a id="app_control.random"></a>

## random

<a id="app_control.json"></a>

## json

<a id="app_control.datetime"></a>

## datetime

<a id="app_control.VERSION"></a>

#### VERSION

<a id="app_control.initialise"></a>

#### initialise

```python
def initialise()
```

Setup the settings dict structure with default values

<a id="app_control.generate_api_key"></a>

#### generate\_api\_key

```python
def generate_api_key(key_len)
```

generate a new random api-key

<a id="app_control.writesettings"></a>

#### writesettings

```python
def writesettings()
```

Write settings to a json file

<a id="app_control.readsettings"></a>

#### readsettings

```python
def readsettings()
```

Read the json file

<a id="app_control.loadsettings"></a>

#### loadsettings

```python
def loadsettings()
```

Replace the default settings with thsoe from the json files, if a setting is not in the json file (e.g. it is a
 new feature setitng) then retain the default value and write that to the json file. If the api-key is the default
value then generate a new key and save it.

<a id="app_control.settings"></a>

#### settings

