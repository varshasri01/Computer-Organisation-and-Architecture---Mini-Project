from project1_mips_simulator import main as run_project1
from project2_addressing_modes import main as run_project2
from project3_computer_arithmetic import main as run_project3
from project4_pipeline import run_project4
from project5_cache import run_project5
def display_menu():
    """
    Display the list of available COA projects.
    """

    print("\n")
    print("=" * 60)
    print("              COA MINI PROJECTS")
    print("=" * 60)

    print("1. MIPS Instruction Execution Simulator")
    print("2. Addressing Mode Analyzer")
    print("3. Computer Arithmetic Analyzer")
    print("4. 5-stage MIPS pipeline Simulator")
    print("5. Cache Mapping Simulator")
    print("0. Exit")

    print("=" * 60)


# ------------------------------------------------------------
# MAIN PROGRAM
# ------------------------------------------------------------

def main():

    while True:

        display_menu()

        choice = input("Enter your choice: ").strip()

        # ----------------------------------------------------
        # PROJECT 1
        # ----------------------------------------------------

        if choice == "1":

            print("\n")
            print("=" * 60)
            print("       PROJECT 1 - MIPS INSTRUCTION SIMULATOR")
            print("=" * 60)

            run_project1()

            input(
                "\nPress ENTER to return to the main menu..."
            )

        # ----------------------------------------------------
        # PROJECT 2
        # ----------------------------------------------------

        elif choice == "2":

            print("\n")
            print("=" * 60)
            print("        PROJECT 2 - ADDRESSING MODE ANALYZER")
            print("=" * 60)

            run_project2()

            input(
                "\nPress ENTER to return to the main menu..."
            )

        # ----------------------------------------------------
        # PROJECT 3
        # ----------------------------------------------------

        elif choice == "3":

            print("\n")
            print("=" * 60)
            print("        PROJECT 3 - COMPUTER ARITHMETIC ANALYZER")
            print("=" * 60)

            run_project3()

            input(
                "\nPress ENTER to return to the main menu..."
            )

        # ----------------------------------------------------
        # PROJECT 4
        # ----------------------------------------------------

        elif choice == "4":
            run_project4()
            input(
                "\nPress ENTER to return to the main menu..."
            )

        # ----------------------------------------------------
        # PROJECT 5
        # ----------------------------------------------------

        elif choice == "5":
            run_project5()
            input(
                "\nPress ENTER to return to the main menu..."
            )

        # ----------------------------------------------------
        # EXIT
        # ----------------------------------------------------

        elif choice == "0":

            print("\n")
            print("=" * 60)
            print("        Thank you for using COA Projects!")
            print("=" * 60)
            print()

            break

        # ----------------------------------------------------
        # INVALID CHOICE
        # ----------------------------------------------------

        else:

            print(
                "\nInvalid choice!"
                "\nPlease enter a number from 0 to 5."
            )


# ------------------------------------------------------------
# PROGRAM ENTRY POINT
# ------------------------------------------------------------

if __name__ == "__main__":
    main()