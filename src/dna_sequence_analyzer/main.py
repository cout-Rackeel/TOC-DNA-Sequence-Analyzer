start_dfa = StartCodonDFA()
validation_dfa = ValidationDFA()

while True:
    dna_sequence = input("Enter Sequence or 0 to close: ")
    if dna_sequence == "0":
        exit(0)
    
    print("DNA Sequence:", dna_sequence)
    
    if start_dfa.process(dna_sequence):
        print("Start Codon: ACCEPTED")
    else:
        print("Start Codon: REJECTED")
    
    if validation_dfa.process(dna_sequence):
        print("DNA Validation: ACCEPTED")
    else:
        print("DNA Validation: REJECTED")
        
    print()
