# SPDX-FileCopyrightText: 2023 Efabless Corporation

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#      http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# SPDX-License-Identifier: Apache-2.0


from caravel_cocotb.caravel_interfaces import test_configure
from caravel_cocotb.caravel_interfaces import report_test
import cocotb


async def waitForValue(caravelEnv, gpio_rng, expected_value):
    while True:
        received_val = caravelEnv.monitor_gpio(gpio_rng[0], gpio_rng[1]).binstr
        if received_val == expected_value:
            break

        await cocotb.triggers.ClockCycles(caravelEnv.clk,1)

async def expectTransition(caravelEnv, gpio_rng, from_value, to_value):
    cocotb.log.info(f"Expecting transition on GPIO {gpio_rng[0]}:{gpio_rng[1]} from {from_value} to {to_value}")
    while True:
        received_val = caravelEnv.monitor_gpio(gpio_rng[0], gpio_rng[1]).binstr
        if received_val == to_value:
            break
        elif received_val != from_value:
            cocotb.log.error(f"Unexpected transition on GPIO {gpio_rng[0]}:{gpio_rng[1]} from {from_value} to {to_value}, but got {received_val}")

        await cocotb.triggers.ClockCycles(caravelEnv.clk,1)

async def expectSeq(caravelEnv, gpio_rng, seq, reps):
    await waitForValue(caravelEnv, gpio_rng, seq[0])
    for _ in range(reps):
        for i in range(len(seq)-1):
            await expectTransition(caravelEnv, gpio_rng, seq[i], seq[i+1])
        if reps > 1:
            await expectTransition(caravelEnv, gpio_rng, seq[-1], seq[0])


@cocotb.test()
@report_test
async def wishbone_gpio_test(dut):
    caravelEnv = await test_configure(dut,timeout_cycles=999998)
    
    cocotb.log.info(f"[TEST] Start wishbone_gpio_test test")  
    # wait for start of sending
    await caravelEnv.release_csb()

    

    cocotb.log.info(f"[TEST] waiting for riscv to start counting on gpio") 
    await caravelEnv.wait_mgmt_gpio(1) # wait for setup to be done

    # check wishbone gpio
    await expectSeq(caravelEnv, (37,32), ['000000', '000001', '000010', '000011', '000100', '000101', '000110', '000111',
                                            '001000', '001001', '001010', '001011', '001100', '001101', '001110', '001111',
                                            '010000', '010001', '010010', '010011', '010100', '010101', '010110', '010111',
                                            '011000', '011001', '011010', '011011', '011100', '011101', '011110', '011111'], reps = 1)
    
    caravelEnv.drive_gpio_in((37,32), '101010')  # set inputs to 0x2A
    
    # wait for riscv to lower mnt_gpio to mark test end
    await caravelEnv.wait_mgmt_gpio(0)
    cocotb.log.info(f"[TEST] wishbone_gpio_test passed")
    

