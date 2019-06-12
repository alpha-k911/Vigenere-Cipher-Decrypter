# Vigenère-Cipher-Decrypter
  <b>Vigenère-Cipher-Decrypter</b> is an tool that attempts to decrypt certain data encrypted by the  Vigenère cipher.
  This tool can decrypt Vigenère cipher <b>with</b> and <b>without Key</b>

## The Files
  </b>vegenere.py</b> is the <i><b>python3</b></i> file for decrypting the cipher
  
## Method
  The encrypted data is decrypted by frequencies of letters observed and the key length is detected by peaks observed in the encrypted data and its shifts.

## Libraries Used
  <b>indexes</b> from <b><i>peakutils.peak</i></b> for finding the length of key from peak values with recursive shifts in cipher.
