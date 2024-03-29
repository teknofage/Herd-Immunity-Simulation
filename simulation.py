import random, sys
random.seed(42)
from person import Person
from logger import Logger
from virus import Virus
from uuid import uuid4 #universal unique indentifier



class Simulation(object):
    ''' Main class that will run the herd immunity simulation program.
    Expects initialization parameters passed as command line arguments when file is run.

    Simulates the spread of a virus through a given population.  The percentage of the
    population that are vaccinated, the size of the population, and the amount of initially
    infected people in a population are all variables that can be set when the program is run.
    '''
    def __init__(self, pop_size, vacc_percentage, virus, initial_infected=1):
        ''' Logger object logger records all events during the simulation.
        Population represents all Persons in the population.
        The next_person_id is the next available id for all created Persons,
        and should have a unique _id value.
        The vaccination percentage represents the total percentage of population
        vaccinated at the start of the simulation.
        You will need to keep track of the number of people currently infected with the disease.
        The total infected people is the running total that have been infected since the
        simulation began, including the currently infected people who died.
        You will also need to keep track of the number of people that have die as a result
        of the infection.

        All arguments will be passed as command-line arguments when the file is run.
        HINT: Look in the if __name__ == "__main__" function at the bottom.
        '''
        # TODO: Create a Logger object and bind it to self.logger.
        # Remember to call the appropriate logger method in the corresponding parts of the simulation.
        # TODO: Call self._create_population() and pass in the correct parameters.

        # Store the array that this method will return in the self.population attribute.



        # TODO: Store each newly infected person's ID in newly_infected attribute.



        # At the end of each time step, call self._infect_newly_infected()
        # and then reset .newly_infected back to an empty list.
        self.logger = Logger('log.txt')
        self.norm_pop = []
        self.vacc_pop = []
        self.unvacc_pop = []
        self.infected_pop = []
        self.pop_size = pop_size # Int
        self.totalvacc = int(vacc_percentage*self.pop_size)
        self.next_person_id = 0 # Int
        self.virus = virus # Virus object
        self.newly_infected = []
        self.initial_infected = initial_infected # Int
        self.total_infected = initial_infected # Int
        self.current_infected = self.initial_infected
        self.vacc_percentage = vacc_percentage # float between 0 and 1
        self.total_dead = 0 # Int
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(
            virus_name, pop_size, vacc_percentage, initial_infected)
        
        self.time_step_counter = 0
        self._infect_newly_infected()
# def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                    #    basic_repro_num):
        repro_rate = self.virus.repro_rate
        self.logger.write_metadata(pop_size, vacc_percentage, virus.name, mortality_rate, repro_rate)
        self.population = self._create_population(initial_infected) # List of Person objects
        self.time_step_counter = 0

    def _create_population(self, initial_infected):
        '''This method will create the initial population.
            Args:
                initial_infected (int): The number of infected people that the simulation
                will begin with.

            Returns:
                list: A list of Person objects.

        '''
        # TODO: Finish this method!  This method should be called when the simulation
        # begins, to create the population that will be used. This method should return
        # an array filled with Person objects that matches the specifications of the
        # simulation (correct number of people in the population, correct percentage of
        # people vaccinated, correct number of initially infected people).

        # Use the attributes created in the init method to create a population that has
        # the correct intial vaccination percentage and initial infected.
        population = []

#create 3 for loops, one for each type of person
        for _ in range(self.pop_size - self.totalvacc - self.initial_infected):
            norm_person = Person(uuid4(), False)
            self.unvacc_pop.append(norm_person)
            population.append(norm_person)

        for _ in range(self.totalvacc):
            vacc_person = Person(uuid4(), True)
            population.append(vacc_person)
            self.vacc_pop.append(vacc_person)

        for _ in range(self.initial_infected):
<<<<<<< HEAD
            self.infected = Person(uuid4(), False, self.virus)
            population.append(current_infected)
            self.infected_pop.append(current_infected)
        
        
=======
            infected = Person(uuid4(), False, self.virus)
            population.append(infected)
            self.infected_pop.append(infected)


