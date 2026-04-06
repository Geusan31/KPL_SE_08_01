```json
{
  "biodata": {
    "nama": "Budi",
    "umur": 22
  },
  "hobi": ["catur", "coding"]
}
```

- ini adalah sebuah objek
- key dan value
- nama dan umur adalah key
- budi adalah value dari key nama
- 22 adalah value dari key umur

- hubungan biodata terhadap objek(nama, umur)

- { => mulai objek
- "biodata" ini adalah sebuah key
- : ini adalah pemisah antara key dan vallue
- { ini adalah objek pembuka yang merupakan value dari key biodata
- "nama" adalah key
- "umur" adalah key
- } ini adalah penutup objek

- } => akhir dari sebuah objek

<!-- Endpoint: auth/login -> Method POST  -->

Payload Body -> HTTP -> Base Text
Form Data
```json
{
  "email": "admin@telu.ac.id",
  "password": "*****"
}
```

string JSON berbeda dengan json
{"email": "admin@telu.ac.id","password":"**\***"} -> Text

Parsing Dasar Int
[main.py](main.py)

Object Data di Python

```python
data = {
    "nama":"Budi",
    "umur":22
}

``javascript
const data = {
    nama: "Budi",
    umur: 22
}
```

```json
{
  "nama": "Budi",
  "umur": 22
}
```