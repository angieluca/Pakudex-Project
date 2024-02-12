from pakuri import *
from pakudex import *


def main():

    print("Welcome to Pakudex: Tracker Extraordinaire!")

    # confirm possible capacity
    capacity = False
    while not capacity:
        user_capacity = input("Enter max capacity of the Pakudex: ")
        if user_capacity.isnumeric():
            user_capacity = int(user_capacity)
            capacity = True
        else:
            print("Please enter a valid size.")

    user_pakudex = Pakudex(user_capacity)  # create a Pakudex instance with given capacity
    print("The Pakudex can hold", user_capacity, "species of Pakuri.")

    while True:
        print("\nPakudex Main Menu\n-----------------\n1. List Pakuri\n2. Show Pakuri\n"
              "3. Add Pakuri\n4. Evolve Pakuri\n5. Sort Pakuri\n6. Exit")
        user_choice = input("\nWhat would you like to do? ")

        # Exit program
        if user_choice == '6':
            print("Thanks for using Pakudex! Bye!")
            return False

        # List Pakuri
        elif user_choice == '1':
            if user_pakudex.get_size() != 0:  # checks that there are Pakuris in Pakudex
                print("Pakuri In Pakudex:")
                i = 1
                for critter in user_pakudex.pakuris:
                    print(i, critter.get_species(), sep=". ")
                    i += 1
            else:
                print("No Pakuri in Pakudex yet!")

        # Show Pakuri
        elif user_choice == '2':
            user_species = input("Enter the name of the species to display: ")
            final_stats = user_pakudex.get_stats(user_species)
            if final_stats:
                print("Species:", user_species)
                stats_list = ["Attack", "Defense", "Speed"]
                for i in range(3):
                    print(stats_list[i], final_stats[i], sep=": ")
            else:
                print("Error: No such Pakuri!")

        # Add Pakuri
        elif user_choice == '3':
            if user_pakudex.get_size() == user_pakudex.get_capacity():
                print("Error: Pakudex is full!")
            else:
                user_add = input("Enter the name of the species to add: ")
                if user_pakudex.add_pakuri(user_add):  # true if successfully added
                    print("Pakuri species", user_add, "successfully added!")
                else:
                    print("Error: Pakudex already contains this species!")  # only other reason add_pakuri() returned F

        # Evolve Pakuri
        elif user_choice == '4':
            user_evolve = str(input("Enter the name of the species to evolve: "))
            if user_pakudex.evolve_species(user_evolve):
                print(user_evolve, "has evolved!")
            else:
                print("Error: No such Pakuri!")

        # Sort Pakuri
        elif user_choice == '5':
            user_pakudex.sort_pakuri()
            print("Pakuri have been sorted!")

        else:
            print("Unrecognized menu selection!")


if __name__ == "__main__":
    main()
