
import random

from classes import Agent, VacuumEnvironment, Direction, ReflexVacuumAgent, TrivialVacuumEnvironment
"""
Exercise 2.8 implementation
(Based on the problem 2.8 of the Artificial Intelligence. A modern approach 3rd Edition)
For this implementation, the agent can percieve:
1. If it bumped
2. If the place where he is is dirty

The performance measure given was for each action taken, -1 point and for each dirt cleaned, +100 points.

The implemented agent, prioritizes to clean, only if the place is dirty to avoid performing an
innecessary action. It then performs random actions, prioritizing moving forward if not bumped,
and only would shut down if it is at home.
"""

class ReactiveVacuumAgent(Agent):
    def __init__(self):
        super().__init__()
        self.direction = Direction('right')
        self.program = self.__reactive_vacuum_agent_program

    def __reactive_vacuum_agent_program(self, percept):
        dirt, bump = percept
        if dirt == 'Dirty':
            action = 'Suck'
        elif bump == 'Bump':
            action = 'TurnRight'
        else:
            action = 'Forward'
        return action
class ReactiveVacuumAgentWithRandomizeFunction(Agent):
    def __init__(self):
        super().__init__()
        self.direction = Direction('right')
        self.program = self.__reactive_vacuum_agent_program

    def __reactive_vacuum_agent_program(self, percept):
        dirt, bump = percept
        if dirt == 'Dirty':
            action = 'Suck'
        elif bump == 'Bump':
            action = random.choice(['TurnRight', 'TurnLeft'])
        else:
            action = random.choice(['Forward', 'Forward', 'Forward', 'Forward','NoOp','TurnRight', 'TurnLeft'])
        return action




class RandomVacuumAgent(Agent):
    def __init__(self):
        super().__init__()
        self.direction = Direction('right')
        self.program = self.__random_vacuum_agent_program

    def __random_vacuum_agent_program(self, percept):
        return random.choice(['Suck', 'Forward', 'TurnRight', 'TurnLeft', 'NoOp'])



if __name__ == "__main__":
    # Experiment for exercise 
    # Exercise 2.11
    agent = ReflexVacuumAgent()
    environment = TrivialVacuumEnvironment()
    environment.add_thing(agent)
    environment.run()
    print(agent.performance)



    # Exercise 2.14 experiment
    metrics_random = []
    metrics_simple = []
    for i in range(100):
        agent = ReactiveVacuumAgent()
        environment = VacuumEnvironment()
        environment.add_dirt()
        environment.add_thing(agent)
        environment.run()
        metrics_simple.append(agent.performance)

        agent = ReactiveVacuumAgentWithRandomizeFunction()
        environment = VacuumEnvironment()
        environment.add_dirt()
        environment.add_thing(agent)
        environment.run()
        metrics_random.append(agent.performance)
    

    with open('metrics.csv', 'w+') as file:
        file.write('Random,Simple\n')
        for i in range(100):
            file.write(f'{metrics_random[i]},{metrics_simple[i]}\n')