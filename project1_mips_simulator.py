# ============================================================
# COA MINI PROJECT 1
# MIPS INSTRUCTION EXECUTION SIMULATOR
# ============================================================

# -----------------------------
# Create 32 MIPS registers
# -----------------------------

def create_registers():

    registers = {}

    for i in range(32):
        registers["R" + str(i)] = 0

    # Initial values for testing
    registers["R1"] = 10
    registers["R2"] = 20
    registers["R3"] = 5
    registers["R4"] = 100

    return registers


# -----------------------------
# Create initial memory
# -----------------------------

def create_memory():

    memory = {
        100: 50,
        104: 75,
        108: 100
    }

    return memory


# -----------------------------
# Display registers
# -----------------------------

def display_registers(registers):

    print("\n---------- REGISTER VALUES ----------")

    for i in range(32):

        name = "R" + str(i)

        print(name, "=", registers[name])

    print("-------------------------------------")


# -----------------------------
# Display memory
# -----------------------------

def display_memory(memory):

    print("\n---------- MEMORY VALUES ----------")

    for address in sorted(memory):

        print("Mem[" + str(address) + "] =", memory[address])

    print("-----------------------------------")


# -----------------------------
# Check whether register is valid
# -----------------------------

def check_register(register):

    register = register.upper()

    if not register.startswith("R"):
        return False

    number = register[1:]

    if not number.isdigit():
        return False

    number = int(number)

    if number < 0 or number > 31:
        return False

    return True


# -----------------------------
# Get register value
# -----------------------------

def get_register(registers, name):

    name = name.upper()

    if not check_register(name):
        raise ValueError("Invalid register: " + name)

    return registers[name]


# -----------------------------
# Store value in register
# -----------------------------

def set_register(registers, name, value):

    name = name.upper()

    if not check_register(name):
        raise ValueError("Invalid register: " + name)

    # R0 is always zero in MIPS
    if name != "R0":
        registers[name] = value


# -----------------------------
# Calculate memory address
# Example: 4(R4)
# If R4 = 100, address = 104
# -----------------------------

def get_address(registers, value):

    value = value.replace(" ", "").upper()

    if "(" not in value or ")" not in value:
        raise ValueError(
            "Memory address should be like 4(R4)"
        )

    left = value.find("(")
    right = value.find(")")

    offset_text = value[:left]
    register_name = value[left + 1:right]

    # If no offset is given, use 0
    if offset_text == "":
        offset = 0
    else:
        try:
            offset = int(offset_text)
        except ValueError:
            raise ValueError("Invalid memory offset")

    if not check_register(register_name):
        raise ValueError(
            "Invalid base register: " + register_name
        )

    base_address = registers[register_name]

    return base_address + offset


# -----------------------------
# Clean the instruction
# -----------------------------

def prepare_instruction(instruction):

    # Remove comments
    instruction = instruction.split("#")[0]

    # Replace comma with space
    instruction = instruction.replace(",", " ")

    # Split into parts
    parts = instruction.split()

    return parts


# ============================================================
# EXECUTE MIPS INSTRUCTIONS
# ============================================================

