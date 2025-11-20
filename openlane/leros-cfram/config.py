

# config is json
config = {}
config["DESIGN_NAME"] = "LerosCaravel_ChipFoundrySram"
config["CLOCK_PORT"] = "clock"
config["CLOCK_NET"] = "clock"
config["CLOCK_PERIOD"] = 25
config["VERILOG_FILES"] = [
  "dir::../../verilog/rtl/CaravelTop.sv"
]

left_edge_space = 40
right_edge_space = 40
center_space = 0
top_space = 10.1

cf_wb_sram_width = 380
cf_wb_sram_height = 435

die_width = 2 * cf_wb_sram_width + left_edge_space + right_edge_space + center_space
die_height = cf_wb_sram_height + 300

sram0_x = left_edge_space
sram0_y = die_height - cf_wb_sram_height - top_space

sram1_x = sram0_x + cf_wb_sram_width + center_space
sram1_y = sram0_y


config["FP_PDN_MULTILAYER"] = True
config["FP_PDN_CORE_RING"] = True

config["FP_SIZING"] = "absolute"
config["DIE_AREA"] = [0, 0, die_width, die_height]

config["VDD_NETS"] = ["vccd1"]
config["GND_NETS"] = ["vssd1"]

config["MACROS"] = {
  "CF_SRAM_1024x32_wrapper": {
    "instances": {
        "instrMem.m.mem": {
        "location": [sram0_x, sram0_y],
        "orientation": "N"
        },
        "dmem.m.mem": {
        "location": [sram1_x, sram1_y],
        "orientation": "N"
        }
    },
    "gds": ["dir::../../gds/CF_SRAM_1024x32_wrapper.gds"],
    "lef": ["dir::../../lef/CF_SRAM_1024x32_wrapper.lef"],
    "nl": ["dir::../../verilog/gl/CF_SRAM_1024x32_wrapper.v"],
    "spef": {
        "min_*": [
            "dir::../../spef/multicorner/CF_SRAM_1024x32_wrapper.min.spef"
        ],
        "nom_*": [
            "dir::../../spef/multicorner/CF_SRAM_1024x32_wrapper.nom.spef"
        ],
        "max_*": [
            "dir::../../spef/multicorner/CF_SRAM_1024x32_wrapper.max.spef"
        ]
    },
    "lib": {
        "*": "dir::../../lib/CF_SRAM_1024x32_wrapper.lib"
    }
  }
}


config["PDN_MACRO_CONNECTIONS"] = [
    "dmem.m.mem vccd1 vssd1 VPWR VGND",
    "instrMem.m.mem vccd1 vssd1 VPWR VGND"
]

config["FP_PDN_HPITCH"] = 51
config["FP_PDN_VPITCH"] = 51

config["FP_PIN_ORDER_CFG"] = "dir::pin_order.cfg"
config["FALLBACK_SDC_FILE"] = "dir::base_user_proj_example.sdc"

config["pdk::sky130*"] = {
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
}

config["SYNTH_ABC_BUFFERING"] = False

config["STA_CORNERS"] = [
    "nom_tt_025C_1v80",
    "min_tt_025C_1v80",
    "max_tt_025C_1v80"
]

config.update({
    "DPL_CELL_PADDING": 2,
    "GPL_CELL_PADDING": 2,
})

config.update({
  "MAX_TRANSITION_CONSTRAINT": 1.0,
  "MAX_FANOUT_CONSTRAINT": 16,
  "PL_RESIZER_SETUP_SLACK_MARGIN": 0.4,
  "GRT_RESIZER_SETUP_SLACK_MARGIN": 0.2,
  "GRT_RESIZER_HOLD_SLACK_MARGIN": 0.2,
  "PL_RESIZER_HOLD_SLACK_MARGIN": 0.4,
  "CTS_CLK_MAX_WIRE_LENGTH": 500,
})


config.update({
  "RUN_HEURISTIC_DIODE_INSERTION": True,
  "HEURISTIC_ANTENNA_THRESHOLD": 110,
  "RUN_ANTENNA_REPAIR": True,
  "RUN_POST_GRT_DESIGN_REPAIR": True,
  "RUN_POST_GRT_RESIZER_TIMING": True,
})

# fix antenna issues
config.update({
    "GRT_ANTENNA_ITERS": 20,
    "GRT_ANTENNA_MARGIN": 15,
    #"DESIGN_REPAIR_MAX_WIRE_LENGTH": 800,
    #"PL_WIRE_LENGTH_COEF": 0.05,
})

config.update({
    "MAX_TRANSITION_CONSTRAINT": 1.5,
    "DESIGN_REPAIR_MAX_SLEW_PCT": 30,
    "DESIGN_REPAIR_MAX_CAP_PCT": 30,
    #"DEFAULT_CORNER": "max_ss_100C_1v60",
    "RUN_POST_GRT_DESIGN_REPAIR": True,
})

config.update({ # Klayout seems to be upset by something in the openram metadata (lef?)
    "MAGIC_DEF_LABELS": False,
    "RUN_KLAYOUT_DRC": True,
    "RUN_MAGIC_DRC": True,
    "MAGIC_DRC_USE_GDS": True,
    "QUIT_ON_MAGIC_DRC": False,
    "MAGIC_EXT_USE_GDS": False,
    "MAGIC_CAPTURE_ERRORS": False,
    "QUIT_ON_ILLEGAL_OVERLAPS": False,
})

# get python file dir
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

# write to file
import json
with open(f"{dir_path}/config.json", "w") as f:
    json.dump(config, f, indent=4)