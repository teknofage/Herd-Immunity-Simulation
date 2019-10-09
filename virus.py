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

    Cercopithecine_herpesvirus = Virus("Cercopithecine herpesvirus", 0.5, 0.2)
    assert virus.name == "Cercopithecine herpesvirus"
    assert virus.repro_rate == 0.5
    assert virus.mortality_rate == 0.2

    Purple_Sock_Fiend_Virus = Virus("Purple Sock Fiend Virus", 0.5, 0.9)
    assert virus.name == "Purple Sock Fiend Virus"
    assert virus.repro_rate == 0.5
    assert virus.mortality_rate == 0.9

    Elephantitis_Hemorrhoids = Virus("Elephantitis Hemorrhoids", 0.2, 0.9)
    assert virus.name == "Elephantitis Hemorrhoids"
    assert virus.repro_rate == 0.2
    assert virus.mortality_rate == 0.9

    Malaria = Virus("Malaria", 0.6, 0.1)
    assert virus.name == "maliria"
    assert malaria.repro_rate == 0.6
    assert malaria.mortality_rate == 0.1

    Black_Death = Virus("Black Death", 0.8, 0.7)
    assert Black_Death.name == "Black Death"
    assert Black_Death.repro_rate == 0.8
    assert Black_Death.mortality_rate == 0.7

    Chicken_Pox = Virus("Chicken Pox", 0.2, 0.275)
    assert Chicken_Pox.name == "Chicken Pox"
    assert Chicken_Pox.repro_rate == 0.2
    assert Chicken_Pox.mortality_rate == 0.275

    Ebola = Virus('Ebola', 0.5, 0.8)
    assert Ebola.name == "Ebola"
    assert Ebola.repro_rate == 0.5
    assert Ebola.mortality_rate == 0.8

    Measles = Virus("Measles", 0.6, 0.9)
    assert Measles.name == "Measles"
    assert Measles.repro_rate == 0.6
    assert Measles.mortality_rate == 0.9

    
