from Crypto.Cipher import AES

key = open('app.data/data.key', 'r').read()
key = bytes.fromhex(key)
bufferSize = 32768  # 32kb


def encrypt(inputFile, outputFile):
    cipher = AES.new(key, AES.MODE_CFB)
    outputFile.write(cipher.iv)

    buffer = inputFile.read(bufferSize)
    while len(buffer) > 0:
        ciphered_bytes = cipher.encrypt(buffer)
        outputFile.write(ciphered_bytes)
        buffer = inputFile.read(bufferSize)

    inputFile.close()
    outputFile.close()


def decrypt(inputFile, outputFile):
    iv = inputFile.read(16)
    cipher = AES.new(key, AES.MODE_CFB, iv=iv)

    buffer = inputFile.read(bufferSize)
    while len(buffer) > 0:
        decryptedBytes = cipher.decrypt(buffer)
        outputFile.write(decryptedBytes)
        buffer = inputFile.read(bufferSize)

    inputFile.close()
    outputFile.close()


"""ifile = open('decrypted.yaml', 'rb')
ofile = open('data.yaml', 'wb')
encrypt(ifile, ofile)"""
