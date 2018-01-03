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

Simulations are initially added to the *queue* table. When a simulator requests a simulation, the dispatcher takes the next simulation this table and moves it to the *running* table. Once the simulator signals that it has finished that simulation, the dispatcher moves it to the *complete* table. All of this is handled by the dispatcher. The only thing the dispatcher does not do is "generate simulations", that is, adding simulations to the queue. This operation can be performed using SQL commands to insert new entries into the DB (boring and time consuming) or using a tool that hides those commands away. We already include a tool to generate simulations [here](https://github.com/ssbgp/dss-simulation-generator).

## Dependencies

All components require python 3.6 (or later) to be installed. If you are sure your system already includes the correct version of python, you can skip this section. Otherwise, keep reading. We include here some pointers on how to get python installed on different platforms.

##### Windows/MacOS

1. Go to Python's download page https://www.python.org/downloads/
1. Press the *'Download'* for the latest version of python 3. At the time of writing that is version 3.6.4. This will direct you to the download page for that release.
1. Scroll all the way down. There should be a table called *Files* including multiple installers. Download the installer for your OS and architecture.
1. The last step is to run the installer and follow each step.

**IMPORTANT:** make sure **`pip`** is installed.

##### Linux

Most linux distributions come with python 3 pre-installed. Thus, the first step is to check which version is installed. Enter the following command in a terminal.

    python3 -V

If the installed is earlier than 3.6, then you have to install a later version. The best way to install a new python version may differ from distribution to distribution. Our suggestion is to search for the best way to install python 3.6 (or later) on your distribution and install it that way.

After making sure python 3.6 (or later) is installed, you have to make sure `pip` is installed. Most linux distribution include `pip` in their main repositories. To install `pip` follow the indications included in this [guide](https://packaging.python.org/guides/installing-using-linux-tools/) for your linux distribution.


## Configure and Run Dispatcher

The dispatcher is implemented as a server listening for requests from one or more simulators.

1. Make sure python 3.6 (or later) is installed in your system, see [Dependencies](#dependencies).
1. Clone dispatcher repository

        git clone https://github.com/ssbgp/dss-dispatcher.git

1. Move to project cloned directory

        cd dss-dispatcher

1. Install dispatcher

        python -m pip install . --user
        python -m pip install -r requirements.txt --user

   _**Warning: some distributions use python3 instead of python to call the python 3 interpreter.**_

1. Create the directory to store some configuration file, including the simulation queue.
1. Run it

        ssbgp-dss-dispatcher <directory>

   Replace `<directory>` with the directory created on the previous step.

##### How to listen on a different port?
By default, the dispatcher will listens for requests from the simulators on port 32014. You can change this port using the `--port` option. To change the listening port to 5000 do the following.

        ssbgp-dss-dispatcher <directory> --port=5000

##### How to ask for help?
Use options `-h/--help`.

        ssbgp-dss-dispatcher --help

## Configure and Run Simulator

The simulator is implemented as a client for the dispatcher. Once it is started, it asks the dispatcher for a new simulation. If the dispatcher has no simulations to dispatch, the simulator starts to check periodically for new simulations.

1. Make sure python 3.6 (or later) is installed in your system, see [Dependencies](#dependencies).
1. Clone simulator repository

        git clone https://github.com/ssbgp/dss-simulator.git

1. Move to project cloned directory

        cd dss-simulator

1. Install simulator

        python -m pip install . --user
        python -m pip install -r requirements.txt --user

   _**Warning: some distributions use python3 instead of python to call the python 3 interpreter.**_

1. Create a directory to store the data obtained from the simulations. This is the *installation directory*.
1. Run it

        ssbgp-dss-simulator <directory>

   Replace `<directory>` with the *installation* directory, created on the previous step.

By default, the dispatcher will listens for requests from the simulators on port 32014. You can change this port using the `--port` option. To change the listening port to 5000 do the following.

        ssbgp-dss-dispatcher <directory> --port=5000

##### Where is data stored?
Data is dumped to a sub-directory called `complete` inside the *installation directory*.

##### How to set the dispatcher IP address and Port?
By default, the simulator assumes the dispatcher is running on the localhost and listening on port port 32014. To have the simulator connect to a different address/port use the following command.

        ssbgp-dss-simulator <directory> --addr=192.168.1.100 --port=5000

This command indicates the dispatcher is running at the address `192.168.1.100` and listening on port `5000`.

##### How to run multiple simulators on the same machine?
Create a different install directory for each simulator. For instance, if we want to have two different simulators,

1. Create two directories: `sim01` and `sim02`
1. Run one simulator instance for each directory

        ssbgp-dss-simulator sim01/
        ssbgp-dss-simulator sim02/

##### How to ask for help?
Use options `-h/--help`.

        ssbgp-dss-dispatcher --help
