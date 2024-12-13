# Proyek 2 : Generator Kata Sandi (Password) Sederhana
# Fitur:

# " Membuat kata sandi dengan panjang dan
# kriteria khusus (huruf besar, angka, karakter khusus). "
# Menghasilkan kata sandi acak yang kuat sesuai dengan preferensi pengguna.

import random
import string

def generate_password(length, use_uppercase, use_digits, use_special_chars):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if length < 1 or not characters:
        print("Parameter tidak valid. Tidak dapat membuat kata sandi.")
        return None

    return ''.join(random.choice(characters) for _ in range(length))

def main():
    print("\nSelamat datang di Generator Kata Sandi!")

    while True:
        try:
            length = int(input("Masukkan panjang kata sandi yang diinginkan: "))
            use_uppercase = input("Gunakan huruf besar? (y/n): ").lower() == 'y'
            use_digits = input("Gunakan angka? (y/n): ").lower() == 'y'
            use_special_chars = input("Gunakan karakter khusus? (y/n): ").lower() == 'y'

            password = generate_password(length, use_uppercase, use_digits, use_special_chars)

            if password:
                print(f"\nKata sandi Anda: {password}\n")

            again = input("Ingin membuat kata sandi lain? (y/n): ").lower()
            if again != 'y':
                print("Terima kasih telah menggunakan Generator Kata Sandi!\n")
                break

        except ValueError:
            print("Masukkan panjang yang valid.\n")

if __name__ == "__main__":
    main()
