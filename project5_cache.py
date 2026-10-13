def get_cache_details():
    """
    Get cache and memory information from the user.
    """

    print("\nEnter Cache and Memory Details")
    print("--------------------------------")

    memory_size = int(input("Main memory size (in bytes): "))
    cache_size = int(input("Cache size (in bytes): "))
    block_size = int(input("Block size (in bytes): "))

    if memory_size <= 0 or cache_size <= 0 or block_size <= 0:
        print("\nValues must be greater than zero.")
        return None

    if memory_size % block_size != 0:
        print("\nMemory size must be divisible by block size.")
        return None

    if cache_size % block_size != 0:
        print("\nCache size must be divisible by block size.")
        return None

    if cache_size > memory_size:
        print("\nCache size cannot be greater than memory size.")
        return None

    return memory_size, cache_size, block_size


def calculate_bits(memory_size, cache_size, block_size):
    """
    Calculate address, tag, index and offset bits.
    """

    memory_blocks = memory_size // block_size
    cache_lines = cache_size // block_size

    offset_bits = (block_size.bit_length() - 1)

    index_bits = 0

    if cache_lines > 1:
        index_bits = (cache_lines.bit_length() - 1)

    address_bits = (memory_size.bit_length() - 1)

    tag_bits = address_bits - index_bits - offset_bits

    return (
        memory_blocks,
        cache_lines,
        address_bits,
        tag_bits,
        index_bits,
        offset_bits
    )


def direct_mapping(address, block_size, cache_lines):
    """
    Direct Mapping

    Cache line = Memory block number % Number of cache lines
    """

    block_number = address // block_size

    offset = address % block_size

    cache_line = block_number % cache_lines

    index = cache_line

    tag = block_number // cache_lines

    return tag, index, offset, cache_line


def fully_associative_mapping(address, block_size, cache_lines):
    """
    Fully Associative Mapping

    Any memory block can be placed in any cache line.

    For this simulator, an empty cache line is selected first.
    """

    block_number = address // block_size

    offset = address % block_size

    tag = block_number

    index = None

    return tag, index, offset, block_number


def set_associative_mapping(
    address,
    block_size,
    cache_lines,
    associativity
):
    """
    Set-Associative Mapping

    Cache is divided into sets.

    Each set contains multiple cache lines.
    """

    block_number = address // block_size

    offset = address % block_size

    number_of_sets = cache_lines // associativity

    set_number = block_number % number_of_sets

    tag = block_number // number_of_sets

    return tag, set_number, offset, set_number


def print_address_information(
    address,
    tag,
    index,
    offset,
    location
):
    """
    Display address breakdown.
    """

    print("\nAddress Analysis")
    print("----------------")

    print("CPU Address :", address)

    print("Tag         :", tag)

    if index is None:
        print("Index       : N/A")
    else:
        print("Index       :", index)

    print("Offset      :", offset)

    print("Cache Location :", location)


def simulate_accesses(
    addresses,
    mapping_type,
    memory_size,
    cache_size,
    block_size,
    associativity=1
):
    """
    Simulate multiple memory accesses.
    """

    cache_lines = cache_size // block_size

    cache = [None] * cache_lines

    hits = 0
    misses = 0

    print("\n")
    print("=" * 70)
    print("CACHE ACCESS SIMULATION")
    print("=" * 70)

    for address in addresses:

        if address < 0 or address >= memory_size:

            print("\nAddress:", address)
            print("Invalid memory address.")
            continue

        if mapping_type == "Direct":

            tag, index, offset, location = direct_mapping(
                address,
                block_size,
                cache_lines
            )

            cache_index = location

        elif mapping_type == "Fully Associative":

            tag, index, offset, location = fully_associative_mapping(
                address,
                block_size,
                cache_lines
            )

            cache_index = None

        else:

            tag, index, offset, location = set_associative_mapping(
                address,
                block_size,
                cache_lines,
                associativity
            )

            cache_index = None

        # ----------------------------------------
        # Direct Mapping
        # ----------------------------------------

        if mapping_type == "Direct":

            if cache[cache_index] == tag:

                result = "HIT"
                hits += 1

            else:

                result = "MISS"
                misses += 1

                cache[cache_index] = tag

        # ----------------------------------------
        # Fully Associative
        # ----------------------------------------

        elif mapping_type == "Fully Associative":

            if tag in cache:

                result = "HIT"
                hits += 1

            else:

                result = "MISS"
                misses += 1

                # Find an empty cache line
                if None in cache:

                    empty_index = cache.index(None)
                    cache[empty_index] = tag

                else:

                    # Simple FIFO-style replacement
                    cache.pop(0)
                    cache.append(tag)

        # ----------------------------------------
        # Set Associative
        # ----------------------------------------

        else:

            number_of_sets = cache_lines // associativity

            start = location * associativity

            end = start + associativity

            set_contents = cache[start:end]

            if tag in set_contents:

                result = "HIT"
                hits += 1

            else:

                result = "MISS"
                misses += 1

                if None in set_contents:

                    empty_position = set_contents.index(None)

                    cache[start + empty_position] = tag

                else:

                    # Simple replacement
                    cache[start] = tag

        print("\nCPU Address:", address)

        print("Tag        :", tag)

        if index is None:
            print("Index      : N/A")
        else:
            print("Index      :", index)

        print("Offset     :", offset)

        print("Cache Location:", location)

        print("Result     :", result)

    return hits, misses