>>>>>>> 934b0ec218f1d91d4a6f3935f40fafc8aebe855d

        return population




    def _simulation_should_continue(self):
        ''' The simulation should only end if the entire population is dead
        or everyone is vaccinated.

            Returns:
                bool: True for simulation should continue, False if it should end.
        '''
        # TODO: Complete this helper method.  Returns a Boolean.
        if self.pop_size == 0 or self.vacc_percentage == 100 or self.current_infected == 0:
            should_continue = False
        else:
            should_continue = True
        return should_continue


    def run(self):
        ''' This method should run the simulation until all requirements for ending
        the simulation are met.
        '''
        # TODO: Finish this method.  To simplify the logic here, use the helper method
        # _simulation_should_continue() to tell us whether or not we should continue
        # the simulation and run at least 1 more time_step.

        # TODO: Keep track of the number of time steps that have passed.
        # HINT: You may want to call the logger's log_time_step() method at the end of each time step.
        # TODO: Set this variable using a helper
        time_step_counter = 0
        should_continue = True
        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus_name, self.virus.mortality_rate, self.virus.repro_rate)

        self.population = self._create_population(self.initial_infected)

        while should_continue:
        # TODO: for every iteration of this loop, call self.time_step() to compute another
        # round of this simulation.
            self.time_step()
            self.logger.log_time_step(self.time_step_counter)

            should_continue = self._simulation_should_continue()


        print('The simulation has ended after {time_step_counter} turns.'.format(self.time_step_counter))
        print('The starting pop was {self.pop_size}. {self.total_dead} amount of people died.'.format(self.pop_size, self.total_dead))
        

    def time_step(self):
        ''' This method should contain all the logic for computing one time step
        in the simulation.

        This includes:
            1. 100 total interactions with a randon person for each infected person
                in the population
            2. If the person is dead, grab another random person from the population.
                Since we don't interact with dead people, this does not count as an interaction.
            3. Otherwise call simulation.interaction(person, random_person) and
                increment interaction counter by 1.
            '''
<<<<<<< HEAD
            
        # TODO: Finish this method.
        for person in self.population:
            print(f"Person Infection: {person.infection}. Person Is Alive: {person.is_alive}")
            if person.infection == None and person.is_alive:
                interactions = 0
                
=======
            #each infected person has 100 interactions of rand person. 4 possible outcomes
            #Infect person, dont infect person, person already infected, already vacced.
            #state changes: if infected -> die or recover. if uninfected -> could become infected or not.
            #mortality_rate detemins state change
            #if infected and did not die you become vacced
            #interactions and state changes are logged.
            #time step happends after state changes are logged.
            #checks if 100 interactions or if everyone has died.
            #full stop
        for person in self.population:
            print(f"Person Infection: {person.infection}. Person Is Alive: {person.is_alive}")
            if person.infection and person.is_alive:
                interactions = 0
>>>>>>> 934b0ec218f1d91d4a6f3935f40fafc8aebe855d
                while interactions < 100:
                    rng = random.randint(0, self.pop_size - 1)
                    if self.population[rng].is_alive == True:
                        interactions +=1
                        self.time_step_counter +=1
                        self.interaction(infected, self.population[rng])
        print(self.time_step_counter)


    def interaction(self, person, random_person):
        '''This method should be called any time two living people are selected for an
        interaction. It assumes that only living people are passed in as parameters.

        Args:
            person1 (person): The initial infected person
            random_person (person): The person that person1 interacts with.
        '''
        # Assert statements are included to make sure that only living people are passed
        # in as params
        assert person.is_alive == True
        assert random_person.is_alive == True

        # TODO: Finish this method.
        #  The possible cases you'll need to cover are listed below:
            # random_person is vaccinated:
            #     nothing happens to random person.
            # random_person is already infected:
            #     nothing happens to random person.
            # random_person is healthy, but unvaccinated:
            #     generate a random number between 0 and 1.  If that number is smaller
            #     than repro_rate, random_person's ID should be appended to
            #     Simulation object's newly_infected array, so that their .infected
            #     attribute can be changed to True at the end of the time step.
        # TODO: Call slogger method during this method.
        infected = True
        if random_person.is_vacc == True:
            infected = False
        elif random_person.virus != None:
            infected = False
        else:
            infection_rng = random.random()
            if infection_rng > self.virus.repro_rate:
                infected = False

        if (infected):
            self.newly_infected.append(random_person._id)

    def _infect_newly_infected(self):
        ''' This method should iterate through the list of ._id stored in self.newly_infected
        and update each Person object with the disease. '''
        # TODO: Call this method at the end of every time step and infect each Person.
        # TODO: Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list.
        for _id in self.newly_infected:
            self.poplulation[_id].virus = self.virus
        self.newly_infected = []


if __name__ == "__main__":
    params = sys.argv[1:]
    virus_name = str(params[0])
    repro_rate = float(params[1])
    mortality_rate = float(params[2])

    pop_size = int(params[3])
    vacc_percentage = float(params[4])

    if len(params) == 6:
        initial_infected = int(params[5])
    else:
        initial_infected = 1

    virus = Virus(virus_name, repro_rate, mortality_rate)
    sim = Simulation(pop_size, vacc_percentage, virus, initial_infected)

    sim.run()
