# Contents for: steppercontrol

* [steppercontrol](#steppercontrol)
  * [threading](#steppercontrol.threading)
  * [sleep](#steppercontrol.sleep)
  * [os](#steppercontrol.os)
  * [Timer](#steppercontrol.Timer)
  * [GPIO](#steppercontrol.GPIO)
  * [logger](#steppercontrol.logger)
  * [settings](#steppercontrol.settings)
  * [writesettings](#steppercontrol.writesettings)
  * [StepperClass](#steppercontrol.StepperClass)
    * [\_\_init\_\_](#steppercontrol.StepperClass.__init__)
    * [read\_switches](#steppercontrol.StepperClass.read_switches)
    * [current](#steppercontrol.StepperClass.current)
    * [movenext](#steppercontrol.StepperClass.movenext)
    * [moveprevious](#steppercontrol.StepperClass.moveprevious)
    * [updateposition](#steppercontrol.StepperClass.updateposition)
    * [stop](#steppercontrol.StepperClass.stop)
    * [move](#steppercontrol.StepperClass.move)
    * [moveslow](#steppercontrol.StepperClass.moveslow)
    * [moveto](#steppercontrol.StepperClass.moveto)
    * [output](#steppercontrol.StepperClass.output)
    * [calibrate](#steppercontrol.StepperClass.calibrate)
  * [statusmessage](#steppercontrol.statusmessage)
  * [apistatus](#steppercontrol.apistatus)
  * [updatesetting](#steppercontrol.updatesetting)
  * [parsecontrol](#steppercontrol.parsecontrol)
  * [reboot](#steppercontrol.reboot)
  * [stepperx](#steppercontrol.stepperx)
  * [steppery](#steppercontrol.steppery)

<a id="steppercontrol"></a>

# steppercontrol

Main controller classes

<a id="steppercontrol.threading"></a>

## threading

<a id="steppercontrol.sleep"></a>

## sleep

<a id="steppercontrol.os"></a>

## os

<a id="steppercontrol.Timer"></a>

## Timer

<a id="steppercontrol.GPIO"></a>

## GPIO

<a id="steppercontrol.logger"></a>

## logger

<a id="steppercontrol.settings"></a>

## settings

<a id="steppercontrol.writesettings"></a>

## writesettings

<a id="steppercontrol.StepperClass"></a>

## StepperClass Objects

```python
class StepperClass()
```

Class to control a stepper motor

<a id="steppercontrol.StepperClass.__init__"></a>

#### \_\_init\_\_

```python
def __init__(direction, a, aa, b, bb, limmax, limmin, moveled)
```

<a id="steppercontrol.StepperClass.read_switches"></a>

#### read\_switches

```python
def read_switches()
```

Read the switch values

<a id="steppercontrol.StepperClass.current"></a>

#### current

```python
def current()
```

Return current sequence, used for debugging

<a id="steppercontrol.StepperClass.movenext"></a>

#### movenext

```python
def movenext()
```

Move +1 step

<a id="steppercontrol.StepperClass.moveprevious"></a>

#### moveprevious

```python
def moveprevious()
```

Move -1 step

<a id="steppercontrol.StepperClass.updateposition"></a>

#### updateposition

```python
def updateposition()
```

write the position to the settings file

<a id="steppercontrol.StepperClass.stop"></a>

#### stop

```python
def stop()
```

Stop moving

<a id="steppercontrol.StepperClass.move"></a>

#### move

```python
def move(steps)
```

Move **steps** at full speed

<a id="steppercontrol.StepperClass.moveslow"></a>

#### moveslow

```python
def moveslow(steps)
```

Move **steps** slowly

<a id="steppercontrol.StepperClass.moveto"></a>

#### moveto

```python
def moveto(target)
```

Move the motor to a specific target value on the ADC

<a id="steppercontrol.StepperClass.output"></a>

#### output

```python
def output(channels)
```

Output the value to thE coils on the stepper

<a id="steppercontrol.StepperClass.calibrate"></a>

#### calibrate

```python
def calibrate()
```

Run a calibration routine to find the man and max limit switches and reset the position of the stage

<a id="steppercontrol.statusmessage"></a>

#### statusmessage

```python
def statusmessage()
```

Return the psotion status to the web page

<a id="steppercontrol.apistatus"></a>

#### apistatus

```python
def apistatus()
```

Return the status as a json message for the api

<a id="steppercontrol.updatesetting"></a>

#### updatesetting

```python
def updatesetting(newsetting)
```

Update the settings with the new values

<a id="steppercontrol.parsecontrol"></a>

#### parsecontrol

```python
def parsecontrol(item, command)
```

Parser that recieves messages from the API or web page posts and directs messages to the correct function

<a id="steppercontrol.reboot"></a>

#### reboot

```python
def reboot()
```

API call to reboot the Raspberry Pi

<a id="steppercontrol.stepperx"></a>

#### stepperx

<a id="steppercontrol.steppery"></a>

#### steppery

