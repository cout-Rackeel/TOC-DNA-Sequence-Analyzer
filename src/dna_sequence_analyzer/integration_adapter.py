
def adapt_nfa(nfa):
    converted = {
        state: {symbol: set() for symbol in "ACGTE"}
        for state in nfa.states
    }

    for (state, symbol), destination in (
        nfa.generateTransitionTable().items()
    ):
        key = "E" if symbol == "ε" else symbol.upper()

        if destination is not None:
            converted[state][key].update(
                destination.split("|")
            )

    return (
        converted,
        nfa.initial_state,
        set(nfa.final_states)
    )

