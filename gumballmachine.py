from enum import Enum
from random import randint


class State(Enum):
    wait_for_coin = 0
    coin_in = 1
    check_coin = 2
    coin_out = 3
    gum_out = 4


class Message(Enum):
    insert_coin = 0
    request_gum = 1
    reject_coin = 2
    accept_coin = 3
    item_out = 4


state_Msg1 = (State.wait_for_coin, Message.insert_coin)
state_Msg2 = (State.coin_in, Message.request_gum)
state_Msg3 = (State.check_coin, Message.reject_coin)
state_Msg4 = (State.check_coin, Message.accept_coin)
state_Msg5 = (State.gum_out, Message.item_out)
state_Msg6 = (State.coin_out, Message.item_out)

state_msg_state = {
    state_Msg1: State.coin_in,
    state_Msg2: State.check_coin,
    state_Msg3: State.coin_out,
    state_Msg4: State.gum_out,
    state_Msg5: State.wait_for_coin,
    state_Msg6: State.wait_for_coin
}


def push(state, message):
    state_msg = (state, message)
    if state_msg in state_msg_state:
        new_state = state_msg_state[state_msg]
        if new_state == State.check_coin:
            random_nr = randint(1, 2)
            if random_nr % 2 == 0:
                new_state = push(new_state, Message.accept_coin)
            else:
                new_state = push(new_state, Message.reject_coin)
        return new_state
    return state
