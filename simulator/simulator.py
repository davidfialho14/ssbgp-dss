class Simulator:
    """
    The simulator's main function is to execute simulations and store
    the data reports they generate.

    Simulations are obtained from a dispatcher. When a simulator is available
    for executing a new simulation it connects to the dispatcher and asks for
    a new simulation. The dispatcher responds with a set of simulation
    parameters, including an ID that the dispatcher uses to uniquely identify
    the simulation. After finishing a simulation the simulator notifies the
    dispatcher, indicating the ID of the finished simulation.

    When a simulation fails for some reason the simulator logs the simulation
    that failed and re-executes the simulation. It tries to include as much
    information as possible in the error log. The simulation is only
    re-executed once. If the simulation fails a second time, then the
    simulator asks the dispatcher to mark the simulation as failed and asks
    for a new simulation.
    """
