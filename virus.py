class Virus(object):
    '''Properties and attributes of the virus used in Simulation.'''

    def __init__(self, name, repro_rate, mortality_rate):
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate


def test_virus_instantiation():
    #TODO: Create your own test that models the virus you are working with
    '''Check to make sure that the virus instantiator is working.'''
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3

    virus = Virus("Cercopithecine herpesvirus", 0.5, 0.2)
    assert virus.name == "Cercopithecine herpesvirus"
    assert virus.repro_rate == 0.5
    assert virus.mortality_rate == 0.2

   virus = Virus("Purple Sock Fiend Virus", 0.5, 0.9)
   assert virus.name == "Purple Sock Fiend Virus"
   assert virus.repro_rate == 0.5
   assert virus.mortality_rate == 0.9

   virus = Virus("Elephantitis Hemorrhoids", 0.2, 0.9)
   assert virus.name == "Elephantitis Hemorrhoids"
   assert virus.repro_rate == 0.2
   assert virus.mortality_rate == 0.9
