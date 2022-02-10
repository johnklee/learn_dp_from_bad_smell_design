#!/usr/bin/env python
import logging
import smartphone


logging.basicConfig(level=logging.INFO)
log = logging.getLogger('demo')
sp_context = smartphone.SmartPhoneContext()
test_phone_number = '123'
log.info(f'Initial state: {sp_context.state}')

# CUJ1: Make phone call
output = sp_context.in_call(test_phone_number)
log.info(f'Make phone call with state={sp_context.state}: {output}')
output = sp_context.answer_call()
log.info(f'Answer call with state={sp_context.state}: {output}')
output = sp_context.end_call()
log.info(f'End call with state={sp_context.state}: {output}')
