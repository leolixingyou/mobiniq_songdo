from typing import NamedTuple


class Actuators(NamedTuple):
    brake: float = 0.0
    steer: float = 0.0
    accel: float = 0.0


class CruiseControl(NamedTuple):
    cancel: bool = False
    resume: bool = False
    override: bool = False


class CANCmd(NamedTuple):
    disable: bool = False
    enable: bool = False
    latActive: bool = False
    longActive: bool = False


class CarControl(NamedTuple):
    canCmd: CANCmd = CANCmd()
    actuators: Actuators = Actuators()
    cruiseControl: CruiseControl = CruiseControl()
