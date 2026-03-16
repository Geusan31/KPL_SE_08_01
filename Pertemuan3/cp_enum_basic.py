from enum import Enum

class JenisKelamin(Enum):
    PRIA = 1
    WANITA = 2
    # PRIA => NAME/CATEGORY
    # 1 => VALUE/ID

patients = []

print(JenisKelamin.PRIA)
print(JenisKelamin.PRIA.value)
print(JenisKelamin.PRIA.name)