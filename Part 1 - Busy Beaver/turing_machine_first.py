# -*- coding: utf-8 -*-
"""A Turing machine simulator skeleton.

    Accepting '#'
    =============

    >>> from turing_machine import TuringMachine

    Instantiate the machine with particular transitions.

    >>> one_hash = TuringMachine(
    ...     {
    ...         ('q0', '#'): ('saw_#', '#', 'R'),
    ...         ('saw_#', ''): ('qa', '', 'R'),
    ...     }
    ... )

    Check whether it accepts a string:

    >>> one_hash.accepts('#')
    True

    >>> one_hash.accepts('##')
    False

    Check whether it rejects a string:

    >>> one_hash.rejects('#')
    False

    >>> one_hash.rejects('##')
    True

"""

import logging
from itertools import islice


class TuringMachine:
    """Turing machine simulator class.

    A machine is instantiated with transitions, start, accept and reject states
    and a blank symbol. We assume that the input and the tape alphabet can be
    deducted from the transitions.

    :param dict transitions: a mapping from (state, symbol) tuples to (state,
    symbol, direction) tuple. Directions are either 'L' (for left) or 'R' (for right).

    :param start_state: the initial state of the machine.

    :param accept_state: the accept state.

    :param reject_state: the reject state.

    :blank_symbol: the special symbol that marks the tape cell to be empty.

    """

    def __init__(self, transitions, start_state='q0', accept_state='qa', reject_state='qr', blank_symbol=''):
        # TODO: Implement the constructor. Initialize transitions, start_state, accept_state,
        # reject_state, blank_symbol, and any other helpful structures.
        self.transitions = transitions
        self.start_state = start_state
        self.accept_state = accept_state
        self.reject_state = reject_state
        self.blank_symbol = blank_symbol

    def run(self, input_):
        """Execute the Turing machine for a particular input.

        :param input_: the input that is written on the tape. It can be a list
        of strings, or just a string, in which case each letter is treated as a symbol.

        This method MUST be a Python generator. It should yield a (action, configuration) tuple
        at each step of the computation.
        
        The action is either 'Accept', 'Reject' or None. 
        
        Configuration is a dictionary with the following keys:
        - 'state': the current state,
        - 'left_hand_side': list of symbols on the left hand side of the current position (closest first),
        - 'symbol': the current symbol under the head,
        - 'right_hand_side': list of symbols on the right hand side of the current position.

        """
        # TODO: Implement the simulator loop as a Python generator.
        # 1. Initialize the tape using two lists (left_hand_side and right_hand_side) and the current symbol.
        # 2. Yield the current step (action, configuration).
        # 3. Read transitions and update state, write symbols, and move the head ('L' or 'R').
        # 4. Handle tape expansion dynamically for both left and right directions (double-sided infinite tape).
        # 5. Log a warning using logging.warning() if the singly-infinite tape boundary is crossed before Part III.
        tape_input= list(input_)
        state=self.start_state 
        if tape_input:
            current_symbol = tape_input[0]
            right_hand_side = tape_input[1:]
        else:
            current_symbol = self.blank_symbol
            right_hand_side = []
            
        left_hand_side = [self.blank_symbol]  # برای پیدا کردن سمت چپ ترین ورودی لازمه اولین خانه سمت چپ را علامت بزنیم
        head_position = 1
        boundary_warning_logged = False
        while True:
            if state == self.accept_state:
                action = 'Accept'
            elif state == self.reject_state:
                action = 'Reject'
            else:
                action = None
            configuration = {'state': state,'left_hand_side': list(left_hand_side),'symbol': current_symbol,'right_hand_side': list(right_hand_side)}
            yield (action, configuration)
            if action is not None:
                break
            transition_key = (state, current_symbol)
            if transition_key not in self.transitions:
                state = self.reject_state
                continue
            next_state, write_symbol, direction = self.transitions[transition_key]
            
            state = next_state
            current_symbol = write_symbol

            if direction == 'L':
                if head_position == 0:
                    logging.warning("Singly-infinite tape boundary crossed ""(cannot move left from position 0).")
                    state = self.reject_state
                    continue
                head_position -= 1
                right_hand_side.insert(0, current_symbol)
                if left_hand_side:
                    current_symbol = left_hand_side.pop(0)
                else:
                    current_symbol = self.blank_symbol
                    
            elif direction == 'R':
                head_position += 1
                left_hand_side.insert(0, current_symbol)
                if right_hand_side:
                    current_symbol = right_hand_side.pop(0)
                else:
                    current_symbol = self.blank_symbol
            else:
                raise ValueError(f"Invalid direction: {direction}. ""Direction must be 'L' or 'R'.")

    def accepts(self, input_, step_limit=100):
        """Check whether the Turing machine accepts a string.

        :param input_: the input string or list.
        :param step_limit: the maximum number of steps to simulate before stopping.
        :return: True if the machine halts in accept_state, False if it rejects,
                 or None if the step limit is reached without halting.
        """
        # TODO: Run the generator up to step_limit and check the action of the final yielded state.
        # Remember to log a warning if the step_limit is reached without halting.
        for step_idx, (action, config) in enumerate(self.run(input_)):
            if action == 'Accept':
                return True
            if action == 'Reject':
                return False
            if step_idx >= step_limit:
                logging.warning(f"Step limit of {step_limit} reached without halting.")
                return None
        return None

    def rejects(self, input_, **kwargs):
        """Check whether the Turing machine rejects a string.

        :param input_: the input string or list.
        :return: True if the machine rejects the string, False if it accepts.
        """
        # TODO: Determine rejection by checking if accepts() returns False.
        result = self.accepts(input_, **kwargs)
        if result is None:
            return None
        return not result

    def debug(self, input_, step_limit=100, colored=False):
        """Print the execution configuration of the machine per transition for debugging.

        :param input_: the input string or list.
        :param step_limit: the maximum number of steps to output.
        :param colored: True to output colored boundaries in terminal.
        """
        # TODO: Loop over the steps yielded by run() up to step_limit and print the tape configuration.
        # E.g., print the state and the tape with the head highlighted in brackets like: left[symbol]right
        GREEN = '\033[92m'
        RED = '\033[91m'
        BLUE = '\033[94m'
        RESET = '\033[0m'

        print(f"--- Debugging Turing Machine (Input: '{input_}') ---")
        for step_idx, (action, config) in enumerate(islice(self.run(input_), step_limit + 1)):
            state = config['state']
            left = "".join(reversed(config['left_hand_side']))
            sym = config['symbol']
            right = "".join(config['right_hand_side'])
            
            if colored:
                head_str = f"{BLUE}[{sym}]{RESET}"
                if action == 'Accept':
                    state_str = f"{GREEN}{state}{RESET}"
                elif action == 'Reject':
                    state_str = f"{RED}{state}{RESET}"
                else:
                    state_str = state
            else:
                head_str = f"[{sym}]"
                state_str = state
                
            tape_str = f"{left}{head_str}{right}"
            print(f"Step {step_idx:03d} | State: {state_str:<5} | Tape: {tape_str}")
            
            if action is not None:
                print(f"--- Machine Halted: {action} ---")
                break
        else:
            print(f"--- Step limit ({step_limit}) reached ---")

