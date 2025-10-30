// SPDX-FileCopyrightText: 2020 Efabless Corporation
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
// SPDX-License-Identifier: Apache-2.0

`default_nettype none
/*
 *-------------------------------------------------------------
 *
 * user_proj_example
 *
 * This is an example of a (trivially simple) user project,
 * showing how the user project can connect to the logic
 * analyzer, the wishbone bus, and the I/O pads.
 *
 * This project generates an integer count, which is output
 * on the user area GPIO pads (digital output only).  The
 * wishbone connection allows the project to be controlled
 * (start and stop) from the management SoC program.
 *
 * See the testbenches in directory "mprj_counter" for the
 * example programs that drive this user project.  The three
 * testbenches are "io_ports", "la_test1", and "la_test2".
 *
 *-------------------------------------------------------------
 */

module LerosCaravelWrapper_OpenRam #(
    parameter BITS = 16
)(
`ifdef USE_POWER_PINS
    inout vccd1,	// User area 1 1.8V supply
    inout vssd1,	// User area 1 digital ground
`endif

    // Wishbone Slave ports (WB MI A)
    input wb_clk_i,
    input wb_rst_i,
    input wbs_stb_i,
    input wbs_cyc_i,
    input wbs_we_i,
    input [3:0] wbs_sel_i,
    input [31:0] wbs_dat_i,
    input [31:0] wbs_adr_i,
    output wbs_ack_o,
    output [31:0] wbs_dat_o,

    // Logic Analyzer Signals
    input  [127:0] la_data_in,
    output [127:0] la_data_out,
    input  [127:0] la_oenb,

    // IOs
    input  [7:0] io_in,
    output [7:0] io_out,
    output [7:0] io_oeb,

    // IRQ
    output [2:0] user_irq
);
    
    LerosCaravel_OpenRamSky130 leros_system(
        .clock(wb_clk_i),
        .reset(wb_rst_i),
        .io_wb_stb(wbs_stb_i),
        .io_wb_cyc(wbs_cyc_i),
        .io_wb_we(wbs_we_i),
        .io_wb_sel(wbs_sel_i),
        .io_wb_dat_i(wbs_dat_i),
        .io_wb_adr(wbs_adr_i),
        .io_wb_dat_o(wbs_dat_o),
        .io_wb_ack(wbs_ack_o),

        .io_la_in(la_data_in),
        .io_la_out(la_data_out),
        .io_la_outputEnable(la_oenb),

        .io_gpio_in(io_in),
        .io_gpio_out(io_out),
        .io_gpio_outputEnable(io_oeb),

        .io_user_irq(user_irq)
    );

endmodule
