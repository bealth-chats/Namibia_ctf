# Cracking the Code: A Walkthrough of the "Bashful Dwarf" CTF Challenge

*By Jules*

In the world of Capture The Flag (CTF) competitions, cryptography challenges often test your ability to recognize patterns and apply classic decoding techniques. Today, I’m going to walk you through a recent challenge I solved, breaking down the steps from initial analysis to the final flag.

## The Challenge

The challenge provided a cryptic note and a required flag format.

**The Note:**
> "y4$sufo_ra_nb_GLK_GRVI_wd4iu_yfwwb_CW"

**Flag Format:**
> NICCTF26{}

At first glance, the string looks like random gibberish, but the structure—specifically the underscores—suggests it might be a sentence where letters have been substituted. The mixed case and special characters (`$`) are interesting features that might be preserved or transformed.

## Step 1: Initial Analysis

My first step in any crypto challenge is to check the basics. Is it Base64? No, the character set includes `$` and underscores, which aren't standard for Base64 (though variants exist, the length and structure didn't look right). Is it a Caesar cipher? That's always a good starting point.

I decided to write a quick Python script to brute-force some common simple ciphers:
1.  **Caesar Cipher (ROT1-25):** Shifting letters by `N` positions.
2.  **Atbash Cipher:** Reversing the alphabet (A becomes Z, B becomes Y, etc.).
3.  **Reverse String:** Just reading it backwards.

## Step 2: Scripting the Solution

Here is the script I used to explore these possibilities:

```python
import string

ciphertext = "y4$sufo_ra_nb_GLK_GRVI_wd4iu_yfwwb_CW"

# ... ROT functions ...

def atbash(text):
    result = ""
    for char in text:
        if char.islower():
            result += chr(ord('z') - (ord(char) - ord('a')))
        elif char.isupper():
            result += chr(ord('Z') - (ord(char) - ord('A')))
        else:
            result += char
    return result

print("\n--- Atbash ---")
print(atbash(ciphertext))
```

## Step 3: The Breakthrough

Running the script produced output for all 25 ROT variations, but none of them looked like English. However, the output for the **Atbash cipher** immediately caught my eye:

**Ciphertext:** `y4$sufo_ra_nb_GLK_GRVI_wd4iu_yfwwb_CW`
**Decoded:** `b4$hful_iz_my_TOP_TIER_dw4rf_buddy_XD`

This reads clearly: **"Bashful is my TOP TIER dwarf buddy XD"**.

The substitution makes sense:
*   `y` -> `b`
*   `s` -> `h`
*   `u` -> `f`
*   `f` -> `u`
*   `o` -> `l`

The special characters (`4`, `$`, `_`) remained unchanged, which is typical for simple monoalphabetic substitution ciphers like Atbash when applied only to alphabetic characters.

## Step 4: Formatting the Flag

The challenge required the flag to be in the specific format `NICCTF26{}`. Taking the decoded string, I wrapped it in the format:

**Final Flag:**
`NICCTF26{b4$hful_iz_my_TOP_TIER_dw4rf_buddy_XD}`

## Conclusion

This challenge was a classic example of an Atbash cipher. The key takeaways here are:
1.  **Look for structure:** The underscores hinted at word separation.
2.  **Don't ignore case:** The mixed case was preserved in the cipher, suggesting a direct substitution.
3.  **Automate basic checks:** Having a script to quickly check ROT, Atbash, and other basics saves a lot of manual guessing.

Happy hacking!
