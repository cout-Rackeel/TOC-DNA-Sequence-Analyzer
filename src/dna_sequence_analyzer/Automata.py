# A DFA is formally defined as a 5-tuple (Q, Σ, δ, q0, F) where:
#  - Q, Σ, δ, q0, F

def start_codeon_transition_func(states , inputs, is_concatenating = False):
    transition_table :  dict[tuple[str, str], str] = {}
    trap_state = states[4] # States[4] will always be our trap state
    for state_idx , state in enumerate(states):
        for input_idx , input in enumerate(inputs):
            if state_idx == 0: 
                if input == "a" : 
                    transition_table[(state,input)] = states[1]
                elif is_concatenating == True and input == "ε" :
                    transition_table[(state,input)] = None
                else:
                    transition_table[(state,input)] = trap_state

            if state_idx == 1: 
                if input == "t" : 
                    transition_table[(state,input)] = states[2]
                elif is_concatenating == True and input == "ε" :
                    transition_table[(state,input)] = None
                else:
                    transition_table[(state,input)] = trap_state

            if state_idx == 2: 
                if input == "g" : 
                    transition_table[(state,input)] = states[3]
                elif is_concatenating == True and input == "ε" :
                    transition_table[(state,input)] = None
                else:
                    transition_table[(state,input)] = trap_state

            if state_idx == 3 or state_idx == 4:
                if is_concatenating and input == "ε" :
                    transition_table[(state,input)] = None
                else: 
                    transition_table[(state,input)] = trap_state 
         
    return transition_table     

def middle_motif_transition_func(states , inputs, is_concatenating = False):
    transition_table :  dict[tuple[str, str], str] = {}
    trap_state = states[3] # States[4] will always be our trap state
    
    for state_idx , state in enumerate(states):
        for input_idx , input in enumerate(inputs):
            if state_idx == 0: 
                if input == "a" : 
                    transition_table[(state,input)] = states[1]
                elif is_concatenating == True and input == "ε" :
                    transition_table[(state,input)] = None
                else:
                    transition_table[(state,input)] = trap_state

            if state_idx == 1: 
                if input == "t" : 
                    transition_table[(state,input)] = states[2]
                elif is_concatenating == True and input == "ε" :
                    transition_table[(state,input)] = None
                else:
                    transition_table[(state,input)] = trap_state

            if state_idx == 2: 
                if input == "a" : 
                    transition_table[(state,input)] = states[1]
                elif is_concatenating == True and input == "ε" :
                    transition_table[(state,input)] = None
                else:
                    transition_table[(state,input)] = trap_state

            if state_idx == 3: 
                if is_concatenating == True and input == "ε" :
                    transition_table[(state,input)] = None
                else:
                    transition_table[(state,input)] = trap_state 
         
    return transition_table 

def taa_stop_codeon_transition_func(states , inputs, is_concatenating = False):
    transition_table :  dict[tuple[str, str], str] = {}
    trap_state = states[4] # States[4] will always be our trap state
    
    for state_idx , state in enumerate(states):
        for input_idx , input in enumerate(inputs):
            if state_idx == 0: 
                if input == "t" : 
                    transition_table[(state,input)] = states[1]
                elif is_concatenating == True and input == "ε" :
                    transition_table[(state,input)] = None
                else:
                    transition_table[(state,input)] = trap_state

            if state_idx == 1: 
                if input == "a" : 
                    transition_table[(state,input)] = states[2]
                elif is_concatenating == True and input == "ε" :
                    transition_table[(state,input)] = None
                else:
                    transition_table[(state,input)] = trap_state

            if state_idx == 2: 
                if input == "a" : 
                    transition_table[(state,input)] = states[3]
                elif is_concatenating == True and input == "ε" :
                    transition_table[(state,input)] = None
                else:
                    transition_table[(state,input)] = trap_state

            if state_idx == 3 or state_idx == 4: 
                if is_concatenating == True and input == "ε" :
                    transition_table[(state,input)] = None
                else:
                    transition_table[(state,input)] = trap_state 
         
    return transition_table

