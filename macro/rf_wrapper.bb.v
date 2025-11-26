// Behavioural model of tnt's register file, for testing.

`default_nettype none

module rf_wrapper (
  
    input  wire [31:0] w_data,
    input  wire  [4:0] w_addr,
    input  wire        w_ena,
    input  wire  [4:0] ra_addr,
    input  wire  [4:0] rb_addr,
    output reg  [31:0] ra_data,
    output reg  [31:0] rb_data,
    input  wire        clk 
);


endmodule /* rf_wrapper */
