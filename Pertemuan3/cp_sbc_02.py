from enum import Enum

class StudentState(Enum):
    TERDAFTAR = "Terdaftar"
    CUTI = "Cuti"
    AKTIF = "Aktif"
    LULUS = "Lulus"
    
class Trigger(Enum):
    CETAK_KSM = "Cetak KSM"
    LULUS = "Lulus"
    MENGAJUKAN_CUTI = "Mengajukan Cuti"
    MENYELESAIKAN_CUTI = "Menyelesaikan Cuti"
    
transitions = {
    StudentState.TERDAFTAR: {
        Trigger.CETAK_KSM: StudentState.AKTIF,
        Trigger.MENGAJUKAN_CUTI: StudentState.CUTI
    },
    StudentState.AKTIF: {
        Trigger.LULUS: StudentState.LULUS,
        Trigger.MENGAJUKAN_CUTI: StudentState.CUTI
    },
    StudentState.CUTI: {
        Trigger.MENYELESAIKAN_CUTI: StudentState.TERDAFTAR
    },
}

def change_state(current_state, trigger):
    if current_state in transitions and trigger in transitions[current_state]:
        return transitions[current_state][trigger]
    return "Transisi tidak valid"

current_state = StudentState.AKTIF
print("State saat ini:", current_state)

next_state = change_state(current_state, Trigger.LULUS)
print("State setelah trigger LULUS:", next_state)

next_state = change_state(current_state, Trigger.MENGAJUKAN_CUTI)
print("State setelah trigger MENGAJUKAN_CUTI:", next_state)