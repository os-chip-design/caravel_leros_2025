

# config is json
config = {}
config["DESIGN_NAME"] = "LerosCaravel_DffRam"
config["CLOCK_PORT"] = "clock"
config["CLOCK_NET"] = "clock"
config["CLOCK_PERIOD"] = 100
config["VERILOG_FILES"] = [
  "dir::../../verilog/rtl/LerosCaravel_DffRam.sv"
]

left_edge_space = 300
right_edge_space = 10.1
center_space = 200
top_space = 100
bottom_space = 100

dffram_width = 809.6
dffram_height = 533.12

die_width = left_edge_space + dffram_width + right_edge_space
die_height = top_space + 2 * dffram_height + center_space + bottom_space

sram0_x = left_edge_space
sram0_y = bottom_space

sram1_x = left_edge_space
sram1_y = bottom_space + dffram_height + center_space


config["FP_PDN_MULTILAYER"] = True
config["FP_PDN_CORE_RING"] = True

config["FP_SIZING"] = "absolute"
config["DIE_AREA"] = [0, 0, die_width, die_height]

config["VDD_NETS"] = ["vccd1"]
config["GND_NETS"] = ["vssd1"]

config["MACROS"] = {
  "RAM256": {
    "instances": {
        "instrMem.m.mem": {
        "location": [sram0_x, sram0_y],
        "orientation": "FN"
        },
        "dmem.m.mem": {
        "location": [sram1_x, sram1_y],
        "orientation": "FN"
        }
    },
    "gds": ["dir::../../dffram/gds/RAM256.gds"],
    "lef": ["dir::../../dffram/lef/RAM256.lef"],
    "nl": ["dir::../../dffram/nl/RAM256.nl.v"],
    "spef": {
        "min_*": ["dir::../../dffram/spef/min/RAM256.min.spef"],
        "nom_*": ["dir::../../dffram/spef/nom/RAM256.nom.spef"],
        "max_*": ["dir::../../dffram/spef/max/RAM256.max.spef"]
    },
    "lib": {
        "min_tt_025C_1v80": "dir::../../dffram/lib/min_tt_025C_1v80/RAM256__min_tt_025C_1v80.lib",
        "min_ff_n40C_1v95": "dir::../../dffram/lib/min_ff_n40C_1v95/RAM256__min_ff_n40C_1v95.lib",
        "max_ff_n40C_1v95": "dir::../../dffram/lib/max_ff_n40C_1v95/RAM256__max_ff_n40C_1v95.lib",
        "nom_tt_025C_1v80": "dir::../../dffram/lib/nom_tt_025C_1v80/RAM256__nom_tt_025C_1v80.lib",
        "min_ss_100C_1v60": "dir::../../dffram/lib/min_ss_100C_1v60/RAM256__min_ss_100C_1v60.lib",
        "max_ss_100C_1v60": "dir::../../dffram/lib/max_ss_100C_1v60/RAM256__max_ss_100C_1v60.lib",
        "max_tt_025C_1v80": "dir::../../dffram/lib/max_tt_025C_1v80/RAM256__max_tt_025C_1v80.lib",
        "nom_ss_100C_1v60": "dir::../../dffram/lib/nom_ss_100C_1v60/RAM256__nom_ss_100C_1v60.lib",
        "nom_ff_n40C_1v95": "dir::../../dffram/lib/nom_ff_n40C_1v95/RAM256__nom_ff_n40C_1v95.lib"
    }
  }
}


config["PDN_MACRO_CONNECTIONS"] = [
    "dmem.m.mem vccd1 vssd1 vccd1 vssd1",
    "instrMem.m.mem vccd1 vssd1 vccd1 vssd1"
]

config["FP_PDN_HPITCH"] = 51
config["FP_PDN_VPITCH"] = 51

config.update({
  "FP_PIN_ORDER_CFG": "dir::pin_order.cfg",
  "MAX_TRANSITION_CONSTRAINT": 1.0,
  "MAX_FANOUT_CONSTRAINT": 16,
  "PL_RESIZER_SETUP_SLACK_MARGIN": 0.4,
  "GRT_RESIZER_SETUP_SLACK_MARGIN": 0.2,
  "GRT_RESIZER_HOLD_SLACK_MARGIN": 0.2,
  "PL_RESIZER_HOLD_SLACK_MARGIN": 0.4,
  "CTS_CLK_MAX_WIRE_LENGTH": 500,
  "MAGIC_DEF_LABELS": False,
  "SYNTH_ABC_BUFFERING": False,
  "RUN_HEURISTIC_DIODE_INSERTION": True,
  "HEURISTIC_ANTENNA_THRESHOLD": 110,
  "RUN_ANTENNA_REPAIR": True,
  "RUN_POST_GRT_DESIGN_REPAIR": True,
  "RUN_POST_GRT_RESIZER_TIMING": True,
  "FALLBACK_SDC_FILE": "dir::base_user_proj_example.sdc",
  "MAGIC_DRC_USE_GDS": True,
  "DPL_CELL_PADDING": 2,
  "GPL_CELL_PADDING": 2,
  "QUIT_ON_MAGIC_DRC": False,
  "MAGIC_EXT_USE_GDS": False,
  "MAGIC_CAPTURE_ERRORS": False,
  "QUIT_ON_ILLEGAL_OVERLAPS": False,
  "pdk::sky130*": {
      "RT_MAX_LAYER": "met4",
      "scl::sky130_fd_sc_hd": {
          "CLOCK_PERIOD": 100
      },
      "scl::sky130_fd_sc_hdll": {
          "CLOCK_PERIOD": 10
      },
      "scl::sky130_fd_sc_hs": {
          "CLOCK_PERIOD": 8
      },
      "scl::sky130_fd_sc_ls": {
          "CLOCK_PERIOD": 10,
          "SYNTH_MAX_FANOUT": 5
      },
      "scl::sky130_fd_sc_ms": {
          "CLOCK_PERIOD": 10
      }
  },
  "pdk::gf180mcuC": {
      "STD_CELL_LIBRARY": "gf180mcu_fd_sc_mcu7t5v0",
      "CLOCK_PERIOD": 24.0,
      "RT_MAX_LAYER": "Metal4",
      "SYNTH_MAX_FANOUT": 4,
      "PL_TARGET_DENSITY_PCT": 45
  },
  "meta": {
      "version": 2
  }
})

#fix antenna issues
config.update({
    "GRT_ANTENNA_ITERS": 20,
    "GRT_ANTENNA_MARGIN": 20,
    "RUN_HEURISTIC_DIODE_INSERTION": True,
    "DESIGN_REPAIR_MAX_WIRE_LENGTH": 800,
    "PL_WIRE_LENGTH_COEF": 0.05,
})

config.update({
    "MAX_TRANSITION_CONSTRAINT": 1.5,
    "DESIGN_REPAIR_MAX_SLEW_PCT": 30,
    "DESIGN_REPAIR_MAX_CAP_PCT": 30,
    "DEFAULT_CORNER": "max_ss_100C_1v60",
    "RUN_POST_GRT_DESIGN_REPAIR": True,
})

# write to file
import json
with open("config.json", "w") as f:
    json.dump(config, f, indent=4)