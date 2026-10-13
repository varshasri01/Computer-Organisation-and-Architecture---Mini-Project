def get_instructions():
    """
    Get MIPS instructions from the user.
    """

    instructions = []

    print("\nEnter MIPS instructions one by one.")
    print("Type 'done' when you have finished.")

    while True:

        instruction = input("Enter instruction: ").strip()

        if instruction.lower() == "done":
            break

        if instruction == "":
            print("Please enter a valid instruction.")
            continue

        instructions.append(instruction)

    return instructions


def create_pipeline(instructions):
    """
    Create the 5-stage pipeline table.
    """

    stages = ["IF", "ID", "EX", "MEM", "WB"]

    number_of_instructions = len(instructions)

    # For a 5-stage pipeline:
    # Total cycles = Number of instructions + 4
    total_cycles = number_of_instructions + 4

    pipeline = []

    for i in range(number_of_instructions):

        row = []

        for cycle in range(total_cycles):

            stage_number = cycle - i

            if 0 <= stage_number < 5:
                row.append(stages[stage_number])
            else:
                row.append("")

        pipeline.append(row)

    return pipeline, total_cycles


def display_pipeline(instructions, pipeline, total_cycles):
    """
    Display the pipeline execution table.
    """

    print("\n")
    print("=" * 80)
    print("                 5-STAGE MIPS PIPELINE")
    print("=" * 80)

    print(f"{'Instruction':<20}", end="")

    for cycle in range(1, total_cycles + 1):
        print(f"{'C' + str(cycle):<8}", end="")

    print()

    print("-" * (20 + total_cycles * 8))

    for i in range(len(instructions)):

        print(f"{instructions[i]:<20}", end="")

        for stage in pipeline[i]:
            print(f"{stage:<8}", end="")

        print()

    print()


def calculate_performance(number_of_instructions, total_cycles):
    """
    Calculate pipeline performance.
    """

    # Without pipelining, every instruction
    # needs all 5 stages.

    non_pipeline_cycles = number_of_instructions * 5

    # Speedup
    speedup = non_pipeline_cycles / total_cycles

    # Pipeline efficiency
    total_work = number_of_instructions * 5
    total_available = total_cycles * 5

    efficiency = (total_work / total_available) * 100

    # Throughput
    throughput = number_of_instructions / total_cycles

    return (
        non_pipeline_cycles,
        speedup,
        efficiency,
        throughput
    )


def display_performance(
    number_of_instructions,
    total_cycles,
    non_pipeline_cycles,
    speedup,
    efficiency,
    throughput
):
    """
    Display calculated performance values.
    """

    print("=" * 60)
    print("              PIPELINE PERFORMANCE")
    print("=" * 60)

    print(f"Number of Instructions : {number_of_instructions}")
    print(f"Non-Pipeline Cycles   : {non_pipeline_cycles}")
    print(f"Pipeline Cycles       : {total_cycles}")

    print(f"Pipeline Speedup      : {speedup:.2f} times")
    print(f"Pipeline Efficiency   : {efficiency:.2f}%")
    print(f"Throughput            : {throughput:.4f} instructions/cycle")

    print("=" * 60)


def run_project4():
    """
    Main function of Project 4.
    This function is called from main.py.
    """

    print("\n")
    print("=" * 60)
    print("          PROJECT 4 - MIPS PIPELINE SIMULATOR")
    print("=" * 60)

    print("\nPipeline Stages:")
    print("IF  -> Instruction Fetch")
    print("ID  -> Instruction Decode")
    print("EX  -> Execute")
    print("MEM -> Memory Access")
    print("WB  -> Write Back")

    instructions = get_instructions()

    if len(instructions) == 0:

        print("\nNo instructions were entered.")
        return

    pipeline, total_cycles = create_pipeline(instructions)

    display_pipeline(
        instructions,
        pipeline,
        total_cycles
    )

    (
        non_pipeline_cycles,
        speedup,
        efficiency,
        throughput
    ) = calculate_performance(
        len(instructions),
        total_cycles
    )

    display_performance(
        len(instructions),
        total_cycles,
        non_pipeline_cycles,
        speedup,
        efficiency,
        throughput
    )

    print("\nProject 4 simulation completed successfully.")