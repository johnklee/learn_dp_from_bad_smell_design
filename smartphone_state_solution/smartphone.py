from abc import ABC, abstractmethod
import enum
import smartphone_states


class SmartPhoneContext:
  def __init__(self):
    self.state = smartphone_states.SmartPhoneIdle(self)
    self.incoming_call_number = None
    self.in_call_number = None

  def in_call(self, phone_number: str) -> str:
    return self.state.in_call(phone_number)

  def answer_call(self) -> str:
    return self.state.answer_call()

  def reject_call(self) -> str:
    return self.state.reject_call()

  def end_call(self) -> str:
    return self.state.end_call()

  def on_hold(self) -> str:
    return self.state.on_hold()
