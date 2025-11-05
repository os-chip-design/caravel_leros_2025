from librelane.flows import Flow
from librelane.config import Config
from librelane.state import State


config = {
    "DESIGN_NAME": "CaravelCounterWrapper",
    "FP_PDN_MULTILAYER": True,
    "FP_PDN_CORE_RING": True,
    "VERILOG_FILES": [
        "dir::../../verilog/rtl/defines.v",
        "dir::../../verilog/rtl/CaravelCounter.sv",
        "dir::../../verilog/rtl/CaravelCounterWrapper.v"
    ],
    "CLOCK_PERIOD": 25,
    "CLOCK_PORT": "wb_clk_i",
    "CLOCK_NET": "counter.clock",
    "FP_SIZING": "absolute",
    "DIE_AREA": [
        0,
        0,
        1000,
        500
    ],
    "FP_PIN_ORDER_CFG": "dir::pin_order.cfg",
    "VDD_NETS": [
        "vccd1"
    ],
    "GND_NETS": [
        "vssd1"
    ],
    "FALLBACK_SDC_FILE": "dir::base_user_proj_example.sdc",
    "STD_CELL_LIBRARY": "sky130_fd_sc_hd",
}

Classic = Flow.factory.get("Classic")
classic_flow = Classic(Config.load(
  config, 
  Classic.config_vars,
  design_dir="dir::.",
  pdk="sky130A"
))

classic_flow.run(State())