def display_performance(hits, misses):
    """
    Display cache performance.
    """

    total_accesses = hits + misses

    if total_accesses == 0:

        print("\nNo valid cache accesses.")
        return

    hit_ratio = hits / total_accesses

    miss_ratio = misses / total_accesses

    # Example access times
    cache_access_time = 1
    main_memory_time = 10

    average_memory_access_time = (
        cache_access_time
        + miss_ratio * main_memory_time
    )

    print("\n")
    print("=" * 60)
    print("              CACHE PERFORMANCE")
    print("=" * 60)

    print("Number of Cache Accesses :", total_accesses)

    print("Number of Hits           :", hits)

    print("Number of Misses         :", misses)

    print(f"Hit Ratio                : {hit_ratio:.2f}")

    print(f"Hit Ratio (%)            : {hit_ratio * 100:.2f}%")

    print(f"Miss Ratio               : {miss_ratio:.2f}")

    print(f"Miss Ratio (%)           : {miss_ratio * 100:.2f}%")

    print(
        f"Average Memory Access Time : "
        f"{average_memory_access_time:.2f}"
    )

    print("=" * 60)


def run_project5():
    """
    Main function for Project 5.

    This function is called from main.py.
    """

    print("\n")
    print("=" * 60)
    print("             PROJECT 5")
    print("          CACHE MAPPING SIMULATOR")
    print("=" * 60)

    details = get_cache_details()

    if details is None:
        return

    (
        memory_size,
        cache_size,
        block_size
    ) = details

    (
        memory_blocks,
        cache_lines,
        address_bits,
        tag_bits,
        index_bits,
        offset_bits
    ) = calculate_bits(
        memory_size,
        cache_size,
        block_size
    )

    print("\nCache Information")
    print("-----------------")

    print("Memory Blocks :", memory_blocks)
    print("Cache Lines   :", cache_lines)

    print("Address Bits  :", address_bits)
    print("Tag Bits      :", tag_bits)
    print("Index Bits    :", index_bits)
    print("Offset Bits   :", offset_bits)

    print("\nSelect Cache Mapping Technique")

    print("1. Direct Mapping")
    print("2. Fully Associative Mapping")
    print("3. Set-Associative Mapping")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        mapping_type = "Direct"

        associativity = 1

    elif choice == "2":

        mapping_type = "Fully Associative"

        associativity = cache_lines

    elif choice == "3":

        mapping_type = "Set-Associative"

        print("\nAvailable Associativity:")

        print("1. 2-way")
        print("2. 4-way")

        set_choice = input("Enter choice: ")

        if set_choice == "1":

            associativity = 2

        elif set_choice == "2":

            associativity = 4

        else:

            print("Invalid associativity choice.")

            return

        if cache_lines % associativity != 0:

            print(
                "\nAssociativity must divide "
                "the number of cache lines."
            )

            return

    else:

        print("\nInvalid mapping choice.")

        return

    print("\nEnter CPU memory addresses.")

    print("Type 'done' when finished.")

    addresses = []

    while True:

        value = input("CPU Address: ").strip()

        if value.lower() == "done":
            break

        try:

            address = int(value)

            addresses.append(address)

        except ValueError:

            print("Please enter a valid integer address.")

    if len(addresses) == 0:

        print("\nNo addresses were entered.")

        return

    hits, misses = simulate_accesses(
        addresses,
        mapping_type,
        memory_size,
        cache_size,
        block_size,
        associativity
    )

    display_performance(
        hits,
        misses
    )

    print("\nProject 5 simulation completed successfully.")


# --------------------------------------------
# Program entry point
# --------------------------------------------

if __name__ == "__main__":
    run_project5()