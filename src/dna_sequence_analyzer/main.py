
import StartCodonDFA as startDFA
import ValidationDFA as validateDFA
from nfa_builder import nfa

start_dfa = startDFA.StartCodonDFA()
validation_dfa = validateDFA.ValidationDFA()

while True:
    dna_sequence = input("\nEnter DNA Sequence or 0 to close: ")

    if dna_sequence == "0":
        break

    print("\nDNA Sequence:", dna_sequence)

    # Member A: Validation
    if not validation_dfa.process(dna_sequence):
        print("DNA Validation: REJECTED")
        continue

    print("DNA Validation: ACCEPTED")

    # Member A: Start Codon
    if start_dfa.process(dna_sequence[:3]):
        print("Start Codon: ACCEPTED")
    else:
        print("Start Codon: REJECTED")
        continue

    # Member B: Combined NFA
    print("\n--- NFA Analysis ---")
    nfa.test_if_string_is_vaild(dna_sequence.lower())

