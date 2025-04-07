# Analysis: time = O(n), space = O(n)
# where n = len(s)
def caesarCipher(s, k):
    res = []
    
    for letter in s:
        if letter.isalpha():
            offset = ord("A") if letter.isupper() else ord('a')
            shifted = (ord(letter) - offset + k) % 26
            res.append(chr(offset + shifted))
        else:
            res.append(letter)
        
    return ''.join(res)


if __name__ == "__main__":
    test_cases = [
        # (input_string, shift, expected_output)
        ("middle-Outz", 2, "okffng-Qwvb"),
        ("Always-Look-on-the-Bright-Side-of-Life", 5, "Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj"),
        ("xyz", 2, "zab"),
        ("ABC", 3, "DEF"),
        ("No-Change!", 0, "No-Change!"),
        ("WrapAround-Zz", 52, "WrapAround-Zz"),  # k is a full cycle
        ("Punctuation? Stay: Put!", 1, "Qvoduvbujpo? Tubz: Qvu!"),
        ("", 10, ""),  # Empty string
        ("Case123Mix", 4, "Gewi123Qmb")
    ]

    for i, (s, k, expected) in enumerate(test_cases, 1):
        output = caesarCipher(s, k)
        assert output == expected, f"Test case {i} failed: expected {expected}, got {output}"

    print("All test cases passed!")



