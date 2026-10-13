# Computer Organization and Architecture — Mini Project

### Learning Computer Architecture Through Python

Hi! I'm a second-year Computer Science Engineering student, and this project is part of my learning journey in Computer Organization and Architecture (COA).

I created this project to understand important computer architecture concepts by implementing them as small Python programs instead of learning everything only through theory.

The project brings together five modules that demonstrate how instructions are executed, how data is accessed, how arithmetic operations work, how instructions move through a processor pipeline, and how cache memory is organized.

## About the Project

Computer Organization and Architecture helps us understand what happens inside a computer when a program runs.

Through this project, I explored these concepts using Python and tried to make them easier to understand through practical examples and program outputs.

## Modules

### 1. MIPS Instruction Execution Simulator

This module demonstrates the basic process of executing MIPS instructions.

**Concepts covered:**
- Registers and Program Counter (PC)
- Memory operations
- Arithmetic and logical instructions
- Branching and jump instructions
- Instruction execution and output tracing

### 2. Addressing Mode Analyzer

This module demonstrates different ways an instruction can access its operands.

**Addressing modes covered:**
- Immediate Addressing
- Register Addressing
- Direct Addressing
- Indirect Addressing
- Base/Displacement Addressing

### 3. Computer Arithmetic Analyzer

This module explores how arithmetic operations can be represented and performed in computer systems.

**Concepts covered:**
- Addition and subtraction
- Multiplication and division
- Restoring and non-restoring division
- Fixed-point arithmetic
- Floating-point arithmetic

### 4. MIPS Pipeline Simulator

This module demonstrates the five stages of a basic MIPS instruction pipeline.

**Pipeline stages:**

`IF → ID → EX → MEM → WB`

- IF — Instruction Fetch
- ID — Instruction Decode
- EX — Execute
- MEM — Memory Access
- WB — Write Back

It also explores pipeline performance concepts such as cycle count, speedup, efficiency, and throughput.

### 5. Cache Mapping Simulator

This module explores how memory blocks are mapped into cache memory.

**Mapping techniques covered:**
- Direct Mapping
- Fully Associative Mapping
- Set-Associative Mapping

It also explores cache concepts such as tags, index, offset, cache hits, cache misses, and performance calculations.

## Technologies Used

- **Programming Language:** Python
- **Editor:** Visual Studio Code
- **Core Concepts:** Computer Organization and Architecture, MIPS Instructions, Computer Arithmetic, Instruction Pipelining, and Cache Memory

## What I Learned

Working on this project helped me connect the concepts I study in COA with practical Python implementations.

Some of the key things I explored were:

- Understanding how instructions use registers and memory.
- Learning how different addressing modes work.
- Exploring arithmetic operations and number representation.
- Understanding the stages involved in instruction pipelining.
- Comparing different cache mapping techniques.
- Organizing a project into separate Python modules.

This project also gave me an opportunity to practise writing Python code and breaking a large subject into smaller, manageable programs.

## Project Structure

```text
COA-Mini-Project/
│
├── main.py
├── Project 1 - MIPS Instruction Simulator
├── Project 2 - Addressing Mode Analyzer
├── Project 3 - Computer Arithmetic Analyzer
├── Project 4 - MIPS Pipeline Simulator
└── Project 5 - Cache Mapping Simulator
```

*Note: The module names above describe the project structure. Refer to the actual filenames in the repository.*

## How to Run

1. Clone or download this repository.
2. Make sure Python is installed on your computer.
3. Open the project folder in Visual Studio Code.
4. Run `main.py` from the terminal:

```bash
python main.py
```

5. Follow the instructions displayed by the program.

The exact steps may depend on your local Python setup.

## Future Improvements

I would like to improve this project further by adding more instruction examples, improving the output presentation, and exploring additional computer architecture concepts.

## A Note

This is a student mini project developed as part of my learning journey in Computer Science Engineering.

I'm sharing it to document what I've learned, practise implementing theoretical concepts, and continue improving my programming skills.

Suggestions and feedback are always welcome!

---

**Thank you for visiting my project!**
