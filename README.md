# Caravel Leros Project

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) [![UPRJ_CI](https://github.com/chipfoundry/caravel_user_project/actions/workflows/user_project_ci.yml/badge.svg)](https://github.com/chipfoundry/caravel_user_project/actions/workflows/user_project_ci.yml)

This is a user project for the Caravel harness, integrating the open-source Leros CPU core.

Checkout with submodules:

    git clone --recurse-submodules git@github.com:os-chip-design/caravel_leros_2025.git

Or later:

    git submodule update --init --recursive

Then build the project as described in [the Docs](docs/source/index.md).

This repository contains the DTU subsystem from the [Edu4Chip](https://edu4chip.github.io/) tapeout project.

Build the Leros with the CF RAM memory:

    pip install cf-ipm
    ipm install CF_SRAM_1024x32

    make leros-cfram


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
* [ ] Make sure to use 10 MHz for the serial port
* [ ] Set pin defines in defines.v
* [ ] Explore three different memories
  - [ ] OpenRAM
  - [x] CF RAM
  - [ ] DFF RAM
* [ ] Have RV Wishbone test to boot Leros
* [ ] Maybe have three versions on the same chip
* [ ] Add a block diagram of the project architecture.
* [ ] Include instructions on how to build and simulate the project.
* [ ] Add more details about the project, its features, and how to use it.


Refer to [README](docs/source/index.md) for basic caravel documentation.
