

# config is json
config = {}
config["DESIGN_NAME"] = "LerosCaravel_RtlSyncMemory"
config["CLOCK_PORT"] = "clock"
config["CLOCK_NET"] = "clock"
config["CLOCK_PERIOD"] = 25
config["VERILOG_FILES"] = [
  "dir::../../verilog/rtl/CaravelTop.sv"
]

left_edge_space = 10.1
right_edge_space = 10.1
center_space = 390
top_space = 10.1
bottom_space = 40

mem_32x32_width = 300
mem_32x32_height = 500

mem_64x32_width = 470
mem_64x32_height = 600

die_width = left_edge_space + mem_64x32_width + center_space + mem_32x32_width + right_edge_space
die_height = top_space + mem_64x32_height + bottom_space

mem_64x32_x = left_edge_space
mem_64x32_y = bottom_space

mem_32x32_x = left_edge_space + mem_64x32_width + center_space
mem_32x32_y = bottom_space


config["FP_PDN_MULTILAYER"] = True
config["FP_PDN_CORE_RING"] = True

config["FP_SIZING"] = "absolute"
config["DIE_AREA"] = [0, 0, die_width, die_height]

config["VDD_NETS"] = ["vccd1"]
config["GND_NETS"] = ["vssd1"]


config["MACROS"] = {
  "mem_64x32": {
    "instances": {
        "instrMem.m.mem_ext": {
        "location": [mem_64x32_x, mem_64x32_y],
        "orientation": "N"
        }
    },
    "gds": [f"dir::../../gds/mem_64x32.gds"],
    "lef": [f"dir::../../lef/mem_64x32.lef"],
    "nl": [f"dir::../../verilog/gl/mem_64x32.v"],
    "spef": {
        "min_*": [
            "dir::../../spef/multicorner/mem_64x32.min.spef"
        ],
        "nom_*": [
            "dir::../../spef/multicorner/mem_64x32.nom.spef"
        ],
        "max_*": [
            "dir::../../spef/multicorner/mem_64x32.max.spef"
        ]
    },
    "lib": {
        "*": "dir::../../lib/mem_64x32.lib"
    }
  },
  "mem_32x32": {
    "instances": {
        "dmem.m.mem_ext": {
        "location": [mem_32x32_x, mem_32x32_y],
        "orientation": "N"
        }
    },
    "gds": [f"dir::../../gds/mem_32x32.gds"],
    "lef": [f"dir::../../lef/mem_32x32.lef"],
    "nl": [f"dir::../../verilog/gl/mem_32x32.v"],
    "spef": {
        "min_*": [
            "dir::../../spef/multicorner/mem_32x32.min.spef"
        ],
        "nom_*": [
            "dir::../../spef/multicorner/mem_32x32.nom.spef"
        ],
        "max_*": [
            "dir::../../spef/multicorner/mem_32x32.max.spef"
        ]
    },
    "lib": {
        "*": "dir::../../lib/mem_32x32.lib"
    }
  }
}


config["PDN_MACRO_CONNECTIONS"] = [
    "dmem.m.mem_ext vccd1 vssd1 vccd1 vssd1",
    "instrMem.m.mem_ext vccd1 vssd1 vccd1 vssd1"
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
          "CLOCK_PERIOD": 25
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
    #"DEFAULT_CORNER": "max_ss_100C_1v60",
    "RUN_POST_GRT_DESIGN_REPAIR": True,
})

config["DIODE_ON_PORTS"] = "both"

config["STA_CORNERS"] = [
    "nom_tt_025C_1v80",
    "min_tt_025C_1v80",
    "max_tt_025C_1v80"
]

config["GRT_ALLOW_CONGESTION"] = True

# get python file dir
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

# write to file
import json
with open(f"{dir_path}/config.json", "w") as f:
    json.dump(config, f, indent=4)