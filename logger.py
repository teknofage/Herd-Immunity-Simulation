import os # os allows you to work with files and system commnds

class Logger(object):
    ''' Utility class responsible for logging all interactions during the simulation. '''
    # TODO: Write a test suite for this class to make sure each method is working
    # as expected.


    # PROTIP: Write your tests before you solve each function, that way you can
    # test them one by one as you write your class.

    def __init__(self, file_name):
        # TODO:  Finish this initialization method. The file_name passed should be the
        # full file name of the file that the logs will be written to.
        self.file_name = None

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       repro_rate):
        '''
        The simulation class should use this method immediately to log the specific
        parameters of the simulation as the first line of the file.
        '''

        # TODO: Finish this method. This line of metadata should be tab-delimited
        # it should create the text file that we will store all logs in.
        # TIP: Use 'w' mode when you open the file. For all other methods, use
        # the 'a' mode to append a new log to the end, since 'w' overwrites the file.
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!

        # create a text file
        log = open("log.txt", 'w+')
        log.close()

        # logadd appends text file
        logadd = open('log.txt', 'a+')

        #these commands write to logadd
        logadd.write (str(pop_size) + '\n')
        logadd.write (str(vacc_percentage) + '\n')
        logadd.write(virus_name + '\n')
        logadd.write (str(mortality_rate) + '\n')
        logadd.write (str(repro_rate) +'\n')



    def log_interaction(self, person, random_person, random_person_sick=None,
                        random_person_vacc=None, did_infect=None):
        '''
        The Simulation object should use this method to log every interaction
        a sick person has during each time step.

        The format of the log should be: "{person.ID} infects {random_person.ID} \n"

        or the other edge cases:
            "{person.ID} didn't infect {random_person.ID} because {'vaccinated' or 'already sick'} \n"
        '''
        # TODO: Finish this method. Think about how the booleans passed (or not passed)
        # represent all the possible edge cases. Use the values passed along with each person,
        # along with whether they are sick or vaccinated when they interact to determine
        # exactly what happened in the interaction and create a String, and write to your logfile.

        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #Case responces: is vacc, is already infected, is infected, is not infected
        with open(self.log.txt, "a") as log:
            #1: person infected random_person.
            if random_person_sick == False and not random_person_vacc:
                did_infect == True
                random_person_sick == True
                print(f"{random_person} got infected by {person}")

            #2: person didn't infect random_person because they are is_vaccinated.
            elif random_person_vacc == True:
                print(f"{person} did not infect {random_person} because they are vaccinated")
                did_infect == False
                random_person_sick == False

            #3: person didn't infect random_person because they were already infected.

            elif random_person_vacc == True:
                print(f"{person} did not infect {random_person} because they are already infected")
                did_infect == False
                random_person_sick == True

                #4: person didn't infect random_person just cause.
            elif random_person_vacc == False and random_person:
                did_infect == False
                random_person_sick == False
                print(f"{random_person} did not get infected.")



    def log_infection_survival(self, person, did_die_from_infection):
        ''' The Simulation object uses this method to log the results of every
        call of a Person object's .resolve_infection() method.

        The format of the log should be:
            "{person.ID} died from infection\n" or "{person.ID} survived infection.\n"
        '''
        # TODO: Finish this method. If the person survives, did_die_from_infection
        # should be False.  Otherwise, did_die_from_infection should be True.
        # Append the results of the infection to the logfile

        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        with open(self.log.txt, "a") as log:

            if did_die_from_infection == True:
                print(f"{person} died.")
        # is dead = person died
            elif did_die_from_infection == False:
                print (f"{person} lived.")
        # in not dead = survived infection
        

    # def log_time_step(self, time_step_number):
    #     ''' STRETCH CHALLENGE DETAILS:
    #
    #     If you choose to extend this method, the format of the summary statistics logged
    #     are up to you.
    #
    #     At minimum, it should contain:
    #         The number of people that were infected during this specific time step.
    #         The number of people that died on this specific time step.
    #         The total number of people infected in the population, including the newly infected
    #         The total number of dead, including those that died during this time step.
    #
    #     The format of this log should be:
    #         "Time step {time_step_number} ended, beginning {time_step_number + 1}\n"
    #     '''
        # TODO: Finish this method. This method should log when a time step ends, and a
        # new one begins.
        # NOTE: Here is an opportunity for a stretch challenge!
        pass
