
def create_registers():
    registers = {}
    for i in range(32):
        registers["R" + str(i)] = 0
    registers["R1"] = 10
    registers["R2"] = 20
    registers["R3"] = 100
    registers["R4"] = 200
    return registers
def create_memory():
    memory = {
        100: 50,
        200: 75,
        300: 100,
        400: 150
    }
    return memory
def check_register(name):
    name = name.upper()
    if not name.startswith("R"):
        return False
    number = name[1:]
    if not number.isdigit():
        return False
    number = int(number)
    if number < 0 or number > 31:
        return False
    return True
def get_register(registers, name):
    name = name.upper()
    if not check_register(name):
        raise ValueError(
            "Invalid register: " + name
        )
    return registers[name]
def display_registers(registers):
    print("\n---------- REGISTER VALUES ----------")
    for i in range(32):
        name = "R" + str(i)
        print(
            name,
            "=",
            registers[name]
        )
    print("-------------------------------------")
def display_memory(memory):
    print("\n---------- MEMORY VALUES ----------")
    for address in sorted(memory):
        print(
            "Mem[" + str(address) + "] =",
            memory[address]
        )
    print("-----------------------------------")
def immediate_addressing():

    print("\n")
    print("=" * 55)
    print("           IMMEDIATE ADDRESSING")
    print("=" * 55)
    value = input(
        "\nEnter immediate value: "
    )
    try:
        value = int(value)
        print("\nInstruction: MOV R1, #" + str(value))
        print(
            "Operand value =",
            value
        )
        print(
            "\nResult: The value is directly present "
            "in the instruction."
        )
    except ValueError:
        print("\nInvalid number!")
def register_addressing(registers):
    print("\n")
    print("=" * 55)
    print("            REGISTER ADDRESSING")
    print("=" * 55)
    source = input(
        "\nEnter source register: "
    ).upper()
    try:
        value = get_register(
            registers,
            source
        )
        print(
            "\nInstruction: MOV R1, " + source
        )
        print(
            "Register", source,
            "contains", value
        )
        print(
            "\nOperand value =",
            value
        )
        print(
            "\nResult: The operand is stored "
            "inside a register."
        )
    except ValueError as error:
        print("\nERROR:", error)
def base_displacement_addressing(registers, memory):
    print("\n")
    print("=" * 55)
    print("        BASE / DISPLACEMENT ADDRESSING")
    print("=" * 55)
    print("\nExample:")
    print("LW R1, 8(R2)")
    base = input(
        "\nEnter base register: "
    ).upper()
    displacement = input(
        "Enter displacement: "
    )
    try:
        base_value = get_register(
            registers,
            base
        )
        displacement = int(displacement)
        effective_address = (
            base_value + displacement
        )
        value = memory.get(
            effective_address,
            0
        )
        print(
            "\nBase register value =",
            base_value
        )
        print(
            "Displacement =",
            displacement
        )
        print(
            "\nEffective Address =",
            base_value,
            "+",
            displacement,
            "=",
            effective_address
        )
        print(
            "Memory value =",
            value
        )
        print(
            "\nResult: Effective address is calculated "
            "using base register + displacement."
        )
    except ValueError as error:
        print("\nERROR:", error)
def direct_addressing(memory):
    print("\n")
    print("=" * 55)
    print("             DIRECT ADDRESSING")
    print("=" * 55)
    address = input(
        "\nEnter memory address: "
    )
    try:
        address = int(address)
        value = memory.get(
            address,
            0
        )
        print(
            "\nInstruction: LOAD R1,",
            address
        )
        print(
            "Memory address =",
            address
        )
        print(
            "Memory value =",
            value
        )
        print(
            "\nResult: The instruction directly "
            "contains the memory address."
        )
    except ValueError:
        print("\nInvalid memory address!")
def indirect_addressing(registers, memory):
    print("\n")
    print("=" * 55)
    print("            INDIRECT ADDRESSING")
    print("=" * 55)
    register = input(
        "\nEnter register containing address: "
    ).upper()
    try:
        address = get_register(
            registers,
            register
        )
        value = memory.get(
            address,
            0
        )
        print(
            "\nRegister", register,
            "contains address =", address
        )
        print(
            "Effective Address =",
            address
        )
        print(
            "Memory value =",
            value
        )
        print(
            "\nResult: The register contains "
            "the memory address of the operand."
        )
    except ValueError as error:
        print("\nERROR:", error)
def compare_modes():
    print("\n")
    print("=" * 65)
    print("              ADDRESSING MODE COMPARISON")
    print("=" * 65)
    print(
        "\n1. Immediate       -> Operand is directly in instruction"
    )
    print(
        "2. Register        -> Operand is stored in a register"
    )
    print(
        "3. Base/Displacement -> Address = Base + Displacement"
    )
    print(
        "4. Direct          -> Instruction contains memory address"
    )
    print(
        "5. Indirect        -> Register contains memory address"
    )
    print("\n" + "=" * 65)
def main():
    registers = create_registers()
    memory = create_memory()
    while True:
        print("\n")
        print("=" * 65)
        print("              ADDRESSING MODE ANALYZER")
        print("                  COA MINI PROJECT 2")
        print("=" * 65)
        print("\n1. Immediate Addressing")
        print("2. Register Addressing")
        print("3. Base / Displacement Addressing")
        print("4. Direct Addressing")
        print("5. Indirect Addressing")
        print("6. Compare All Addressing Modes")
        print("7. Show Registers")
        print("8. Show Memory")
        print("0. Return to Main Menu")
        print("=" * 65)
        choice = input(
            "\nEnter your choice: "
        ).strip()
        if choice == "1":
            immediate_addressing()
            input(
                "\nPress ENTER to continue..."
            )
        elif choice == "2":
            register_addressing(
                registers
            )
            input(
                "\nPress ENTER to continue..."
            )
        elif choice == "3":
            base_displacement_addressing(
                registers,
                memory
            )
            input(
                "\nPress ENTER to continue..."
            )
        elif choice == "4":
            direct_addressing(
                memory
            )
            input(
                "\nPress ENTER to continue..."
            )
        elif choice == "5":
            indirect_addressing(
                registers,
                memory
            )
            input(
                "\nPress ENTER to continue..."
            )
        elif choice == "6":
            compare_modes()
            input(
                "\nPress ENTER to continue..."
            )
        elif choice == "7":
            display_registers(
                registers
            )
            input(
                "\nPress ENTER to continue..."
            )
        elif choice == "8":
            display_memory(
                memory
            )
            input(
                "\nPress ENTER to continue..."
            )
        elif choice == "0":
            break
        else:

            print(
                "\nInvalid choice!"
            )
if __name__ == "__main__":
    main()