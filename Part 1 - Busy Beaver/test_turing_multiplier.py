# -*- coding: utf-8 -*-
from turing_machine_first import TuringMachine
from test_turing_machine_example1 import print_states

#create the Turing machine
transitions = {
        # TODO: Part II b) - Write your transition rules here as entries to a Python dictionary
    ('q0', '1'): ('q1', 'X', 'R'), 
    ('q0', '0'): ('q6', '0', 'L'),  

    ('q1', '1'): ('q1', '1', 'R'),
    ('q1', '0'): ('q2', '0', 'R'),

    ('q2', '1'): ('q3', 'Y', 'R'),   
    ('q2', 'Y'): ('q2', 'Y', 'R'),   
    ('q2', 'Z'): ('q5', 'Z', 'L'),   
    ('q2', ''): ('q5', '', 'L'),   

    ('q3', '1'): ('q3', '1', 'R'),
    ('q3', 'Z'): ('q3', 'Z', 'R'),
    ('q3', ''): ('q4', 'Z', 'L'),    

    ('q4', 'Z'): ('q4', 'Z', 'L'),
    ('q4', '1'): ('q4', '1', 'L'),
    ('q4', 'Y'): ('q2', 'Y', 'R'),  

    ('q5', 'Y'): ('q5', '1', 'L'),   
    ('q5', '0'): ('q5', '0', 'L'),
    ('q5', '1'): ('q5', '1', 'L'),
    ('q5', 'X'): ('q0', 'X', 'R'),  

    ('q6', 'X'): ('q6', '', 'L'),
    ('q6', ''): ('q7', '', 'R'),    

    ('q7', ''): ('q7', '', 'R'),
    ('q7', '0'): ('q8', '', 'R'),    

    ('q8', '1'): ('q8', '', 'R'),
    ('q8', 'Z'): ('q9', '1', 'R'),   
    ('q8', ''): ('qa', '', 'L'),

    ('q9', 'Z'): ('q9', '1', 'R'),
    ('q9', ''): ('q10', '', 'L'), 
    ('q10', '1'): ('q10', '1', 'L'), 
    ('q10', ''): ('qa', '', 'R'),  

}

if __name__ == "__main__":
    print_states(transitions)
    machine = TuringMachine(transitions)

    def run(input_):
        w = input_
        print("Input:",w)
        print("Accepted" if machine.accepts(w) else "Rejected")
        machine.debug(w, step_limit=1000)

        print()

    # SHOULD ACCEPT
    run("110111")
    # outputs 111111

    # SHOULD ACCEPT
    run("11101111")
    # outputs 111111111111

    run("01111")
