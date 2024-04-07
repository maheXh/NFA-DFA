### NFA to DFA Converter

![NFA and DFA](https://github.com/maheXh/NFA-DFA/assets/122071980/b4b4cf3b-655d-44cd-b051-69ebeaa11bd1)

This Python script converts a Non-Deterministic Finite Automaton (NFA) to a Deterministic Finite Automaton (DFA) using the powerset construction method. It also provides visual representations of both the NFA and DFA using Graphviz.

---

## Contributer:
| Name                | Roll Number    | GitHub Profile                                   |
|---------------------|----------------|--------------------------------------------------|
| B Mahesh Raj        | CB.EN.U4CSE22006 | [Mahesh](https://github.com/maheXh)             |
| Amit Kumar          | CB.EN.U4CSE22002 | [Amit](https://github.com/Arch-AMIt)       |
| Ananth Madhusoodanan| CB.EN.U4CSE22061 | [Ananth](https://github.com/ananthmadhusoodanan) |
| Hariharan A.s       | CB.EN.U4CSE22017 | [Hariharan](https://github.com/Harihar1269)   |
| Daniyal Ahmad       | CB.EN.U4CSE22012 | [Daniyal](https://github.com/Daniyalahmad07) |

**Your Role: Amit Kumar**

## Table of Contents

1. [Working Principles](#working-principles)
2. [How to Run](#how-to-run)
3. [Dependencies](#dependencies)
4. [Example Usage](#example-usage)
5. [Contributing](#contributing)
6. [License](#license)

---

## Working Principles

### 1. Input
- The script prompts the user to input the necessary information about the NFA:
  - Total number of states.
  - Total number of transitions.
  - For each state and transition:
    - State name.
    - Transition symbol (path).
    - End state(s) reached from the current state via the transition.

### 2. Conversion to DFA
- The script constructs a DFA from the given NFA using the powerset construction method.
- It initializes empty dictionaries and lists to store DFA transitions and states.
- It iterates over each state in the NFA and computes the transitions for the DFA.
- New states are created in the DFA as needed.
- Final states of the DFA are determined based on the final states of the NFA.

### 3. Visualization
- The script utilizes Graphviz to visualize the NFA and DFA as state transition diagrams.
- It combines the NFA and DFA into a single automaton and generates a visualization.

---

## How to Run

1. Clone the repository to your local machine:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd <project-directory>
   ```

3. Install the required Python dependencies:
   ```
   pip install pandas graphviz
   ```

4. Run the script:
   ```
   python nfa_to_dfa_converter.py
   ```

5. Follow the on-screen prompts to input the NFA details.

6. Once the conversion is complete, the DFA transitions, final states, and visualization will be displayed.

---

## Dependencies

- **pandas:** pandas is used for creating and manipulating DataFrames to represent NFA and DFA transitions. It provides easy-to-use data structures and data analysis tools.
  
  ```bash
  pip install pandas
  ```

- **graphviz:** graphviz is used for visualizing the state transition diagrams of the NFA and DFA. It provides a simple interface for generating graph visualizations.
  
  ```bash
  pip install graphviz
  ```

---

