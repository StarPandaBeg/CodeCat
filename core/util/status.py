from enum import Enum


class ProblemStatus(Enum):
    none = 'не начато'
    solved = 'решено'
    wrong = 'неверное решение'
    time_exceed = 'превышен лимит времени'
    memory_exceed = 'превышен лимит объема памяти'


def get_problemstatus_items():
    return [(st.name, st.value) for st in ProblemStatus]
