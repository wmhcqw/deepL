import numpy as np


def from_text_to_number(msg):
    start_index = msg.find("%")+1
    end_index = msg[start_index:].find("%") + start_index
    return float(msg[start_index:end_index])