def run(instructions, registers, memory):

    pc = 0
    step = 1

    # This prevents infinite loops
    max_steps = 100

    print("\n========== EXECUTION ==========")

    while step <= max_steps:

        # Convert PC to instruction number
        instruction_number = pc // 4

        # Stop when all instructions are completed
        if instruction_number < 0 or instruction_number >= len(instructions):
            break

        original_instruction = instructions[instruction_number]

        parts = prepare_instruction(original_instruction)

        # Empty line
        if len(parts) == 0:
            pc = pc + 4
            continue

        operation = parts[0].upper()

        old_pc = pc

        branch_taken = False
        jump_taken = False

        try:

            # ------------------------------------------------
            # ADD
            # ADD R5,R1,R2
            # ------------------------------------------------

            if operation == "ADD":

                if len(parts) != 4:
                    raise ValueError(
                        "ADD needs 3 registers"
                    )

                rd = parts[1]
                rs = parts[2]
                rt = parts[3]

                result = (
                    get_register(registers, rs)
                    + get_register(registers, rt)
                )

                set_register(registers, rd, result)

            # ------------------------------------------------
            # SUB
            # SUB R5,R1,R2
            # ------------------------------------------------

            elif operation == "SUB":

                if len(parts) != 4:
                    raise ValueError(
                        "SUB needs 3 registers"
                    )

                rd = parts[1]
                rs = parts[2]
                rt = parts[3]

                result = (
                    get_register(registers, rs)
                    - get_register(registers, rt)
                )

                set_register(registers, rd, result)

            # ------------------------------------------------
            # AND
            # AND R5,R1,R2
            # ------------------------------------------------

            elif operation == "AND":

                if len(parts) != 4:
                    raise ValueError(
                        "AND needs 3 registers"
                    )

                rd = parts[1]
                rs = parts[2]
                rt = parts[3]

                result = (
                    get_register(registers, rs)
                    & get_register(registers, rt)
                )

                set_register(registers, rd, result)

            # ------------------------------------------------
            # OR
            # OR R5,R1,R2
            # ------------------------------------------------

            elif operation == "OR":

                if len(parts) != 4:
                    raise ValueError(
                        "OR needs 3 registers"
                    )

                rd = parts[1]
                rs = parts[2]
                rt = parts[3]

                result = (
                    get_register(registers, rs)
                    | get_register(registers, rt)
                )

                set_register(registers, rd, result)

            # ------------------------------------------------
            # ADDI
            # ADDI R5,R1,10
            # ------------------------------------------------

            elif operation == "ADDI":

                if len(parts) != 4:
                    raise ValueError(
                        "ADDI needs a destination register, "
                        "source register and number"
                    )

                rt = parts[1]
                rs = parts[2]

                try:
                    number = int(parts[3])
                except ValueError:
                    raise ValueError(
                        "Invalid immediate value"
                    )

                result = get_register(registers, rs) + number

                set_register(registers, rt, result)

            # ------------------------------------------------
            # SLT
            # SLT R5,R1,R2
            # ------------------------------------------------

            elif operation == "SLT":

                if len(parts) != 4:
                    raise ValueError(
                        "SLT needs 3 registers"
                    )

                rd = parts[1]
                rs = parts[2]
                rt = parts[3]

                if (
                    get_register(registers, rs)
                    < get_register(registers, rt)
                ):
                    result = 1
                else:
                    result = 0

                set_register(registers, rd, result)

            # ------------------------------------------------
            # LW
            # LW R5,0(R4)
            # ------------------------------------------------

            elif operation == "LW":

                if len(parts) != 3:
                    raise ValueError(
                        "LW needs a register and memory address"
                    )

                rt = parts[1]

                address = get_address(
                    registers,
                    parts[2]
                )

                # If address is not present, value is 0
                value = memory.get(address, 0)

                set_register(
                    registers,
                    rt,
                    value
                )

                print(
                    "        Memory Read ->",
                    "Mem[" + str(address) + "] =",
                    value
                )

            # ------------------------------------------------
            # SW
            # SW R3,4(R4)
            # ------------------------------------------------

            elif operation == "SW":

                if len(parts) != 3:
                    raise ValueError(
                        "SW needs a register and memory address"
                    )

                rt = parts[1]

                address = get_address(
                    registers,
                    parts[2]
                )

                value = get_register(
                    registers,
                    rt
                )

                memory[address] = value

                print(
                    "        Memory Write ->",
                    "Mem[" + str(address) + "] =",
                    value
                )

            # ------------------------------------------------
            # BEQ
            # BEQ R1,R2,1
            # ------------------------------------------------

            elif operation == "BEQ":

                if len(parts) != 4:
                    raise ValueError(
                        "BEQ needs 2 registers and an offset"
                    )

                rs = parts[1]
                rt = parts[2]

                try:
                    offset = int(parts[3])
                except ValueError:
                    raise ValueError(
                        "Invalid branch offset"
                    )

                if (
                    get_register(registers, rs)
                    == get_register(registers, rt)
                ):

                    # Branch calculation
                    pc = pc + 4 + (offset * 4)

                    branch_taken = True

            # ------------------------------------------------
            # J
            # J 4
            # ------------------------------------------------

            elif operation == "J":

                if len(parts) != 2:
                    raise ValueError(
                        "J needs a target instruction number"
                    )

                try:
                    target = int(parts[1])
                except ValueError:
                    raise ValueError(
                        "Invalid jump target"
                    )

                if target < 0 or target >= len(instructions):
                    raise ValueError(
                        "Jump target is outside the program"
                    )

                # Target is the instruction index
                pc = target * 4

                jump_taken = True

            # ------------------------------------------------
            # Unknown instruction
            # ------------------------------------------------

            else:

                raise ValueError(
                    "Unknown instruction: " + operation
                )

            # R0 must always remain 0
            registers["R0"] = 0

            # ------------------------------------------------
            # SHOW EXECUTION
            # ------------------------------------------------

            if branch_taken:

                print(
                    "Step", step,
                    "| PC =", old_pc,
                    "|", original_instruction,
                    "| Branch Taken -> PC =", pc
                )

            elif jump_taken:

                print(
                    "Step", step,
                    "| PC =", old_pc,
                    "|", original_instruction,
                    "| Jump -> PC =", pc
                )

            else:

                print(
                    "Step", step,
                    "| PC =", old_pc,
                    "|", original_instruction
                )

            # Normal instruction moves to next instruction
            if not branch_taken and not jump_taken:
                pc = pc + 4

            step = step + 1

        except ValueError as error:

            print("\nERROR")
            print("PC:", old_pc)
            print("Instruction:", original_instruction)
            print("Reason:", error)

            break

    if step > max_steps:

        print(
            "\nProgram stopped after 100 steps."
        )

        print(
            "This is done to prevent an infinite loop."
        )

    print("\n========== EXECUTION FINISHED ==========")


