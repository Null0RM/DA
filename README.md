# DA
Study Ethereum DA

# EIP-4844
- kzg commitment


# EIP-7594
Starting from data unavailability attack risk on fraud proof and lack of Data availability on light nodes
- on roadmap Fusaka
- enables 8x more data processing(theoretically)

**countermeasure**
- Erasure coding
    * 1d-reed-solomon (eip-7594)
        - good: simple struture
        - bad: size of fraud proof gets bigger
    * 2d-reed-solomon (full-danksharding)
        - good: small size of fraud proof
        - bad: complex structure
> refs
> [ethereum research]("https://github.com/ethereum/research/wiki/a-note-on-data-availability-and-erasure-coding")

- Sampling
Not recovering missing data, just checking data availability.