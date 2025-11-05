# Caravel Leros Project

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) [![UPRJ_CI](https://github.com/chipfoundry/caravel_user_project/actions/workflows/user_project_ci.yml/badge.svg)](https://github.com/chipfoundry/caravel_user_project/actions/workflows/user_project_ci.yml)

This is a user project for the Caravel harness, integrating the open-source Leros CPU core.
This repository contains the DTU subsystem from the [Edu4Chip](https://edu4chip.github.io/) tapeout project.

Checkout with submodules:

    git clone --recurse-submodules git@github.com:os-chip-design/caravel_leros_2025.git

Or later:

    git submodule update --init --recursive

Then build the project start Docker and follow [the Docs](docs/source/index.md), or as follows:

    make setup

For a Mac install the CF RAM (it is included in the Makefile on Linux):

    pip3 install --break-system-packages cf-ipm
    ipm install CF_SRAM_1024x32

Generate the Leros Verilog files

    make generate-verilog

then harden the wrapper for the memory

    make CF_SRAM_1024x32_wrapper

then build and harden Leros with the CF RAM:

    make leros-cfram LIBRELANE_USE_NIX=1

and the wrapper for Caravel:

    make user_project_wrapper LIBRELANE_USE_NIX=1

Then install the CF tools and the design should be ready for **tapeout** (submit to CF) ;-)

    cf init
    cf push

Or do a precheck first:

    make precheck
    DISABLE_LVS=1 make run-precheck

## TODO

* [x] Setup Caravel on Mac (MS, TP)
* [x] Setup Caravel on chipdesign1
* [x] Harden the example project
* [x] Run the provided tests
* [x] MPW check
* [x] Test upload to ChipFoundry (user is martin-schoeberl)
* [ ] Change example to Chisel top level (with a simple design) and harden it
* [ ] Have some basic tests
* [x] Add DTU subsystem (inclusive memories)
* [x] Make sure to use 10 MHz for the serial port
* [ ] Set pin defines in defines.v
* [x] TODO: there is a mismatch between io_out vs io_gpio_out
* [ ] Explore three different memories
  - [ ] OpenRAM
  - [x] CF RAM
  - [ ] DFF RAM
* [ ] Have a RV Wishbone test to boot Leros
* [ ] Maybe have three versions on the same chip
* [ ] Add some more simple example on the top level (WB IO, Sylvan's RF)
* [ ] Add a block diagram of the project architecture.
* [ ] Include instructions on how to build and simulate the project.

Refer to [README](docs/source/index.md) for basic Caravel documentation.

## Address Map

Wishbone User space is mapped as follows: 0x3000_0000 - 0x300F_FFFF

Let us decide on 0x300n_xxxx where n is:
- 0: Leros CPU 1
- 1: Leros CPU 2
- 2: Leros CPU 3
- 3: Sylvan's Register File
- 4: Maybe a plain WB GPIO
