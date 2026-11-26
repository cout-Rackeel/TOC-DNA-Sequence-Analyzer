# DNA Sequence Pattern Analyzer
# DFA Implementation
#Shemar Campbell
#211864
#Theory of Computation

# 1. DFA Transition Table
transitions = {
    'q0': {'A': 'q1', 'C': 'q4', 'G': 'q4', 'T': 'q4'},

    'q1': {'A': 'q4', 'C': 'q4', 'G': 'q4', 'T': 'q2'},

    'q2': {'A': 'q4', 'C': 'q4', 'G': '{q3,q5}', 'T': 'q4'},

    '{q3,q5}': {'A': 'q6', 'C': '{q4,q8}', 'G': 'q8', 'T': 'q8'},

    'q4': {'A': 'q4', 'C': 'q4', 'G': 'q4', 'T': 'q4'},

    '{q4,q8}': {'A': '{q4,q8}', 'C': '{q4,q8}',
                'G': '{q4,q8}', 'T': '{q4,q8}'},

    'q8': {'A': 'q8', 'C': 'q8', 'G': 'q8', 'T': 'q8'},

    'q6': {'A': 'q8', 'C': 'q8', 'G': 'q8',
           'T': '{q7,q9,q14,q19}'},

    '{q7,q9,q14,q19}': {
        'A': 'q6',
        'C': '{q13,q18,q23}',
        'G': '{q13,q18,q23}',
        'T': '{q10,q15,q20}'
    },

    '{q13,q18,q23}': {
        'A': '{q13,q18,q23}',
        'C': '{q13,q18,q23}',
        'G': '{q13,q18,q23}',
        'T': '{q13,q18,q23}'
    },

    '{q10,q15,q20}': {
        'A': '{q11,q16,q23}',
        'C': '{q13,q18,q23}',
        'G': '{q13,q18,q21}',
        'T': '{q13,q18,q23}'
    },

    '{q11,q16,q23}': {
        'A': '{q12,q18,q23}',
        'C': '{q13,q18,q23}',
        'G': '{q13,q17,q23}',
        'T': '{q13,q18,q23}'
    },

    '{q13,q18,q21}': {
        'A': '{q13,q18,q22}',
        'C': '{q13,q18,q23}',
        'G': '{q13,q18,q23}',
        'T': '{q13,q18,q23}'
    },

    '{q12,q18,q23}': {
        'A': '{q13,q18,q23}',
        'C': '{q13,q18,q23}',
        'G': '{q13,q18,q23}',
        'T': '{q13,q18,q23}'
    },

    '{q13,q17,q23}': {
        'A': '{q13,q18,q23}',
        'C': '{q13,q18,q23}',
        'G': '{q13,q18,q23}',
        'T': '{q13,q18,q23}'
    },

    '{q13,q18,q22}': {
        'A': '{q13,q18,q23}',
        'C': '{q13,q18,q23}',
        'G': '{q13,q18,q23}',
        'T': '{q13,q18,q23}'
    }
}

# 2. Initial and Final States
initial_state = 'q0'

final_states = {
    '{q12,q18,q23}',
    '{q13,q17,q23}',
    '{q13,q18,q22}'
}

# 3. Function to Process the DNA Sequence
def run_dfa(input_string, transitions, initial_state, final_states):
    current_state = initial_state

    for symbol in input_string.upper():

        if symbol not in transitions[current_state]:
            return False

        current_state = transitions[current_state][symbol]

    return current_state in final_states

# 4. Function that Display State Transitions
def trace_dfa(input_string, transitions, initial_state, final_states):
    current_state = initial_state

    print("\nStarting State:", current_state)

    for symbol in input_string.upper():

        if symbol not in transitions[current_state]:
            print("Invalid input symbol:", symbol)
            return

        next_state = transitions[current_state][symbol]

        print(current_state, "--", symbol, "-->", next_state)

        current_state = next_state

    print("\nFinal State:", current_state)

    if current_state in final_states:
        print("DNA Sequence Accepted")
    else:
        print("DNA Sequence Rejected")

# 5. Get the DNA Sequence from User

if __name__ == "__main__":
    dna_sequence = input("Enter DNA sequence (A, C, G, T): ")

    trace_dfa(
        dna_sequence,
        transitions,
        initial_state,
        final_states
    )
