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
 * user_project_wrapper
 *
 * This wrapper enumerates all of the pins available to the
 * user for the user project.
 *
 * An example user project is provided in this wrapper.  The
 * example should be removed and replaced with the actual
 * user project.
 *
 *-------------------------------------------------------------
 */

module user_project_wrapper #(
    parameter BITS = 32
) (
`ifdef USE_POWER_PINS
    inout vdda1,	// User area 1 3.3V supply
    inout vdda2,	// User area 2 3.3V supply
    inout vssa1,	// User area 1 analog ground
    inout vssa2,	// User area 2 analog ground
    inout vccd1,	// User area 1 1.8V supply
    inout vccd2,	// User area 2 1.8v supply
    inout vssd1,	// User area 1 digital ground
    inout vssd2,	// User area 2 digital ground
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
    input  [`MPRJ_IO_PADS-1:0] io_in,
    output [`MPRJ_IO_PADS-1:0] io_out,
    output [`MPRJ_IO_PADS-1:0] io_oeb,

    // Analog (direct connection to GPIO pad---use with caution)
    // Note that analog I/O is not available on the 7 lowest-numbered
    // GPIO pads, and so the analog_io indexing is offset from the
    // GPIO indexing by 7 (also upper 2 GPIOs do not have analog_io).
    inout [`MPRJ_IO_PADS-10:0] analog_io,

    // Independent clock (on independent integer divider)
    input   user_clock2,

    // User maskable interrupt signals
    output [2:0] user_irq
);

/*--------------------------------------*/
/* User project is instantiated  here   */
/*--------------------------------------*/
wire [5:0] leros_cfram_gpio_in;
wire [5:0] leros_cfram_gpio_out;
wire [5:0] leros_cfram_gpio_oe;

wire [5:0] leros_openram_gpio_in;
wire [5:0] leros_openram_gpio_out;
wire [5:0] leros_openram_gpio_oe;

wire [5:0] leros_dffram_gpio_in;
wire [5:0] leros_dffram_gpio_out;
wire [5:0] leros_dffram_gpio_oe;

wire [5:0] leros_regmem_gpio_in;
wire [5:0] leros_regmem_gpio_out;
wire [5:0] leros_regmem_gpio_oe;

wire [5:0] wb_gpio_in;
wire [5:0] wb_gpio_out;
wire [5:0] wb_gpio_oe;

assign leros_cfram_gpio_in   = io_in[24:19];
assign io_out[24:19]         = leros_cfram_gpio_out;
assign io_oeb[24:19]         = leros_cfram_gpio_oe;

assign leros_openram_gpio_in = io_in[30:25];
assign io_out[30:25]         = leros_openram_gpio_out;
assign io_oeb[30:25]         = leros_openram_gpio_oe;

assign leros_dffram_gpio_in  = io_in[12:7];
assign io_out[12:7]          = leros_dffram_gpio_out;
assign io_oeb[12:7]          = leros_dffram_gpio_oe;

assign leros_regmem_gpio_in  = io_in[18:13];
assign io_out[18:13]         = leros_regmem_gpio_out;
assign io_oeb[18:13]         = leros_regmem_gpio_oe;

assign wb_gpio_in            = io_in[36:31];
assign io_out[36:31]         = wb_gpio_out;
assign io_oeb[36:31]         = wb_gpio_oe;

CaravelTop mprj (

// `ifdef USE_POWER_PINS
// 	.vccd1(vccd1),	// User area 1 1.8V power
// 	.vssd1(vssd1),	// User area 1 digital ground
// `endif


    .clock(wb_clk_i),
    .reset(wb_rst_i),

    // MGMT SoC Wishbone Slave

    .io_wb_cyc(wbs_cyc_i),
    .io_wb_stb(wbs_stb_i),
    .io_wb_we(wbs_we_i),
    .io_wb_sel(wbs_sel_i),
    .io_wb_adr(wbs_adr_i[19:0]),
    .io_wb_dat_i(wbs_dat_i),
    .io_wb_ack(wbs_ack_o),
    .io_wb_dat_o(wbs_dat_o),

    // Logic Analyzer

    // IO Pads

    .io_gpio_in({wb_gpio_in,
                 leros_regmem_gpio_in,
                 leros_dffram_gpio_in,
                 leros_openram_gpio_in,
                 leros_cfram_gpio_in}),
    .io_gpio_out({wb_gpio_out,
                  leros_regmem_gpio_out,
                  leros_dffram_gpio_out,
                  leros_openram_gpio_out,
                  leros_cfram_gpio_out}),
    .io_gpio_oe({wb_gpio_oe,
                 leros_regmem_gpio_oe,
                 leros_dffram_gpio_oe,
                 leros_openram_gpio_oe,
                 leros_cfram_gpio_oe})
);

endmodule	// user_project_wrapper

`default_nettype wire
