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
    * [\_\_read\_switches](#steppercontrol.StepperClass.__read_switches)
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

Main controller classes. Has a class to manage a single stepper so is called twice once for X and once for Y.
It also contains an API Request parser that directs messages to the correct function and stepper based on the
API request.

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

Class to control a stepper motor for a single axis

<a id="steppercontrol.StepperClass.__init__"></a>

#### \_\_init\_\_

```python
def __init__(direction, a, aa, b, bb, limmax, limmin, moveled)
```

<a id="steppercontrol.StepperClass.__read_switches"></a>

#### \_\_read\_switches

```python
def __read_switches()
```

A threaded method that continually reads the max and min limit switch status. If a limit is reached and
the stepper is not calibrating, this function will stop the stepper. The function also sets a flashing LED on
the front panel of the controller to show the stepper is moving

<a id="steppercontrol.StepperClass.current"></a>

#### current

```python
def current()
```

Return current sequence, only used for debugging

<a id="steppercontrol.StepperClass.movenext"></a>

#### movenext

```python
def movenext()
```

Move +1 step towards the maximum, if the maximum value has been reached it will not move further

<a id="steppercontrol.StepperClass.moveprevious"></a>

#### moveprevious

```python
def moveprevious()
```

Move -1 step towards the minimum, if the minimum value has been reached it will not move further.

<a id="steppercontrol.StepperClass.updateposition"></a>

#### updateposition

```python
def updateposition()
```

write the stepper position to the settings file

<a id="steppercontrol.StepperClass.stop"></a>

#### stop

```python
def stop()
```

Stop the stepper motor and set the coils to 0, also update the position of the stepper and write to
the settings file

<a id="steppercontrol.StepperClass.move"></a>

#### move

```python
def move(steps)
```

Move **n steps** at full speed

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

Moves the axis to the specified target position within its limits.

This method initiates the movement process for the axis motor to reach the
desired target position. The movement continues as long as the motor is in
motion and has not been interrupted by external control. The method checks
if the target position is within the specified range of lower and upper limits
and adjusts the motor position incrementally. It stops the motion and updates
the motor status accordingly when the target is reached or the sequence changes.

:param target: Desired position to move the axis to.
:type target: int or float
:return: None

<a id="steppercontrol.StepperClass.output"></a>

#### output

```python
def output(channels)
```

Output the value to the coils on the stepper

<a id="steppercontrol.StepperClass.calibrate"></a>

#### calibrate

```python
def calibrate()
```

Run a calibration routine to find the man and max limit switches and reset the position of the stage. The
routine will move the stepper backward as far as the minimum switch is triggered, it will then slowly move the
stepper forward until the switch is just released. This position is then recorded as zero. The stepper will
then be moved forward unti the maximum limit is triggeed, then move backward until the switch is released,
this position (- 10 steps) is stored as the maximum value. The routine then calculates the centre position and
moves the stepper to that position. When calibrating the read() method will not stop the motor when a limit
switch is triggered

<a id="steppercontrol.statusmessage"></a>

#### statusmessage

```python
def statusmessage()
```

Return the psotion and stepper status in a format that can be read by the web page

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

Update the settings variable and file with the new values from an api call

<a id="steppercontrol.parsecontrol"></a>

#### parsecontrol

```python
def parsecontrol(item, command)
```

Parser that recieves messages from the API or web page posts and directs messages to the correct function:
Valid messages are:
getxystatus: returns the current position of the steppers
(axis)move: moves the stepper axis by the number of steps specified
(axix)moveto: moves the stepper axis to the position specified
(axis)calibrate: calibrates the stepper axis
calibrate-all: calibrates both axes
output: sets the coils on the stepper to the value specified (used foir testing ta stepper motor
getsettings: returns the current settings in a json format
updatesetting: updates the settings file with the new values specified in a json object
restart: restarts the raspberry pi

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

