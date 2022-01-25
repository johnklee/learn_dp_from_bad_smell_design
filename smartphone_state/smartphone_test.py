import unittest
import smartphone
from parameterized import parameterized, parameterized_class


TEST_PHONE_NUMBER = '123'

class SmartPhoneTest(unittest.TestCase):
  def setUp(self):
    super().setUp()
    self.phone = smartphone.SmartPhone()

  @parameterized.expand([
    ('idle', smartphone.CallState.IDLE, f'Has call from {TEST_PHONE_NUMBER}', smartphone.CallState.RING),
    ('ring', smartphone.CallState.RING, f'Busy with call from {TEST_PHONE_NUMBER}', smartphone.CallState.RING),
    ('incall', smartphone.CallState.INCALL, f'Alerting user of incoming call from {TEST_PHONE_NUMBER}', smartphone.CallState.INCALL),
  ])
  def test_in_call(self, state_name, state_obj, expected_msg, expected_state):
    self.phone.state = state_obj
    self.assertEqual(
      self.phone.in_call(TEST_PHONE_NUMBER),
      expected_msg)
    self.assertEqual(self.phone.state, expected_state)

  @parameterized.expand([
    ('idle', smartphone.CallState.IDLE, 'No incoming call', smartphone.CallState.IDLE, None),
    ('ring', smartphone.CallState.RING, f'Pickup call from {TEST_PHONE_NUMBER}', smartphone.CallState.INCALL, TEST_PHONE_NUMBER),
    ('incall', smartphone.CallState.INCALL, f'Switch call to {TEST_PHONE_NUMBER}', smartphone.CallState.INCALL, TEST_PHONE_NUMBER),
    ('incall_no_incoming', smartphone.CallState.INCALL, 'No incoming call', smartphone.CallState.INCALL, None),
  ])
  def test_answer_call(self, state_name, state_obj, expected_msg, expected_state, incoming_call_number):
    self.phone.state = state_obj
    self.phone.incoming_call_number = incoming_call_number
    self.assertEqual(
      self.phone.answer_call(),
      expected_msg)
    self.assertEqual(self.phone.state, expected_state)

  @parameterized.expand([
    ('idle', smartphone.CallState.IDLE, 'No call', smartphone.CallState.IDLE, None, None),
    ('ring', smartphone.CallState.RING, f'Can not end call in RING', smartphone.CallState.RING, None, TEST_PHONE_NUMBER),
    ('incall', smartphone.CallState.INCALL, f'End call from {TEST_PHONE_NUMBER}', smartphone.CallState.IDLE, TEST_PHONE_NUMBER, None),
    ('incall_with_incoming', smartphone.CallState.INCALL, f'End call from {TEST_PHONE_NUMBER}', smartphone.CallState.RING, TEST_PHONE_NUMBER, '456'),
  ])
  def test_end_call(self, state_name, state_obj, expected_msg, expected_state, in_call_number, incoming_call_number):
    print(f'test case: {state_name}')
    self.phone.state = state_obj
    self.phone.incoming_call_number = incoming_call_number
    self.phone.in_call_number = in_call_number
    self.assertEqual(
      self.phone.end_call(),
      expected_msg)
    self.assertEqual(self.phone.state, expected_state)

  @parameterized.expand([
    ('idle', smartphone.CallState.IDLE, 'No call', smartphone.CallState.IDLE, None, None),
    ('ring', smartphone.CallState.RING, f'Reject call from {TEST_PHONE_NUMBER}', smartphone.CallState.IDLE, None, TEST_PHONE_NUMBER),
    ('incall', smartphone.CallState.INCALL, 'Can not reject call in INCALL', smartphone.CallState.INCALL, TEST_PHONE_NUMBER, None),
    ('incall_with_incoming', smartphone.CallState.INCALL, 'Can not reject call in INCALL', smartphone.CallState.INCALL, TEST_PHONE_NUMBER, '456'),
  ])
  def test_reject_call(self, state_name, state_obj, expected_msg, expected_state, in_call_number, incoming_call_number):
    print(f'test case: {state_name}')
    self.phone.state = state_obj
    self.phone.incoming_call_number = incoming_call_number
    self.phone.in_call_number = in_call_number
    self.assertEqual(
      self.phone.reject_call(),
      expected_msg)
    self.assertEqual(self.phone.state, expected_state)


if __name__ == '__main__':
    unittest.main()
