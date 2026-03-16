from enum import Enum

class JenisKelamin(Enum):
    PRIA = 1
    WANITA = 2

patients = []

def addPatient(name: str, gender: JenisKelamin):
    if not isinstance(gender, JenisKelamin):
        raise ValueError("Jenis kelamin harus PRIA atau WANITA dari Enum JenisKelamin")
    patients.append({"Nama": name, "Jenis Kelamin": gender})
    print(f"Pasien {name} dengan jenis kelamin {gender.name} berhasil ditambahkan.")

addPatient("Budi", JenisKelamin.PRIA)
addPatient("Siti", JenisKelamin.WANITA)

print("\nDaftar Pasien:")
for patient in patients:
    print(f"Nama: {patient['Nama']}, Jenis Kelamin: {patient['Jenis Kelamin'].name}")