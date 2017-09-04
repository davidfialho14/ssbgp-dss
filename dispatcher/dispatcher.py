class Dispatcher:
    """
    The dispatcher distributes simulations to multiple simulators which
    execute them.

    Its job is to manage a queue of simulations and assign each of them to
    simulators to be executed.

    When a simulator is available for processing, it asks the dispatcher for
    a simulation to run. The dispatcher looks into the simulation queue and
    takes the next simulation in the queue and sends it to the simulator to
    be executed. Once the simulator finishes the simulation, it notifies the
    dispatcher. The dispatcher then marks the simulation as `complete` stores
    a record of when was the simulation complete and which simulator executed
    the simulation.

    In order to ask for simulations, a simulator must register with the
    dispatcher first. Registering will give the simulator an ID that will
    uniquely identify it in the system.
    """

    def register(self) -> str:
        """
        Registers a simulator with the system and returns the unique ID of
        the newly registered simulator.

        :return: the ID assigned to the new simulator
        """

    def next_simulation(self, simulator_id: str) -> dict:
        """
        It pops the next simulation in the queue, assigns it to the simulator
        with the specified ID, and returns the simulation parameters.

        :param simulator_id:
        :return: the simulation parameters of the next simulation in the queue
        """

    def notify_finished(self, simulator_id: str, simulation_id: str):
        """
        Informs the dispatcher that the simulation with the specified ID was
        executed.

        :param simulator_id:  ID of the simulator that executed the simulation
        :param simulation_id: ID of the simulation that was executed
        """

    def notify_failed(self, simulator_id: str, simulation_id: str):
        """
        Tells the dispatcher to mark the simulation with the specified ID as
        failed.

        :param simulator_id:  ID of the simulator notifying
        :param simulation_id: ID of the simulation to mark as failed
        :return:
        """
