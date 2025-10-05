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
