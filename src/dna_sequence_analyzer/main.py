
import Automata

# run cd src/dna_sequence_analyzer; python3 main.py

alphabet = ("a", "t", "g", "c",)
codeon_states = ("A1", "B1", "C1", "D1", "E1",)
middle_motif_states = ("A2", "B2", "C2", "E2",)
taa_stop_codeon_states = ("A3", "B3", "C3", "D3", "E3",)
tag_stop_codeon_states = ("A4", "B4", "C4", "D4", "E4",)
tga_stop_codeon_states = ("A5", "B5", "C5", "D5", "E5",)

def print_concat_states(states):
    for idx,state in enumerate(states):
        print(f"{idx}:{state}")

start_codeon_dfa = Automata.DFA(codeon_states, alphabet , Automata.start_codeon_transition_func, codeon_states[0], [codeon_states[3]])
# start_codeon_Automata.test_if_string_is_vaild("atg")
# print("START CODEON DFA TRANSITION TABLE")
# start_codeon_Automata.print_transition_table()

middle_motif_dfa = Automata.DFA(middle_motif_states, alphabet, Automata.middle_motif_transition_func, middle_motif_states[0], [middle_motif_states[2]])
# middle_motif_Automata.test_if_string_is_vaild("atatatatatat")
# print("MIDDLE MOTIF DFA TRANSITION TABLE")
# middle_motif_Automata.print_transition_table()

taa_stop_codeon_dfa = Automata.DFA(taa_stop_codeon_states, alphabet, Automata.taa_stop_codeon_transition_func, taa_stop_codeon_states[0], [taa_stop_codeon_states[3]])
# taa_stop_codeon_Automata.test_if_string_is_vaild("taa")
# print("STOP CODEON 1(TAA) DFA TRANSITION TABLE")
# taa_stop_codeon_Automata.print_transition_table()

tag_stop_codeon_dfa = Automata.DFA(tag_stop_codeon_states, alphabet, Automata.tag_stop_codeon_transition_func, tag_stop_codeon_states[0], [tag_stop_codeon_states[3]])
# tag_stop_codeon_Automata.test_if_string_is_vaild("tag")
# print("STOP CODEON 2(TAG) DFA TRANSITION TABLE")
# tag_stop_codeon_Automata.print_transition_table()

tga_stop_codeon_dfa = Automata.DFA(tga_stop_codeon_states, alphabet, Automata.tga_stop_codeon_transition_func, tga_stop_codeon_states[0], [tga_stop_codeon_states[3]])
# tga_stop_codeon_Automata.test_if_string_is_vaild("tga")
# print("STOP CODEON 3(TGA) DFA TRANSITION TABLE")
# tga_stop_codeon_Automata.print_transition_table()

nfa = Automata.concatenate_dfas(start_codeon_dfa , middle_motif_dfa, taa_stop_codeon_dfa, tag_stop_codeon_dfa, tga_stop_codeon_dfa)

# nfa.print_transition_table()
nfa.test_if_string_is_vaild("atgatatatattaag")
# print_concat_states(nfa.states)



#   if current_state == self.states[7]:
#                 print(f"{index}")
#                 if (index + 3) > len(input_str):
#                     print("String too short to be valid")
#                     validator = False