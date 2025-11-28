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

void set_sys_ctrl(unsigned int lerosId, unsigned int data) {
    USER_writeWord(data, (0x2000 >> 2) + ((lerosId * 0x10000) >> 2));
}

int get_sys_ctrl(unsigned int lerosId) {
    return USER_readWord((0x2000 >> 2) + ((lerosId * 0x10000) >> 2));
}

void leros_set_reset(unsigned int lerosId) {
    set_sys_ctrl(lerosId, get_sys_ctrl(lerosId) | 0x1);
}

void leros_clear_reset(unsigned int lerosId) {
    set_sys_ctrl(lerosId, get_sys_ctrl(lerosId) & ~0x1);
}

void leros_boot_from_ram(unsigned int lerosId) {
    set_sys_ctrl(lerosId, get_sys_ctrl(lerosId) | 0x2);
}

void leros_boot_from_rom(unsigned int lerosId) {
    set_sys_ctrl(lerosId, get_sys_ctrl(lerosId) & ~0x2);
}

void leros_uart_loopback_enable(unsigned int lerosId) {
    set_sys_ctrl(lerosId, get_sys_ctrl(lerosId) | 0x4);
}

void leros_uart_loopback_disable(unsigned int lerosId) {
    set_sys_ctrl(lerosId, get_sys_ctrl(lerosId) & ~0x4);
}

void write_reg(unsigned int lerosId, unsigned int i, int data) {
    USER_writeWord(data, (0x1000 >> 2) + i + (lerosId * 0x10000 >> 2));
}

int read_reg(unsigned int lerosId, unsigned int i) {
    return USER_readWord((0x1000 >> 2) + i + (lerosId * 0x10000 >> 2));
}

void write_prog(unsigned int lerosId, unsigned int *prog, unsigned int size) {
    for (unsigned int i = 0; i < size; i++) {
        USER_writeWord(prog[i], 0x000 + i + (lerosId * 0x10000 >> 2));
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

unsigned int blink[] = {
  0x21000000, // 0x0000
  0x2a002980, // 0x0004
  0x50013001, // 0x0008
  0x30022100, // 0x000c
  0x09012002, // 0x0010
  0x70003002, // 0x0014
  0x23017041, // 0x0018
  0x70450930, // 0x001c
  0x8ff8, // 0x0020
};

#define numberOfLeros 4

void main(){
    // Enable managment gpio as output to use as indicator for finishing configuration  
    ManagmentGpio_outputEnable();
    ManagmentGpio_write(0);
    enableHkSpi(0); // disable housekeeping spi
    // configure all gpios as  user out then chenge gpios from 32 to 37 before loading this configurations
    GPIOs_configureAll(GPIO_MODE_USER_STD_OUT_MONITORED);
    
    GPIOs_loadConfigs(); // load the configuration 
    User_enableIF(); // this necessary when reading or writing between wishbone and user project if interface isn't enabled no ack would be recieve and the command will be stuck

    for (unsigned int i = 0; i < numberOfLeros; i++) {
        leros_set_reset(i);
    }

    for (unsigned int i = 0; i < numberOfLeros; i++) {
        leros_boot_from_ram(i);
        leros_uart_loopback_enable(i);
        write_prog(i, blink, sizeof(blink) / sizeof(unsigned int));
        leros_clear_reset(i);
    }
    
    ManagmentGpio_write(1); // mark setup is done


    return;
}