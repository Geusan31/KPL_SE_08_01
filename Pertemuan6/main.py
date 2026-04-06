import json


def parse_integer():
    input_str = input("Masukkan nilai yang akan dikuadratkan:")
    try:
        number = int(input_str)
        result = number**2
        print(f"Hasil kuadrat dari {number} adalah {result}.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka yang benar.")


# if __name__ == "__main__":
#     parse_integer()

data = {
    "name": "John Doe",
    "age": 30,
}

json_str = json.dumps(data)

print(data)
print(json_str)
print(data['name']) # ini adalah objek/dictionary
# print(json_str["nama"]) # ini adalah string JSON
# print(data == json.loads(json_str))
