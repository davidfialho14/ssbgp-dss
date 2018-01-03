# SS-BGP: Distributed Simulation System

A distributed simulation system (DSS) for the [SS-BGP simulator](https://github.com/ssbgp/simulator). This repository does include any actual code. Since the DSS is composed of multiple components it makes perfect sense to have one repository for each component. Hence, this repository serves as the entry point for the DSS.

This document serves as basic documentation for the DSS. It describes the basic architecture of the system and shows the necessary steps to configure and run each component of the DSS.

## Architecture

The DSS is composed of three different components:

- simulation queue
- [dispatcher](https://github.com/ssbgp/dss-dispatcher)
- [simulator](https://github.com/ssbgp/dss-simulator)

There is only a single simulation queue and a single dispatcher. But, there might be multiple simulators. The simulation queue holds a set of simulations that need to be executed. The dispatcher takes simulations from this queue and distributes them between all simulators that are available. Each simulator runs one simulation at a time. Once a simulator finishes running a simulation, it requests a new simulation from the dispatcher.

The simulation queue is implemented using a file based database (DB) called [SQLite](https://sqlite.org/). This DB contains 4 main tables:

- *simulation*, containing all simulations added to the DB
- *queue*, contains the simulations that are in the queue
- *running*, contains the simulations that are currently being run by some simulator
- *complete*, contains the simulations that have already been run

Simulations are initially added to the *queue* table. When a simulator requests a simulation, the dispatcher takes the next simulation this table and moves it to the *running* table. Once the simulator signals that it has finished that simulation, the dispatcher moves it to the *complete* table. All of this is handled by the dispatcher. The only thing the dispatcher does not do is "generate simulations", that is, adding simulations to the queue. This operation can be performed by some other tool. We already include a tool to generate simulation [here]().

## Configure and Run Dispatcher

#### How to add simulations to the queue?

#### How to set priorities among simulations?

## Configure and Run Simulator
