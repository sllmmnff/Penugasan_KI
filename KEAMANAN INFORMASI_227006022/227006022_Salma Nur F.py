import string

def encrypt(pesan, key):
    abjad = string.printable[:-5]  # Menggunakan abjad yang sesuai tanpa karakter spesial
    cipher = ''
    for char in pesan:
        if char in abjad:
            index = (abjad.find(char) + key) % len(abjad)
            cipher += abjad[index]
        else:
            cipher += char  # Menambahkan karakter non-abjad seperti spasi dan tanda baca
    return cipher

def decrypt(cipher, key):
    abjad = string.printable[:-5]
    pesan = ''
    for char in cipher:
        if char in abjad:
            index = (abjad.find(char) - key) % len(abjad)  # Menggunakan modulus panjang abjad
            pesan += abjad[index]
        else:
            pesan += char
    return pesan

if __name__ == '__main__':
    print("=============================================")
    print('|===ENCRYPT AND DECRYPT WITH CAESAR CIPHER==|')
    print("=============================================")
    
    while True:
        option = int(input('1. Encrypt\n2. Decrypt\n3. Keluar\nPilih Option: '))
        if option == 1:
            pesan = input('Masukkan Pesan/Teks ingin dienkripsi (Plaintext): ')
            key = int(input('Masukkan Key: '))
            print("Pesan Terenkripsi:", encrypt(pesan, key))
        elif option == 2:
            cipher = input('Masukkan Pesan/Teks yang dienkripsi (Ciphertext): ')
            key = int(input('Masukkan Key: '))
            print("Pesan Terdekripsi:", decrypt(cipher, key))
        elif option == 3:
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")
