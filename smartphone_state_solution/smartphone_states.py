"""Smartphone states."""

from abc import ABC, abstractmethod


class SmartPhoneState(ABC):
  def __init__(self, context):
    self._ctx = context

  @abstractmethod
  def in_call(self, phone_number: str) -> str:
    pass

  @abstractmethod
  def answer_call(self) -> str:
    pass

  @abstractmethod
  def reject_call(self) -> str:
    pass

  @abstractmethod
  def end_call(self) -> str:
    pass

  @abstractmethod
  def on_hold(self) -> str:
    pass

  def __str__(self) -> str:
    return self.__class__.__name__


class SmartPhoneIdle(SmartPhoneState):
  def __init__(self, context):
    super().__init__(context)

  def in_call(self, phone_number: str) -> str:
    msg = f'Has call from {phone_number}'
    self._ctx.incoming_call_number = phone_number
    self._ctx.state = SmartPhoneRing(self._ctx)
    return msg

  def answer_call(self) -> str:
    return 'No incoming call'

  def reject_call(self) -> str:
    return 'No call'

  def end_call(self) -> str:
    return 'No call'

  def on_hold(self) -> str:
    return 'No call'


class SmartPhoneRing(SmartPhoneState):
  def __init__(self, context):
    super().__init__(context)

  def in_call(self, phone_number: str) -> str:
    return f'Busy with call from {phone_number}'

  def answer_call(self) -> str:
    msg = f'Pickup call from {self._ctx.incoming_call_number}'
    self._ctx.in_call_number = self._ctx.incoming_call_number
    self._ctx.incoming_call_number = None
    self._ctx.state = SmartPhoneInCall(self._ctx)
    return msg

  def reject_call(self) -> str:
    msg = f'Reject call from {self._ctx.incoming_call_number}'
    self._ctx.incoming_call_number = None
    self._ctx.state = SmartPhoneIdle(self._ctx)
    return msg

  def end_call(self) -> str:
    return 'Can not end call in RING'

  def on_hold(self) -> str:
    msg = f'Put call {self._ctx.incoming_call_number} on hold'
    return msg


class SmartPhoneInCall(SmartPhoneState):
  def __init__(self, context):
    super().__init__(context)

  def in_call(self, phone_number: str) -> str:
    self._ctx.incoming_call_number = phone_number
    return f'Alerting user of incoming call from {phone_number}'

  def answer_call(self) -> str:
    if self._ctx.incoming_call_number:
      msg =  f'Switch call to {self._ctx.incoming_call_number}'
      self._ctx.in_call_number, self._ctx.incoming_call_number = self._ctx.incoming_call_number, self._ctx.in_call_number
    else:
      msg =  'No incoming call'
    return msg

  def reject_call(self) -> str:
    return 'Can not reject call in INCALL'

  def end_call(self) -> str:
    msg = f'End call from {self._ctx.in_call_number}'
    self._ctx.in_call_number = None
    if self._ctx.incoming_call_number:
      self._ctx.state = SmartPhoneRing(self._ctx)
    else:
      self._ctx.state = SmartPhoneIdle(self._ctx)

    return msg

  def on_hold(self) -> str:
    msg = f'Put call {self._ctx.in_call_number} on hold and pickup {self._ctx.incoming_call_number}'
    self._ctx.in_call_number, self._ctx.incoming_call_number = self._ctx.incoming_call_number, self._ctx.in_call_number
    return msg


class SmartPhoneOnHold(SmartPhoneState):
  def __init__(self, context):
    super().__init__(context)
    # TBD
