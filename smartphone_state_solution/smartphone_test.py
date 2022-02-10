import enum
import unittest
import smartphone
import smartphone_states
from parameterized import parameterized, parameterized_class


TEST_PHONE_NUMBER = '123'


class CallState(enum.Enum):
  IDLE = 1
  INCALL = 2
  RING = 3
  ONHOLD = 4


class SmartPhoneTest(unittest.TestCase):
  def setUp(self):
    super().setUp()
    self.phone_ctx = smartphone.SmartPhoneContext()

  def switch_state(self, state: CallState):
    if state == CallState.IDLE:
      self.phone_ctx.state = smartphone_states.SmartPhoneIdle(self.phone_ctx)
    elif state == CallState.INCALL:
      self.phone_ctx.state = smartphone_states.SmartPhoneInCall(self.phone_ctx)
    elif state == CallState.RING:
      self.phone_ctx.state = smartphone_states.SmartPhoneRing(self.phone_ctx)
    elif state == CallState.ONHOLD:
      self.phone_ctx.state = smartphone_states.SmartPhoneOnHold(self.phone_ctx)
    else:
      raise Exception('Unknown state!')

  def assertState(self, expected_state):
    if expected_state == CallState.IDLE:
      self.assertTrue(isinstance(self.phone_ctx.state, smartphone_states.SmartPhoneIdle))
    elif expected_state == CallState.INCALL:
      self.assertTrue(isinstance(self.phone_ctx.state, smartphone_states.SmartPhoneInCall))
    elif expected_state == CallState.RING:
      self.assertTrue(isinstance(self.phone_ctx.state, smartphone_states.SmartPhoneRing))
    elif expected_state == CallState.ONHOLD:
      self.assertTrue(isinstance(self.phone_ctx.state, smartphone_states.SmartPhoneOnHold))
    else:
      raise Exception('Unknown state!')

  @parameterized.expand([
    ('idle', CallState.IDLE, f'Has call from {TEST_PHONE_NUMBER}', CallState.RING),
    ('ring', CallState.RING, f'Busy with call from {TEST_PHONE_NUMBER}', CallState.RING),
    ('incall', CallState.INCALL, f'Alerting user of incoming call from {TEST_PHONE_NUMBER}', CallState.INCALL),
  ])
  def test_in_call(self, state_name, init_state, expected_msg, expected_state):
    self.switch_state(init_state)
    self.assertEqual(
      self.phone_ctx.in_call(TEST_PHONE_NUMBER),
      expected_msg)
    self.assertState(expected_state)

  @parameterized.expand([
    ('idle', CallState.IDLE, 'No incoming call', CallState.IDLE, None),
    ('ring', CallState.RING, f'Pickup call from {TEST_PHONE_NUMBER}', CallState.INCALL, TEST_PHONE_NUMBER),
    ('incall', CallState.INCALL, f'Switch call to {TEST_PHONE_NUMBER}', CallState.INCALL, TEST_PHONE_NUMBER),
    ('incall_no_incoming', CallState.INCALL, 'No incoming call', CallState.INCALL, None),
  ])
  def test_answer_call(self, state_name, init_state, expected_msg, expected_state, incoming_call_number):
    self.switch_state(init_state)
    self.phone_ctx.incoming_call_number = incoming_call_number
    self.assertEqual(
      self.phone_ctx.answer_call(),
      expected_msg)
    self.assertState(expected_state)

  @parameterized.expand([
    ('idle', CallState.IDLE, 'No call', CallState.IDLE, None, None),
    ('ring', CallState.RING, f'Can not end call in RING', CallState.RING, None, TEST_PHONE_NUMBER),
    ('incall', CallState.INCALL, f'End call from {TEST_PHONE_NUMBER}', CallState.IDLE, TEST_PHONE_NUMBER, None),
    ('incall_with_incoming', CallState.INCALL, f'End call from {TEST_PHONE_NUMBER}', CallState.RING, TEST_PHONE_NUMBER, '456'),
  ])
  def test_end_call(self, state_name, init_state, expected_msg, expected_state, in_call_number, incoming_call_number):
    self.switch_state(init_state)
    self.phone_ctx.incoming_call_number = incoming_call_number
    self.phone_ctx.in_call_number = in_call_number
    self.assertEqual(
      self.phone_ctx.end_call(),
      expected_msg)
    self.assertState(expected_state)

  @parameterized.expand([
    ('idle', CallState.IDLE, 'No call', CallState.IDLE, None, None),
    ('ring', CallState.RING, f'Reject call from {TEST_PHONE_NUMBER}', CallState.IDLE, None, TEST_PHONE_NUMBER),
    ('incall', CallState.INCALL, 'Can not reject call in INCALL', CallState.INCALL, TEST_PHONE_NUMBER, None),
    ('incall_with_incoming', CallState.INCALL, 'Can not reject call in INCALL', CallState.INCALL, TEST_PHONE_NUMBER, '456'),
  ])
  def test_reject_call(self, state_name, init_state, expected_msg, expected_state, in_call_number, incoming_call_number):
    self.switch_state(init_state)
    self.phone_ctx.incoming_call_number = incoming_call_number
    self.phone_ctx.in_call_number = in_call_number
    self.assertEqual(
      self.phone_ctx.reject_call(),
      expected_msg)
    self.assertState(expected_state)

  @parameterized.expand([
    ('idle', CallState.IDLE, 'No call', CallState.IDLE, None, None),
    ('ring', CallState.RING, f'Put call {TEST_PHONE_NUMBER} on hold', CallState.ONHOLD, None, TEST_PHONE_NUMBER),
    ('incall', CallState.INCALL, f'Put call {TEST_PHONE_NUMBER} on hold', CallState.ONHOLD, TEST_PHONE_NUMBER, None),
    ('incall_with_incoming', CallState.INCALL, f'Put call {TEST_PHONE_NUMBER} on hold and pickup 456', CallState.INCALL, TEST_PHONE_NUMBER, '456'),
  ])
  def test_onhold(self, state_name, init_state, expected_msg, expected_state, in_call_number, incoming_call_number):
    self.switch_state(init_state)
    self.phone_ctx.incoming_call_number = incoming_call_number
    self.phone_ctx.in_call_number = in_call_number
    self.assertEqual(
      self.phone_ctx.on_hold(),
      expected_msg)
    self.assertState(expected_state)


if __name__ == '__main__':
    unittest.main()
