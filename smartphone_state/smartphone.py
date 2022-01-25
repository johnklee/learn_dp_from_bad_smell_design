import enum


class CallState(enum.Enum):
  IDLE = 1
  INCALL = 2
  RING = 3


class SmartPhone:
  def __init__(self, init_state: CallState=CallState.IDLE):
    self.state = init_state
    self.incoming_call_number = None
    self.in_call_number = None

  def in_call(self, phone_number: str) -> str:
    if self.state == CallState.IDLE:
      msg = f'Has call from {phone_number}'
      self.incoming_call_number = phone_number
      self.state = CallState.RING
      return msg
    elif self.state == CallState.RING:
      return f'Busy with call from {phone_number}'
    elif self.state == CallState.INCALL:
      self.incoming_call_number = phone_number
      return f'Alerting user of incoming call from {phone_number}'
    else:
      return 'Unknown state'

  def answer_call(self) -> str:
    if self.state == CallState.IDLE:
      return f'No incoming call'
    elif self.state == CallState.RING:
      msg = f'Pickup call from {self.incoming_call_number}'
      self.in_call_number = self.incoming_call_number
      self.incoming_call_number = None
      self.state = CallState.INCALL
      return msg
    elif self.state == CallState.INCALL:
      if self.incoming_call_number:
        msg =  f'Switch call to {self.incoming_call_number}'
        self.in_call_number, self.incoming_call_number = self.incoming_call_number, self.in_call_number
      else:
        msg =  'No incoming call'
      return msg
    else:
      return 'Unknown state'

  def reject_call(self) -> str:
    if self.state == CallState.IDLE:
      return 'No call'
    elif self.state == CallState.RING:
      msg = f'Reject call from {self.incoming_call_number}'
      self.state = CallState.IDLE
      return msg
    elif self.state == CallState.INCALL:
      return f'Can not reject call in INCALL'
    else:
      return 'Unknown state'

  def end_call(self) -> str:
    if self.state == CallState.IDLE:
      return 'No call'
    elif self.state == CallState.RING:
      return 'Can not end call in RING'
    elif self.state == CallState.INCALL:
      msg = f'End call from {self.in_call_number}'
      self.in_call_number = None
      if self.incoming_call_number:
        self.state = CallState.RING
      else:
        self.state = CallState.IDLE
      return msg
    else:
      return 'Unknown state'
