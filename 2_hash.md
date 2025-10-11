# Hash functions

- What is the bit strength of a password with 20 chars having 156 unique values?

20 -> 8 bits per char -> 160 bits
2^160 = number of unique values
log2(156) = 7.285 -> 8 bits per char

- What is the bit strength of a password with 20 chars each char having 5 unique values?

1 -> 8 bits per char ->2^8
1 char -> 5 different values -> log2(5) = 3 aprox -> 2^3 (at the exam we should use the decimal number, not the aprox)

2^3 *2^3*2^3....20 times = 2^60 -> 60 bits strength

## Mathematical Background

PRNG vs TRNG

## Protocols

Types of protocols:

- arbitrated -> with a trusted third party
- adjudicated -> 2 lower-level sub-protocols
- self-enforcing -> no third party, we trust the participants

## Hash Functions

- SHA-256
- SHA-3
- MD5 (not secure)

### Password-Based Key Derivation Function (PBKDF)

- a cryptographic algorithm that derives a key from a password
- **Input**: It takes a password, a salt (random value), and an iteration count (number of times the hashing function is applied).
- **Iteration**: The function applies a hashing function (like SHA-256) multiple times to the combination of the password and salt. This process is known as key stretching.
- **Salt**: The salt is a random value added to the password before hashing. It ensures that even if two users have the same password, their derived keys will be different.
- **Output**: The output is a derived key that can be used for encryption or authentication purposes.

### Crypto

- Data Integrity: used to verify that data (e.g, transactions) has not been altered.
- Mining in Proof of Work (PoW): miners compete to find a hash value that meets certain criteria, which requires significant computational effort.
- Address Generations: A user's public key is hashed to create a shorter, fixed-length address that is easier to share and use in transactions.
- Digital Signatures: Hash functions are used in the creation and verification of digital signatures, ensuring the authenticity and integrity of messages.
- Merkle Derivation and Block Validation: help derive private keys from a master seed, allowing users to manage multiple addresses securely.
- Proof of Stake (PoS): Validators are chosen to create new blocks based on the amount of cryptocurrency they hold and are willing to "stake" as collateral.

### Proof of Stake (PoS)

- Goal: Achieve blockchain consensus without energy-intensive computation (unlike Proof of Work).
- Stake and validators: Participants lock up a stake (tokens) to become validators. Selection to propose/validate blocks is pseudo-random and weighted by stake.
- Block proposal and attestation: One validator proposes a block; others attest (vote) on its validity. Enough attestations finalize the block per the chain’s rules.
- Rewards: Validators earn protocol rewards and transaction fees for proposing and correctly attesting to blocks.
- Slashing and penalties: Misbehavior (e.g., double-signing, equivocation) or prolonged downtime can lead to loss of stake (slashing) or reduced rewards.
- Finality: Many PoS chains add probabilistic or economic finality via checkpoints/epochs (e.g., Ethereum’s Casper FFG), making finalized blocks very costly to revert.
- Security model: Attacks require acquiring and risking a large share of stake. Honest majority-by-stake is assumed; penalties deter attacks.
- Pros vs PoW: Far lower energy use, typically faster confirmation/finality, lower hardware barriers. Risks include stake centralization, long-range attacks (handled via weak subjectivity), and governance concentration.
