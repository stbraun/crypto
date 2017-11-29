class IllegalKeyException(Exception):
    pass


class Vigenere:
    """ Implementation of the Vigenère cipher.

    The Vigenère cipherbelongs to the polyalphabetic ciphers. It uses not
    only one cipher alphabet, but multiple to encode a message making
    the cipher much harder to break. On the other hand the effort for
    encoding and decoding is quite high. Because of this effort the
    Vingenère cipher was not used for about 200 years despite its qualities.

    This implementation works for characters, numbers and some punctuation
    marks: see plain_alphabet.
    """

    def __init__(self, key):
        self.key = str(key).upper()
        self.base = ord('A')
        self.plain_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789.:,;!?"
        self.cipher_alphabets = []
        self.__initialized = False

    def __gen_cipher_alphabets(self):
        alpha = self.plain_alphabet
        for i in range(len(alpha)):
            a = alpha[1:] + alpha[0]
            self.cipher_alphabets.append(a)
            alpha = a

    def __find_alphabet(self, key):
        for alphabet in self.cipher_alphabets:
            if alphabet[0] == key:
                return alphabet
        raise IllegalKeyException

    def __initialize(self):
        if not self.__initialized:
            self.__gen_cipher_alphabets()
            self.__initialized = True

    def encrypt(self, plain):
        self.__initialize()
        plain_u = str(plain).upper()
        cipher = []
        k_idx = 0;
        for mc in plain_u:
            try:
                p_idx = self.plain_alphabet.index(mc)
                kc = self.key[k_idx]
                k_idx = (k_idx + 1) % len(self.key)
                cipher_alphabet = self.__find_alphabet(kc)
                cipher.append(cipher_alphabet[p_idx])
            except (
            ValueError):  # Happens if unsupported characters are in the
                # plain text.
                pass
        return ''.join(cipher)

    def decrypt(self, cipher):
        self.__initialize()
        plain = []
        k_idx = 0
        for cc in cipher:
            kc = self.key[k_idx]
            k_idx = (k_idx + 1) % len(self.key)
            cipher_alphabet = self.__find_alphabet(kc)
            plain.append(self.plain_alphabet[cipher_alphabet.index(cc)])
        return ''.join(plain)
