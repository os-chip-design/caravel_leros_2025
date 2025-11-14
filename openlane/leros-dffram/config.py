

# config is json
config = {}
config["DESIGN_NAME"] = "LerosCaravel_DffRam"
config["CLOCK_PORT"] = "clock"
config["CLOCK_NET"] = "clock"
config["CLOCK_PERIOD"] = 100
config["VERILOG_FILES"] = [
  "dir::../../verilog/rtl/LerosCaravel_DffRam.sv"
]

left_edge_space = 500
right_edge_space = 50
center_space = 0
top_space = 200
bottom_space = 200

dffram_width = 1152.795
dffram_height = 535.550

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

dffram_dir = "dir::../../ip/DFFRAM256x32"

config["MACROS"] = {
  "DFFRAM256x32": {
    "instances": {
        "instrMem.m.mem": {
        "location": [sram0_x, sram0_y],
        "orientation": "FN"
        },
        "dmem.m.mem": {
        "location": [sram1_x, sram1_y],
        "orientation": "S"
        }
    },
    "gds": [f"{dffram_dir}/layout/gds/DFFRAM256x32.gds"],
    "lef": [f"{dffram_dir}/layout/lef/DFFRAM256x32.lef"],
    "nl": [f"{dffram_dir}/hdl/gl/DFFRAM256x32.v"],
    "spef": {
        "min_*": [f"{dffram_dir}/timing/spef/DFFRAM256x32.min.spef"],
        "nom_*": [f"{dffram_dir}/timing/spef/DFFRAM256x32.nom.spef"],
        "max_*": [f"{dffram_dir}/timing/spef/DFFRAM256x32.max.spef"]
    },
    "lib": {
        "max_ff_*": f"{dffram_dir}/timing/lib/max/DFFRAM256x32.Fastest.lib",
        "max_ss_*": f"{dffram_dir}/timing/lib/max/DFFRAM256x32.Slowest.lib",
        "max_tt_*": f"{dffram_dir}/timing/lib/max/DFFRAM256x32.Typical.lib",
        "min_ff_*": f"{dffram_dir}/timing/lib/min/DFFRAM256x32.Fastest.lib",
        "min_ss_*": f"{dffram_dir}/timing/lib/min/DFFRAM256x32.Slowest.lib",
        "min_tt_*": f"{dffram_dir}/timing/lib/min/DFFRAM256x32.Typical.lib",
        "nom_ff_*": f"{dffram_dir}/timing/lib/nom/DFFRAM256x32.Fastest.lib",
        "nom_ss_*": f"{dffram_dir}/timing/lib/nom/DFFRAM256x32.Slowest.lib",
        "nom_tt_*": f"{dffram_dir}/timing/lib/nom/DFFRAM256x32.Typical.lib"
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
          "CLOCK_PERIOD": config["CLOCK_PERIOD"]
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