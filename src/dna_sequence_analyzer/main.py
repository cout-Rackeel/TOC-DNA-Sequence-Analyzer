
import StartCodonDFA as startDFA
import ValidationDFA as validateDFA

from nfa_builder import nfa
from integration_adapter import adapt_nfa
from nfa_to_dfa import convert_nfa_to_dfa
from dfa_runner import run_dfa, trace_dfa


# MEMBER A: Initialize validation and start codon
start_dfa = startDFA.StartCodonDFA()
validation_dfa = validateDFA.ValidationDFA()

# MEMBER B: Retrieve the combined NFA
table, initial, final = adapt_nfa(nfa)

# MEMBER C: Convert the NFA into a DFA
dfa, dfa_start, dfa_final = convert_nfa_to_dfa(
    table, initial, final
)

# MEMBER D: Reserved for minimization and RE derivation
# Until available, use the unminimized DFA.
active_dfa = dfa
active_start = dfa_start
active_final = dfa_final


print("=" * 50)
print("       DNA SEQUENCE PATTERN ANALYZER")
print("=" * 50)

print("NFA States:", len(table))
print("DFA States:", len(dfa))
print("Accepting States:", len(dfa_final))
print("Minimization: Not implemented")


while True:

    dna_sequence = input(
        "\nEnter DNA Sequence or 0 to close: "
    )

    if dna_sequence == "0":
        print("Program closed.")
        break

    print("\nDNA Sequence:", dna_sequence)

    # MEMBER A: Validate nucleotides
    if not validation_dfa.process(dna_sequence):
        print("DNA Validation: REJECTED")
        print("FINAL RESULT: REJECTED")
        continue

    print("DNA Validation: ACCEPTED")

    # MEMBER A: Check start codon
    if not start_dfa.process(dna_sequence[:3]):
        print("Start Codon: REJECTED")
        print("FINAL RESULT: REJECTED")
        continue

    print("Start Codon: ACCEPTED")

    # MEMBER B: NFA simulation
    print("\n--- NFA Analysis ---")
    nfa.test_if_string_is_vaild(
        dna_sequence.lower()
    )

    # MEMBER C: Execute the converted DFA
    print("\n--- DFA Analysis ---")

    trace_dfa(
        dna_sequence,
        active_dfa,
        active_start,
        active_final
    )

    accepted = run_dfa(
        dna_sequence,
        active_dfa,
        active_start,
        active_final
    )

    print("\n" + "=" * 50)

    if accepted:
        print("FINAL RESULT: ACCEPTED")
    else:
        print("FINAL RESULT: REJECTED")

    print("=" * 50)

