#!/usr/bin/python3
import argparse
from peakutils.peak import indexes
import logging

MODULE_DESCRIPTION = """Vigenère-Cipher-Decrypter is a tool that attempts to decrypt certain data encrypted
by the Vigenère cipher. This tool can decrypt Vigenère cipher with and without Key"""



def encrypt():
    a = ""

def guessKey(ciphertext=None,verbose=False):
    a = ciphertext
    b = ciphertext
    freq = []
    for i in range(0, len(a) - 1):
        b = " " + b[:-1]
        c = 0
        for j in range(i, len(a)):
            if b[j] == a[j]:
                c += 1
        freq.append(c)
        # print(c)
    # peaks = find_peaks(freq)
    peaks = indexes(freq, thres=0.678)
    # print(freq)
    # print(peaks)
    possible_keys = []
    possible_keys.append(peaks[1] - peaks[0])
    logging.info("Possible Key Length: {} ".format(possible_keys[0]))
    # print(possible_keys[0])
    # print(type(possible_keys[0]))
    # key = input("Select a Key: ")
    # print(peaks)
    # print(freq)
    #logging.debug("Possible Key Lengths : {} ".format(possible_keys))
    logging.debug("Peaks : {}".format(peaks))
    logging.debug("Freq  : {}".format(freq))
    key = possible_keys[0]

    # ciphers
    j = 0
    ciphers = []
    p = ""
    while (j < key):
        i = j
        p = ""
        while (i < len(a)):
            # print(a[i],end=" ")
            p = p + a[i]
            i = i + key
        j += 1
        ciphers.append(p)
        # print(p)

    # frequency
    ciphers_freq = []
    for i in range(0, len(ciphers)):
        arr = [0] * 26
        p = ciphers[i]
        # i = 0
        # arr = [0] * 26
        j = 0
        while (j < len(p)):
            pos = (ord(p[j]) - 13) % 26
            arr[pos] += 1
            j += 1
        ciphers_freq.append(arr)
    # print("Ciphers: ")
    # print(ciphers_freq)
    logging.debug("Ciphers : {}".format(ciphers_freq))
    # map of fequency
    ind = []
    for i in range(0, 26):
        ind.append(i)

    def shift_left(f, t1):
        i = 0
        while i < f:
            t2 = t1
            t1 = t2[1:len(t2)] + [t2[0]]
            i += 1
        return t1

    j = 0
    char_freq = [0.08, 0.02, 0.03, 0.04, 0.13, 0.02, 0.02, 0.06, 0.07, 0.0, 0.01, 0.04, 0.02, 0.07, 0.08, 0.02, 0.0,
                 0.06, 0.06, 0.09, 0.03, 0.01, 0.02, 0.0, 0.02, 0.0]

    freq_sums = []

    def get_key(ciphers_freq, key_len):
        guessed_key = ""
        for l in range(0, key_len):
            freq_sums = []
            for i in range(0, 26):
                shift = shift_left(i, ciphers_freq[l])
                sum = 0
                for k in range(0, 26):
                    sum += shift[k] * char_freq[k]
                freq_sums.append(sum)
            freq_max = zip(freq_sums, ind)
            freq_max = list(freq_max)
            freq_max = sorted(freq_max, reverse=True)
            # print(freq_max[0][1])
            guessed_key += chr(65 + freq_max[0][1])
        return guessed_key

    logging.info("Guessed Key: " + get_key(ciphers_freq, key))
    print("[+] Guessed Key: " + get_key(ciphers_freq, key))
    return get_key(ciphers_freq, key)




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=MODULE_DESCRIPTION)
    parser.add_argument("action",help="Action to perform on the input [encrypt/guesskey/decrypt] [e/g/d]")
    parser.add_argument("input",help="Input to be processed")
    parser.add_argument("-v", "--verbose",help="print debug info",action="store_true")
    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG,format='%(levelname)s : %(message)s ')

    if args.action.lower() == "encrypt" or args.action.lower() == "e":
        pass
    elif args.action.lower() == "decrypt" or args.action.lower() == "d":
        pass
    elif args.action.lower() == "guesskey" or args.action.lower() == "g" or args.action.lower() == "guess":
        if len(args.input) < 500:
            logging.warning(" Key Detection will be much accurate if the cipher is enough long")
        guessKey(args.input)