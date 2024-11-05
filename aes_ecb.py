import time
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

# 16-byte AES key for AES-128 encryption
key = b'SecuritySolution'

# Example plaintext (must be padded to a multiple of the block size for ECB mode)
plaintext = b"Encryption_Tool Encryption_Tool Encryption_Tool "

# Function to measure encryption and decryption time
def measure_time_aes_ecb(key, plaintext):
    # Initialize cipher in ECB mode
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    decryptor = cipher.decryptor()

    # Pad plaintext to make it a multiple of 16 bytes (AES block size)
    padder = padding.PKCS7(128).padder()
    padded_plaintext = padder.update(plaintext) + padder.finalize()

    # Measure encryption time
    start_time = time.time()
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
    encryption_time = time.time() - start_time

    print("Ciphertext (hex):", ciphertext.hex())
    print(f"Encryption took {encryption_time:.6f} seconds")

    # Measure decryption time
    start_time = time.time()
    decrypted_padded_text = decryptor.update(ciphertext) + decryptor.finalize()
    decryption_time = time.time() - start_time

    # Unpad decrypted plaintext
    unpadder = padding.PKCS7(128).unpadder()
    decrypted_text = unpadder.update(decrypted_padded_text) + unpadder.finalize()

    print("Decrypted Text:", decrypted_text.decode())
    print(f"Decryption took {decryption_time:.6f} seconds")

# Run the function
measure_time_aes_ecb(key, plaintext)
