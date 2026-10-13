def addition():
    print("\n")
    print("=" * 60)
    print("                 ADDITION")
    print("=" * 60)
    try:
        a = int(input("\nEnter first number: "))
        b = int(input("Enter second number: "))
        result = a + b
        print("\nCalculation:")
        print(a, "+", b, "=", result)
    except ValueError:
        print("\nPlease enter valid numbers.")
def subtraction():
    print("\n")
    print("=" * 60)
    print("                SUBTRACTION")
    print("=" * 60)
    try:
        a = int(input("\nEnter first number: "))
        b = int(input("Enter second number: "))
        result = a - b
        print("\nCalculation:")
        print(a, "-", b, "=", result)
    except ValueError:
        print("\nPlease enter valid numbers.")
def multiplication():
    print("\n")
    print("=" * 60)
    print("              MULTIPLICATION")
    print("=" * 60)
    try:
        a = int(input("\nEnter first positive number: "))
        b = int(input("Enter second positive number: "))
        if a < 0 or b < 0:
            print("\nPlease enter positive numbers.")
            return
        result = 0
        temp_a = a
        temp_b = b
        step = 1
        print("\nBinary Multiplication Steps")
        print("-" * 60)
        while temp_b > 0:
            print(
                "Step", step,
                ": Multiplicand =", temp_a,
                ", Multiplier =", temp_b
            )
            if temp_b % 2 == 1:
                result = result + temp_a
                print(
                    "  Multiplier is odd -> Add multiplicand"
                )
            else:
                print(
                    "  Multiplier is even -> No addition"
                )
            temp_a = temp_a * 2
            temp_b = temp_b // 2
            step = step + 1
        print("\nFinal Result:")
        print(a, "x", b, "=", result)
    except ValueError:
        print("\nPlease enter valid numbers.")
def restoring_division():
    print("\n")
    print("=" * 60)
    print("              RESTORING DIVISION")
    print("=" * 60)
    try:
        dividend = int(
            input("\nEnter dividend: ")
        )
        divisor = int(
            input("Enter divisor: ")
        )
        if dividend < 0 or divisor <= 0:
            print(
                "\nPlease enter a positive dividend "
                "and positive divisor."
            )
            return
        if dividend < divisor:
            print(
                "\nDividend must be greater than "
                "or equal to divisor for this demonstration."
            )
            return
        n = max(
            dividend.bit_length(),
            divisor.bit_length()
        )
        A = 0
        Q = dividend
        M = divisor
        print("\nInitial Values")
        print("A =", A)
        print("Q =", Q)
        print("M =", M)
        print("Number of bits =", n)
        print("\nRestoring Division Steps")
        print("-" * 60)
        for step in range(1, n + 1):
            A = (A << 1) | ((Q >> (n - 1)) & 1)
            Q = (Q << 1) & ((1 << n) - 1)
            A = A - M
            print("\nStep", step)
            print("After shift:")
            print("A =", A)
            print("Q =", Q)
            if A < 0:
                A = A + M
                Q = Q & ~1
                print("A is negative")
                print("Restore A by adding M")
                print("Quotient bit = 0")
            else:
                Q = Q | 1
                print("A is positive")
                print("Quotient bit = 1")
            print("Final A =", A)
            print("Final Q =", Q)
        print("\n" + "-" * 60)
        print("FINAL RESULT")
        print("-" * 60)
        print("Quotient  =", Q)
        print("Remainder =", A)
        print(
            "\nVerification:",
            dividend,
            "=",
            divisor,
            "*",
            Q,
            "+",
            A
        )
    except ValueError:
        print("\nPlease enter valid integers.")
def non_restoring_division():
    print("\n")
    print("=" * 60)
    print("             NON-RESTORING DIVISION")
    print("=" * 60)
    try:
        dividend = int(
            input("\nEnter dividend: ")
        )
        divisor = int(
            input("Enter divisor: ")
        )
        if dividend < 0 or divisor <= 0:
            print(
                "\nPlease enter a positive dividend "
                "and positive divisor."
            )
            return
        if dividend < divisor:
            print(
                "\nDividend must be greater than "
                "or equal to divisor for this demonstration."
            )
            return
        n = max(
            dividend.bit_length(),
            divisor.bit_length()
        )
        A = 0
        Q = dividend
        M = divisor
        print("\nInitial Values")
        print("A =", A)
        print("Q =", Q)
        print("M =", M)
        print("Number of bits =", n)
        print("\nNon-Restoring Division Steps")
        print("-" * 60)
        for step in range(1, n + 1):
            A = (A << 1) | ((Q >> (n - 1)) & 1)
            Q = (Q << 1) & ((1 << n) - 1)
            print("\nStep", step)
            if A >= 0:
                A = A - M
                print(
                    "A was positive/zero -> A = A - M"
                )
            else:
                A = A + M
                print(
                    "A was negative -> A = A + M"
                )
            print("A =", A)
            print("Q =", Q)
            if A >= 0:
                Q = Q | 1
                print(
                    "A is positive -> Quotient bit = 1"
                )
            else:
                Q = Q & ~1
                print(
                    "A is negative -> Quotient bit = 0"
                )
        if A < 0:
            A = A + M
            print(
                "\nFinal correction:"
                "\nA = A + M"
            )
        print("\n" + "-" * 60)
        print("FINAL RESULT")
        print("-" * 60)
        print("Quotient  =", Q)
        print("Remainder =", A)
        print(
            "\nVerification:",
            dividend,
            "=",
            divisor,
            "*",
            Q,
            "+",
            A
        )
    except ValueError:
        print("\nPlease enter valid integers.")
