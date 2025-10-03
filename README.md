# Caravel Leros Project

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) [![UPRJ_CI](https://github.com/chipfoundry/caravel_user_project/actions/workflows/user_project_ci.yml/badge.svg)](https://github.com/chipfoundry/caravel_user_project/actions/workflows/user_project_ci.yml)

This is a user project for the Caravel harness, integrating the open-source Leros CPU core.

Checkout with submodules:

    git clone --recurse-submodules git@github.com:os-chip-design/caravel_leros_2025.git

Then build the project as described in [the Docs](docs/source/index.md).

This repository contains the DTU subsystem from the [Edu4Chip](https://edu4chip.github.io/) tapeout project.


## TODO

* [x] Setup Caravel on Mac (MS, TP)
* [x] Setup Caravel on chipdesign1
* [x] Harden the example project
* [ ] Run the provided tests
* [ ] MPW check
* [ ] Test upload to ChipFoundry
* [ ] Change example to Chisel top level and synthesize it
* [ ] Have some basic tests
* [ ] Add DTU subsystem (inclusive memories)
* [ ] Explore three different memories
  - [ ] OpenRAM
  - [ ] EF RAM
  - [ ] DFF RAM
* [ ] Maybe have three versions on the same chip
* [ ] Add a block diagram of the project architecture.
* [ ] Include instructions on how to build and simulate the project.
* [ ] Add more details about the project, its features, and how to use it.


Refer to [README](docs/source/index.md) for basic caravel documentation.
