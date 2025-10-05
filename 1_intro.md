# Intro to cryptograghy

## Concepts

- Cryptography -> secret writing science
- Cryptanalysis -> science of breaking ciphers
- Cryptology -> math and science of codes and ciphers
- Steganography -> hiding messages in other messages

## Cryptography

The secret writing science. The goal is to ensure that only the intended recipient can read the message.

- Alice and Bob are the good actors

## Cryptographic System

clear text (plain text) -> encryption function + encryption key -> cipher text (encrypted text) -> communication protocol (considered insecure) -> decryption function + decryption key -> clear text

## Classification

### Algorithms

- Hash functions
- Symmetric key algorithms (1 key)
- Asymmetric key algorithms (2 keys)

### Processing

- Stream ciphers (1 bit at a time)
- Block ciphers (n bits at a time)

### Attack types

1. Passive attacks (eavesdropping)
   - The attacker just listens to the communication channel
   - Mitigation: encryption data
   - Passive DNS (DNS MONITORING) -> it will leak metadata even though you are using a vpn
   - Mitigation: use DNS over HTTPS (DoH) or DNS over TLS (DoT)
2. Active attacks (modifying messages)
   - **Reply attacks**: the attacker captures a message and replays it later
   - Mitigation: uuid + timestamp
   - **Impersonation attacks**: the attacker pretends to be someone else
   - Mitigation: digital signatures, certificates
   - **Tampering attacks**: the attacker modifies the message
   - Mitigation: message authentication codes (MACs), digital signatures
   - **DDOS attacks**: the attacker floods the communication channel with traffic
   - Mitigation: rate limiting, firewalls, anti-DDOS services
   - **Injection attacks**: the attacker injects malicious code into the message
   - Mitigation: input validation, sanitization
   - **Man-in-the-middle attacks**: the attacker intercepts the communication between two parties
   - Mitigation: end-to-end encryption, secure communication protocols

### What the attacker knows

- Ciphertext only attack (COA): the attacker only has access to the ciphertext
- Known plaintext attack (KPA): the attacker has access to some pairs of plaintext and ciphertext
- Chosen plaintext attack (CPA): the attacker can choose arbitrary plaintexts to be encrypted and obtain the corresponding ciphertexts
- Chosen ciphertext attack (CCA): the attacker can choose arbitrary ciphertexts to be decrypted and obtain the corresponding plaintexts

### Side channel attacks

- The attacker exploits information leaked during the encryption/decryption process (e.g., timing, power consumption, electromagnetic leaks)

### Zero stuff

- Zero day vulnerabilities:
  - Vulnerabilities that are unknown to the vendor and have no patch available
- Zero knowledge protocols:
  - A method by which one party can prove to another party that they know a value, without revealing any information about the value itself
- Zero Trust security:
  - The concept of having no inherent trust in any user or system, and requiring strict verification and authentication for every access request
- Zero click attacks:
  - Attacks that do not require any user interaction to be successful (e.g., drive-by downloads, watering hole attacks)

### Cybersecurity Objectives

- Confidentiality: Ensuring that information is only accessible to those who are authorized to access it.
- Availability: Ensuring that information and systems are accessible and usable when needed.
- Authentication: The process of verifying the identity of a user or system.
- Non-repudiation: The ability to prove that a user or system performed a specific action, preventing them from denying it later.
- Data integrity: The assurance that data has not been altered or tampered with during transmission or storage.

### Threat Modeling

- Is a structured approach to identifying and assessing potential threats to a system or application.

## Mathematical Background

- XOR

plain_text XOR key = cipher_text
cipher_text XOR key = plain_text

- Log x

we use log base 2 to analyze the complexity of password cracking. Total number of possible passwords = 2^n, where n is the number of bits in the password. To find n, we use log base 2:

- Entropy
- Complexity
- Big number arithmetic
- Prime numbers