def fixed_point():
    print("\n")
    print("=" * 60)
    print("              FIXED-POINT ARITHMETIC")
    print("=" * 60)
    print(
        "\nFixed-point numbers use a fixed number of "
        "digits after the decimal point."
    )
    try:
        a = float(
            input("\nEnter first number: ")
        )
        b = float(
            input("Enter second number: ")
        )
        decimal_places = int(
            input(
                "Enter number of decimal places: "
            )
        )
        if decimal_places < 0:
            print(
                "\nDecimal places cannot be negative."
            )
            return
        scale = 10 ** decimal_places
        fixed_a = round(a * scale)
        fixed_b = round(b * scale)
        fixed_add = fixed_a + fixed_b
        fixed_sub = fixed_a - fixed_b
        result_add = fixed_add / scale
        result_sub = fixed_sub / scale
        print("\nFixed-Point Representation")
        print("-" * 60)
        print(
            a,
            "->",
            fixed_a,
            "(scaled integer)"
        )
        print(
            b,
            "->",
            fixed_b,
            "(scaled integer)"
        )
        print("\nAddition:")
        print(
            fixed_a,
            "+",
            fixed_b,
            "=",
            fixed_add
        )
        print(
            "Result =",
            result_add
        )
        print("\nSubtraction:")
        print(
            fixed_a,
            "-",
            fixed_b,
            "=",
            fixed_sub
        )
        print(
            "Result =",
            result_sub
        )
    except ValueError:
        print("\nPlease enter valid values.")
def floating_point():
    print("\n")
    print("=" * 60)
    print("             FLOATING-POINT ARITHMETIC")
    print("=" * 60)
    try:
        a = float(
            input("\nEnter first number: ")
        )
        b = float(
            input("Enter second number: ")
        )
        print("\nFloating-Point Representation")
        print("-" * 60)
        print(
            "First number  =",
            a
        )
        print(
            "Second number =",
            b
        )
        print("\nAddition:")
        print(
            a,
            "+",
            b,
            "=",
            a + b
        )
        print("\nSubtraction:")
        print(
            a,
            "-",
            b,
            "=",
            a - b
        )
        print("\nMultiplication:")
        print(
            a,
            "*",
            b,
            "=",
            a * b
        )
        if b != 0:
            print("\nDivision:")
            print(
                a,
                "/",
                b,
                "=",
                a / b
            )
        else:
            print(
                "\nDivision is not possible by zero."
            )
    except ValueError:
        print("\nPlease enter valid numbers.")
def compare_arithmetic():
    print("\n")
    print("=" * 65)
    print("             COMPUTER ARITHMETIC COMPARISON")
    print("=" * 65)
    print(
        "\n1. Addition"
        "\n   Adds two numbers."
    )
    print(
        "\n2. Subtraction"
        "\n   Finds the difference between two numbers."
    )
    print(
        "\n3. Multiplication"
        "\n   Repeated addition using binary operations."
    )
    print(
        "\n4. Restoring Division"
        "\n   Subtract divisor and restore when result is negative."
    )
    print(
        "\n5. Non-Restoring Division"
        "\n   Avoids restoring after every negative result."
    )
    print(
        "\n6. Fixed-Point"
        "\n   Decimal point remains at a fixed position."
    )
    print(
        "\n7. Floating-Point"
        "\n   Uses sign, exponent and mantissa representation."
    )
    print("\n" + "=" * 65)
def main():
    while True:
        print("\n")
        print("=" * 65)
        print("             COMPUTER ARITHMETIC ANALYZER")
        print("                  COA MINI PROJECT 3")
        print("=" * 65)
        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Restoring Division")
        print("5. Non-Restoring Division")
        print("6. Fixed-Point Arithmetic")
        print("7. Floating-Point Arithmetic")
        print("8. Compare Arithmetic Methods")
        print("0. Return to Main Menu")
        print("=" * 65)
        choice = input(
            "\nEnter your choice: "
        ).strip()
        if choice == "1":
            addition()
            input(
                "\nPress ENTER to continue..."
            )
        elif choice == "2":
            subtraction()
            input(
                "\nPress ENTER to continue..."
            )
        elif choice == "3":
            multiplication()
            input(
                "\nPress ENTER to continue..."
            )
        elif choice == "4":
            restoring_division()
            input(
                "\nPress ENTER to continue..."
            )
        elif choice == "5":
            non_restoring_division()
            input(
                "\nPress ENTER to continue..."
            )
        elif choice == "6":
            fixed_point()
            input(
                "\nPress ENTER to continue..."
            )
        elif choice == "7":
            floating_point()
            input(
                "\nPress ENTER to continue..."
            )
        elif choice == "8":
            compare_arithmetic()

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