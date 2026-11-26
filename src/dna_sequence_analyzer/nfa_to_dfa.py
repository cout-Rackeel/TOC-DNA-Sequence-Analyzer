
# NFA to DFA Conversion CODE
# Power Set Construction
# Shemar Campbell
# 211864
# Theory of Computation

# 1. Original NFA Transition Table

nfa_transitions = {

    'q0': {'A': {'q1'}, 'C': {'q4'}, 'G': {'q4'}, 'T': {'q4'}, 'E': set()},
    'q1': {'A': {'q4'}, 'C': {'q4'}, 'G': {'q4'}, 'T': {'q2'}, 'E': set()},
    'q2': {'A': {'q4'}, 'C': {'q4'}, 'G': {'q3'}, 'T': {'q4'}, 'E': set()},
    'q3': {'A': set(), 'C': {'q4'}, 'G': set(), 'T': set(), 'E': {'q5'}},
    'q4': {'A': {'q4'}, 'C': {'q4'}, 'G': {'q4'}, 'T': {'q4'}, 'E': set()},
    'q5': {'A': {'q6'}, 'C': {'q8'}, 'G': {'q8'}, 'T': {'q8'}, 'E': set()},
    'q6': {'A': {'q8'}, 'C': {'q8'}, 'G': {'q8'}, 'T': {'q7'}, 'E': set()},
    'q7': {'A': {'q6'}, 'C': set(), 'G': set(), 'T': set(), 'E': {'q9', 'q14', 'q19'}},
    'q8': {'A': {'q8'}, 'C': {'q8'}, 'G': {'q8'}, 'T': {'q8'}, 'E': set()},
    'q9': {'A': {'q13'}, 'C': {'q13'}, 'G': {'q13'}, 'T': {'q10'}, 'E': set()},
    'q10': {'A': {'q11'}, 'C': {'q13'}, 'G': {'q13'}, 'T': {'q13'}, 'E': set()},
    'q11': {'A': {'q12'}, 'C': {'q13'}, 'G': {'q13'}, 'T': {'q13'}, 'E': set()},
    'q12': {'A': {'q13'}, 'C': {'q13'}, 'G': {'q13'}, 'T': {'q13'}, 'E': set()},
    'q13': {'A': {'q13'}, 'C': {'q13'}, 'G': {'q13'}, 'T': {'q13'}, 'E': set()},
    'q14': {'A': {'q18'}, 'C': {'q18'}, 'G': {'q18'}, 'T': {'q15'}, 'E': set()},
    'q15': {'A': {'q16'}, 'C': {'q18'}, 'G': {'q18'}, 'T': {'q18'}, 'E': set()},
    'q16': {'A': {'q18'}, 'C': {'q18'}, 'G': {'q17'}, 'T': {'q18'}, 'E': set()},
    'q17': {'A': {'q18'}, 'C': {'q18'}, 'G': {'q18'}, 'T': {'q18'}, 'E': set()},
    'q18': {'A': {'q18'}, 'C': {'q18'}, 'G': {'q18'}, 'T': {'q18'}, 'E': set()},
    'q19': {'A': {'q23'}, 'C': {'q23'}, 'G': {'q23'}, 'T': {'q20'}, 'E': set()},
    'q20': {'A': {'q23'}, 'C': {'q23'}, 'G': {'q21'}, 'T': {'q23'}, 'E': set()},
    'q21': {'A': {'q22'}, 'C': {'q23'}, 'G': {'q23'}, 'T': {'q23'}, 'E': set()},
    'q22': {'A': {'q23'}, 'C': {'q23'}, 'G': {'q23'}, 'T': {'q23'}, 'E': set()},
    'q23': {'A': {'q23'}, 'C': {'q23'}, 'G': {'q23'}, 'T': {'q23'}, 'E': set()}
}

# 2. Initial and Final States

initial_state = 'q0'

final_states = {'q12', 'q17', 'q22'}

alphabet = ['A', 'C', 'G', 'T']

# 3. Function to Find Epsilon Closure

def epsilon_closure(states, nfa):

    closure = set(states)
    pending = list(states)

    while pending:

        state = pending.pop()

        for next_state in nfa[state]['E']:

            if next_state not in closure:
                closure.add(next_state)
                pending.append(next_state)

    return frozenset(closure)

# 4. Function to Find the Next States

def get_next_states(states, symbol, nfa):

    next_states = set()

    for state in states:

        if symbol == 'A':
            next_states.update(nfa[state]['A'])

        elif symbol == 'C':
            next_states.update(nfa[state]['C'])

        elif symbol == 'G':
            next_states.update(nfa[state]['G'])

        elif symbol == 'T':
            next_states.update(nfa[state]['T'])

    return next_states

# 5. Power Set Construction

def convert_nfa_to_dfa(nfa, initial, final):

    start_state = epsilon_closure({initial}, nfa)

    unprocessed_states = [start_state]
    dfa_states = [start_state]
    dfa_transitions = {}

    while unprocessed_states:

        current_state = unprocessed_states.pop(0)

        dfa_transitions[current_state] = {}

        for symbol in alphabet:

            next_states = get_next_states(
                current_state, symbol, nfa
            )

            next_dfa_state = epsilon_closure(next_states, nfa)

            dfa_transitions[current_state][symbol] = next_dfa_state

            if next_dfa_state not in dfa_states:

                dfa_states.append(next_dfa_state)
                unprocessed_states.append(next_dfa_state)

    # Identify the final states of the DFA

    dfa_final_states = set()

    for state in dfa_states:

        if any(nfa_state in final for nfa_state in state):
            dfa_final_states.add(state)

    return dfa_transitions, start_state, dfa_final_states

# 6. Convert NFA into DFA

if __name__ == "__main__":
    dfa_transitions, dfa_initial_state, dfa_final_states = (
        convert_nfa_to_dfa(
            nfa_transitions,
            initial_state,
            final_states
        )
    )

    # 7. Display DFA States

    def display_state(state):

        if not state:
            return '{}'

        ordered_states = sorted(state, key=lambda x: int(x[1:]))

        return '{' + ','.join(ordered_states) + '}'

    # 8. Display the DFA Transition Table

    print("\nEQUIVALENT DFA TRANSITION TABLE")

    print("\nInitial State:", display_state(dfa_initial_state))

    print("\nFinal States:")

    for state in dfa_final_states:
        print(display_state(state))

    print("\nState\t\tA\t\tC\t\tG\t\tT")

    for state, transitions in dfa_transitions.items():

        print(
            display_state(state), "\t",
            display_state(transitions['A']), "\t",
            display_state(transitions['C']), "\t",
            display_state(transitions['G']), "\t",
            display_state(transitions['T'])
        )