def tag_stop_codeon_transition_func(states , inputs, is_concatenating = False):
    transition_table :  dict[tuple[str, str], str] = {}
    trap_state = states[4] # States[4] will always be our trap state
    
    for state_idx , state in enumerate(states):
        for input_idx , input in enumerate(inputs):
            if state_idx == 0: 
                if input == "t" : 
                    transition_table[(state,input)] = states[1]
                elif is_concatenating == True and input == "ε" :
                    transition_table[(state,input)] = None
                else:
                    transition_table[(state,input)] = trap_state

            if state_idx == 1: 
                if input == "a" : 
                    transition_table[(state,input)] = states[2]
                elif is_concatenating == True and input == "ε" :
                    transition_table[(state,input)] = None
                else:
                    transition_table[(state,input)] = trap_state

            if state_idx == 2: 
                if input == "g" : 
                    transition_table[(state,input)] = states[3]
                elif is_concatenating == True and input == "ε" :
                    transition_table[(state,input)] = None
                else:
                    transition_table[(state,input)] = trap_state

            if state_idx == 3 or state_idx == 4: 
                if is_concatenating == True and input == "ε" :
                    transition_table[(state,input)] = None
                else:
                    transition_table[(state,input)] = trap_state 
         
    return transition_table 

def tga_stop_codeon_transition_func(states , inputs, is_concatenating = False):
    transition_table :  dict[tuple[str, str], str] = {}
    trap_state = states[4] # States[4] will always be our trap state
    
    for state_idx , state in enumerate(states):
        for input_idx , input in enumerate(inputs):
            if state_idx == 0: 
                if input == "t" : 
                    transition_table[(state,input)] = states[1]
                elif is_concatenating == True and input == "ε" :
                    transition_table[(state,input)] = None
                else:
                    transition_table[(state,input)] = trap_state

            if state_idx == 1: 
                if input == "g" : 
                    transition_table[(state,input)] = states[2]
                elif is_concatenating == True and input == "ε" :
                    transition_table[(state,input)] = None
                else:
                    transition_table[(state,input)] = trap_state

            if state_idx == 2: 
                if input == "a" : 
                    transition_table[(state,input)] = states[3]
                elif is_concatenating == True and input == "ε" :
                    transition_table[(state,input)] = None
                else:
                    transition_table[(state,input)] = trap_state

            if state_idx == 3 or state_idx == 4: 
                if is_concatenating == True and input == "ε" :
                    transition_table[(state,input)] = None
                else:
                    transition_table[(state,input)] = trap_state 
         
    return transition_table 

class DFA:
    def __init__(self, states, alphabet, transition_func, initial_state, final_states : tuple[str]):
        self.states = states 
        self.alphabet = alphabet
        self.transition_func = transition_func
        self.initial_state = initial_state
        self.final_states = final_states

    def generateTransitionTable(self):
        return self.transition_func(self.states , self.alphabet)

    def print_transition_table(self):
        for state in self.states:
            for input in self.alphabet:
                print(f"{state}, {input} --> {self.generateTransitionTable()[(state,input)]} \n")

    def test_if_string_is_vaild(self, input_str):
        current_state = self.initial_state
        transition_table = self.generateTransitionTable()
        validator = None
        for index,letter in enumerate(input_str):
            print(f"Input : {letter} on State: {current_state} leads to {transition_table[(current_state,letter)]}")
            current_state = transition_table[(current_state,letter)]

            # If you know your trap states beforehand this is more efficient way to check if a string is not in the language
            # if current_state == self.states[4]:
            #     print("String is rejected")
            #     return

            if index == (len(input_str) - 1):
                if (current_state in self.final_states):
                    print("String is accepted")
                else:
                    print("String is rejected")

