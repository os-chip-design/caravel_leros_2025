// SPDX-FileCopyrightText: 2023 Efabless Corporation

// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at

//      http://www.apache.org/licenses/LICENSE-2.0

// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.


#include <firmware_apis.h>

void set_sys_ctrl(unsigned int data) {
    USER_writeWord(data, 0xC00 >> 2);
}

int get_sys_ctrl() {
    return USER_readWord(0xC00 >> 2);
}

void leros_set_reset() {
    set_sys_ctrl(get_sys_ctrl() | 0x1);
}

void leros_clear_reset() {
    set_sys_ctrl(get_sys_ctrl() & ~0x1);
}

void leros_boot_from_ram() {
    set_sys_ctrl(get_sys_ctrl() | 0x2);
}

void leros_boot_from_rom() {
    set_sys_ctrl(get_sys_ctrl() & ~0x2);
}

void leros_uart_loopback_enable() {
    set_sys_ctrl(get_sys_ctrl() | 0x4);
}

void leros_uart_loopback_disable() {
    set_sys_ctrl(get_sys_ctrl() & ~0x4);
}

void write_reg(unsigned int i, int data) {
    USER_writeWord(data, (0x800 >> 2) + i);
}

int read_reg(unsigned int i) {
    return USER_readWord((0x800 >> 2) + i);
}

void write_prog(unsigned int *prog, unsigned int size) {
    for (unsigned int i = 0; i < size; i++) {
        USER_writeWord(prog[i], 0x000 + i);
    }
}

unsigned int adder_test[] = {
  0x29802100, // 0x0000
  0x30012a00, // 0x0004
  0x21015001, // 0x0008
  0x60007000, // 0x000c
  0x21009fff, // 0x0010
  0x60017000, // 0x0014
  0x60023002, // 0x0018
  0x70030802, // 0x001c
  0x8ff5, // 0x0020
};

bool adder_test_ready() {
    return (read_reg(0) == 1);
}

void set_valid(bool b) {
    write_reg(0, b ? 1 : 0);
}

void load_values(int a, int b) {
    write_reg(1, a);
    write_reg(2, b);
}

int get_result() {
    return read_reg(3);
}

int add(int a, int b) {
    load_values(a, b);
    set_valid(true);
    while (!adder_test_ready()) {} // wait for leros to be ready
    set_valid(false); // clear valid
    while (!adder_test_ready()) {} // wait for leros to be ready again
    return get_result();
}

void main(){
    // Enable managment gpio as output to use as indicator for finishing configuration  
    ManagmentGpio_outputEnable();
    ManagmentGpio_write(0);
    enableHkSpi(0); // disable housekeeping spi
    // configure all gpios as  user out then chenge gpios from 32 to 37 before loading this configurations
    GPIOs_configureAll(GPIO_MODE_USER_STD_OUT_MONITORED);
    
    GPIOs_loadConfigs(); // load the configuration 
    User_enableIF(); // this necessary when reading or writing between wishbone and user project if interface isn't enabled no ack would be recieve and the command will be stuck

    leros_set_reset();
    leros_boot_from_ram();
    leros_uart_loopback_enable();
    write_prog(adder_test, sizeof(adder_test) / sizeof(unsigned int));
    leros_clear_reset();

    bool pass = true;
    pass &= add(1, 2) == 3;
    pass &= add(10, 20) == 30;
    pass &= add(100, 200) == 300;
    pass &= add(0xFFFFFFFF, 1) == 0;

    if (pass) { // signal pass to cocotb
        ManagmentGpio_write(1); 
    } // let the test timeout when fail

    return;
}