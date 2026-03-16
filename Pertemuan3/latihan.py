from enum import Enum

class State(Enum):
    IDLE = "Idle"
    MENUNGGU_PRODUK = "Menunggu Produk"
    MENGELUARKAN_PRODUK = "Mengeluarkan Produk"
    SELESAI = "Selesai"
    
class Trigger(Enum):
    MASUKKAN_UANG="Masukkan Uang"
    PILIH_PRODUK="Pilih Produk"
    KELUARKAN_PRODUK="Keluarkan Produk"
    RESET = "Reset"

transitions = {
    State.IDLE: {
        Trigger.MASUKKAN_UANG: State.MENUNGGU_PRODUK
    },
    State.MENUNGGU_PRODUK: {
        Trigger.PILIH_PRODUK: State.MENGELUARKAN_PRODUK
    },
    State.MENGELUARKAN_PRODUK: {
        Trigger.KELUARKAN_PRODUK: State.SELESAI
    },
    State.SELESAI: {
        Trigger.RESET: State.IDLE
    }
}
 
def change_state(current_state, trigger):
    if current_state in transitions and trigger in transitions[current_state]:
        return transitions[current_state][trigger]
    return "Transisi tidak valid"

current_state = State.IDLE
print("State saat ini:", current_state)

next_state = change_state(current_state, Trigger.MASUKKAN_UANG)
print("State setelah trigger MASUKKAN_UANG:", next_state)

next_state = change_state(next_state, Trigger.PILIH_PRODUK)
print("State setelah trigger PILIH_PRODUK:", next_state)

next_state = change_state(next_state, Trigger.KELUARKAN_PRODUK)
print("State setelah trigger KELUARKAN_PRODUK:", next_state)

next_state = change_state(next_state, Trigger.RESET)
print("State setelah trigger RESET:", next_state)