class NFA(DFA):
    def generateTransitionTable(self):
        return self.transition_func
    
    def test_if_string_is_vaild(self, input_str):
        current_state = self.initial_state
        transition_table = self.generateTransitionTable()
        validator = None

        for index,letter in enumerate(input_str):

            if current_state == self.states[3]:
                if letter != "c":
                    print(f"ε-transition on State: {current_state} leads to {self.states[5]}") 
                    current_state = transition_table[(current_state,"ε")]

            if current_state == self.states[7]:
                letter_index = index
                if letter != "c" and letter != "a":
                    raw_potential_states = transition_table[(current_state,"ε")]
                    potential_states = raw_potential_states.split("|")
                    base_state = current_state

                    for state in potential_states:
                        print(f"ε-transition on State: {base_state} leads to {state}") 
                        current_state = state
                        index = letter_index

                        while index < (len(input_str)):
                            print(f"Input : {input_str[index]} on State: {current_state} leads to {transition_table[(current_state,input_str[index])]}") 
                            current_state = transition_table[(current_state,input_str[index])]
                            index += 1
                            

                        if index == (len(input_str)):
                            if (current_state in self.final_states):
                                validator = True
                                print("\n***** DNA Sequence is valid *****") 
                                return
                            else:
                                validator = False
                                print("Not valid on this path")


                    # return
                    
                    
                
            print(f"Input : {letter} on State: {current_state} leads to {transition_table[(current_state,letter)]}") 
            current_state = transition_table[(current_state,letter)]

            if index == (len(input_str) - 1):
                if (current_state in self.final_states):
                    validator = True
                    print("\n***** DNA Sequence is valid *****") 
                    return
                else:
                    validator = False
                    print("\n***** DNA Sequence is not valid *****")        
                    
        
            
        


def gather_states(dfas: tuple[DFA]):
    states = ()
    for dfa in dfas:
        states += dfa.states
    return states

def gather_final_states(dfas: tuple[DFA]):
    states = []
    for dfa in dfas:
        states.extend(dfa.final_states)
    return states

def concatenated_dfas_transition_func(dfas :tuple[DFA] , alphabet_with_episilon):
    transition_table :  dict[tuple[str, str], str] = {}

    for dfa_idx , dfa in enumerate(dfas):
        transition_table.update( dfa.transition_func( dfa.states , alphabet_with_episilon, True ) )

        if dfa_idx == 0: # Start Codeon DFA
            for state_idx , state in enumerate(dfa.states):
                if state_idx == 3: # Original Final State for Start Codeon DFA
                    transition_table[(state,"a")] = None
                    transition_table[(state,"t")] = None
                    transition_table[(state,"g")] = None
                    transition_table[(state,"ε")] = dfas[dfa_idx + 1].initial_state # ε-transition to initial state of middle motif codeon
        elif dfa_idx == 1: # Middle Motif DFA
                    for state_idx , state in enumerate(dfa.states):
                        if state_idx == 2 : # Original Final State for Middle Motif DFA
                            transition_table[(state,"t")] = None
                            transition_table[(state,"g")] = None
                            transition_table[(state,"ε")] = dfas[dfa_idx + 1].initial_state +"|"+ dfas[dfa_idx + 1 + 1].initial_state +"|"+ dfas[dfa_idx + 1 + 1 + 1].initial_state # Ending Codeons
    return transition_table

def concatenate_dfas(start_codeon : DFA, middle_motif : DFA, taa_stop_codeon : DFA, tag_stop_codeon : DFA, tga_stop_codeon : DFA):
    dfas = (start_codeon , middle_motif, taa_stop_codeon, tag_stop_codeon, tga_stop_codeon)
    final_dfas = (taa_stop_codeon, tag_stop_codeon, tga_stop_codeon)

    states = gather_states(dfas)
    alphabet_with_episilon = start_codeon.alphabet
    alphabet_with_episilon += ("ε",)
    final_states = gather_final_states(final_dfas)
    transition_func = concatenated_dfas_transition_func( (start_codeon , middle_motif, taa_stop_codeon, tag_stop_codeon, tga_stop_codeon) , alphabet_with_episilon)


    nfa = NFA(states, alphabet_with_episilon, transition_func, start_codeon.states[0], final_states)

    return nfa