# ============================================================
# MAIN FUNCTION OF PROJECT 1
# ============================================================

def main():

    registers = create_registers()

    memory = create_memory()

    print("\n")
    print("=" * 60)
    print("        MIPS INSTRUCTION EXECUTION SIMULATOR")
    print("                 COA MINI PROJECT 1")
    print("=" * 60)

    # Show initial values
    print("\nInitial Register Values:")

    for i in range(32):

        name = "R" + str(i)

        if registers[name] != 0:
            print(
                name,
                "=",
                registers[name]
            )

    print("\nInitial Memory:")

    display_memory(memory)

    # --------------------------------------------------------
    # Instructions supported
    # --------------------------------------------------------

    print("\nSupported Instructions:")
    print("ADD  Rd,Rs,Rt")
    print("SUB  Rd,Rs,Rt")
    print("AND  Rd,Rs,Rt")
    print("OR   Rd,Rs,Rt")
    print("ADDI Rt,Rs,number")
    print("SLT  Rd,Rs,Rt")
    print("LW   Rt,offset(Rs)")
    print("SW   Rt,offset(Rs)")
    print("BEQ  Rs,Rt,offset")
    print("J    instruction_number")

    print("\nExamples:")
    print("ADD R5,R1,R2")
    print("SUB R6,R2,R1")
    print("ADDI R7,R1,5")
    print("LW R8,0(R4)")
    print("SW R3,4(R4)")
    print("BEQ R1,R2,1")
    print("J 3")

    # --------------------------------------------------------
    # Get number of instructions
    # --------------------------------------------------------

    while True:

        try:

            number = int(
                input("\nHow many instructions? ")
            )

            if number <= 0:

                print(
                    "Enter a number greater than 0."
                )

            else:

                break

        except ValueError:

            print(
                "Please enter a valid number."
            )

    # --------------------------------------------------------
    # Get instructions from user
    # --------------------------------------------------------

    instructions = []

    print("\nEnter the instructions:")

    for i in range(number):

        instruction = input(
            "Instr " + str(i + 1) + ": "
        )

        instructions.append(instruction)

    # --------------------------------------------------------
    # Execute instructions
    # --------------------------------------------------------

    run(
        instructions,
        registers,
        memory
    )

    # --------------------------------------------------------
    # Display final results
    # --------------------------------------------------------

    print("\n")
    print("=" * 60)
    print("             FINAL REGISTER VALUES")
    print("=" * 60)

    display_registers(registers)

    print("\n")
    print("=" * 60)
    print("               FINAL MEMORY")
    print("=" * 60)

    display_memory(memory)


# ============================================================
# RUN PROJECT 1 DIRECTLY
# ============================================================

if __name__ == "__main__":
    main()