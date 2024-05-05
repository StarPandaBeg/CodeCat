from enum import Enum


class ProblemStatus(Enum):
    none = 'не начато'
    solved = 'решено'
    wrong = 'неверное решение'
    time_exceed = 'превышен лимит времени'
    memory_exceed = 'превышен лимит объема памяти'


def get_problemstatus_items():
    return [(st.name, st.value) for st in ProblemStatus]


def test_solved(value: ProblemStatus):
    return value.value == ProblemStatus.solved.value


def test_failed(value: ProblemStatus):
    match value.value:
        case ProblemStatus.wrong.value | ProblemStatus.time_exceed.value | ProblemStatus.memory_exceed.value:
            return True
        case _:
            return False


def test_untouched(value: ProblemStatus):
    return value.value == ProblemStatus.none.value
