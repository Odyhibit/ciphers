def add_or_create(dictionary:{}, key: str, amount:int=1):
    if key in dictionary:
        dictionary[key] += amount
    else:
        dictionary[key] = 1


alphabet = {}
letter_pairs = {}
cipher_text_1 = "UOMAESvShPvSqPZ1nsZSwLvSgYZzAyeQTpwvAOLgEZTjMRpqQNvAQpQPQAE1QuQAJURUTwBsZAQvUAZWyUTue0hTBZkqLvAUyLAFvUpUTukGUAuMGAM0fgUTQ1NyvOYvAMwWUTGMjUAQ1FAQFULQTEGLAUqyTkBQwQTUswULwbhZAqFPTYsNUAydBq1ZAUdsTURkAveqeRQ1TYgNknjNUZTQLP"
cipher_text_2 ="WBQisTRhqmiO0mo0himTHLogiPWfNsGoGmNz0mqkvk0qfGBUmRYnrgLgGqmUvHGfBvpmrQByqfGvi0GmGFrfhFLifWHFifysqbzQWskpWsgQWsv0qbkPqSmiqifvqGJimisvmUODBGmUTimLJt0kGVWfPpVGf0tGvGmGNFmi0QminiQimWTBPOGsmHiOifqbJBbqmneqmytpWmQeFh"
cipher_text_3 ="QpwhEeLALNzALmzAnqzAn1XALmtAZsznFXqDJhrEYTDysUpJAztLrEi1zsyL1shQXE1AhBysbFKSmhqAER1AEgDrEgRzrsyByzhErNtinAsOcmersNypmXAsOcqyEAOiOPynsTfvihEKSYhsQOysyfXEhAyEwyfyEhpyShsgLhRhsybzpJOSNrsmYXEAUTysSKhphsySc"
cipher_text_4 ="EbwbNrEnbfsYFmNclOfctUNOubTbfHniofcirfSwdcofsyoubfb0TcyrfYTmNmKCVGoAfntEoNHotCJrNYOlbNoGOfoBUTZVJlmNoJUNKUZoNDyryHUrycUmyqUryTJmACKmQftmbWoNEtCsrfomofwVnJZiqbrfbnONi0YOCoqmfotoJbfbyTNFYVsloKrfnVbfo0bFo"
cipher_text_5 ="nEUEfWUqbuUERuUE1OUEbtUIsLcKcdcUDsfcbBUdgl0bpUsSpVDsDSWAdLtMZAdMfpscOWs0WRcdcFpsBEDkDde0DsU0M0JcEsg0yDsmqSWkP0UsVFgcdcKOd1UcmcdWbefsJUPWHgRcAdUyFcdS1UdcqPsA1DL0gWfAdpkc1csDPcOcdD1usgByScEHAsFJibcdcLcuc"
cipher_text = cipher_text_5 + cipher_text_4 + cipher_text_3 + cipher_text_2 + cipher_text_1

for i in range(5):
    this_cipher = [cipher_text_1, cipher_text_2, cipher_text_3, cipher_text_4, cipher_text_5]
    alphabet.clear()
    letter_pairs.clear()
    for letter in this_cipher[i]:
        add_or_create(alphabet, letter)

    for letters in range(0, len(this_cipher[i]), 2):
        if len(cipher_text) >= letters + 2:
            add_or_create(letter_pairs, cipher_text[letters:letters + 2])

    print(f"Cipher text {i}")
    print(f"{len(this_cipher[i])} total chars")
    #print(this_cipher[i])
    print(f"{len(alphabet)} unique chars")
    print(f"{len(letter_pairs)} letter pairs")
    print()
