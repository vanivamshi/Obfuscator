# Obfuscator

Original.py - contains original program

Mutator.py - contains obfuscated code

Code uses the following,

1) Advanced Mutation Techniques - 
(a) Control Flow Alteration: Replaces if statements with if True: pass to add redundant checks,
(b) Dynamic Code Generation: Encrypts the original code and uses exec to execute the decrypted code,
(c) Code Encryption and Decryption: Encrypts the original code using Base64 encoding and decrypts it at runtime

2) Function and Variable Name Obfuscation - Randomize Names: Generates random names for functions and variables using generate_random_name

3) Code Injection and Insertion - Dummy Code Insertion: Adds a dummy print statement to the end of the code

4) Control Flow Flattening - Flatten Control Flow: Inserts if True: pass to flatten control flow in the code

5) Variable and Function Transformation - 
(a) Inline Functions: Function inlining is not explicitly shown but can be added as needed,
(b) Function Splitting: More complex splitting techniques can be incorporated as needed

6) Dynamic Runtime Alteration - 
(a) Code Swapping: This example does not directly swap code but demonstrates dynamic execution with exec,
(b) Self-Modifying Code: The script itself does not modify at runtime but could be extended to include such functionality

7) Integration with Obfuscation Tools - Use Obfuscation Libraries: The script does not directly use external tools but could be extended to integrate with tools like PyArmor for additional obfuscation.
