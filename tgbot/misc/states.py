from aiogram.dispatcher.filters.state import StatesGroup, State


class CollectInfoEss(StatesGroup):
    # type state
    Type_essay_state = State()
    # topic states
    Topic_state = State()
    Scan_Topic_state = State()
    next_text_topic_state = State()
    # essay states
    Essay_state = State()
    Scan_Essay_state = State()
    next_text_essay_state = State()
    # last state
    Last_state = State()
    Bestv_state = State()
