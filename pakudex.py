from pakuri import *


class Pakudex:

    def __init__(self, capacity=20):
        self.capacity = capacity  # initialized value is 20
        self.pakuris = []  # store list of pakuri objects
        self.size = 0  # how many pakuris are already in the list

    def get_size(self):
        return self.size

    def get_capacity(self):
        return self.capacity

    # return string list of Pakuri objects as ordered in Pakudex
    def get_species_array(self):
        species_list = []
        for each_pakuri in self.pakuris:
            species_list.append(each_pakuri.get_species())
        if len(species_list) == 0:
            return None
        else:
            return species_list

    # return an int list containing attack, defense, speed stats of species
    def get_stats(self, species):
        int_list = []
        for critters in self.pakuris:
            if species == critters.get_species():  # check that the Pakuri already exists
                int_list.extend([critters.get_attack(), critters.get_defense(), critters.get_speed()])
        # if species not in Pakudex, return None
        if len(int_list) < 1:
            int_list = None
        return int_list

    # Sorts pakuri objects in pakudex by SPECIES NAME by lexicographical
    def sort_pakuri(self):
        self.pakuris.sort(key=lambda pakuri: pakuri.get_species())

    def add_pakuri(self, species):
        # check if the list is full
        if self.size == self.capacity:
            return False

        # check for duplicates based off species name
        if self.get_species_array() is not None:
            if species in self.get_species_array():
                return False

        self.pakuris.append(Pakuri(species))  # add Pakuri object to Pakudex
        self.size += 1
        return True  # means that new Pakuri was successfully added

    # successful evolve return true, return false otherwise
    def evolve_species(self, species):  # change name to evolve species
        for critters in self.pakuris:
            if critters.get_species() == species:  # check that the Pakuri already exists
                critters.evolve()
                return True
        return False


