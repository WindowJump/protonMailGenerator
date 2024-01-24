# Test task solution for the Con10T Labs
There are several things that I fixed in the code:

  1. Fixed hotkeys.
  2. Used a currently (as of 24.01.2024) unblocked temporary email for verification on Proton.
  3. Utilized pyperclip to work with the clipboard instead of the kernel, allowing this code to be used not only on Windows.
  4. Adhered to Python programming principles, making the code more readable, easier to understand, and also removing those strange Python-incompatible signs ';'.
  5. Added a user function so that they can specify whether they want to use a password or username; if nothing is specified, random values are used.
  6. Transformed the generator into a class for easier import and further modification of the code.

You can compare old code(chromegen.py) to the new one(generator.py)

# How to run
  To run this code localy you need to install following packages:
    1. pyperclip
    2. pyautogui
