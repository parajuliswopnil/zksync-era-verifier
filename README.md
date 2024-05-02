# `zksync-era-verifier`

A verifier for ZkSync-Era ethereum proofs. This crate provides a way for deserializing the proofs
that ZkSync-Era post on ethereum, the default verification key and a function to check if the proof
is correct:

```rust
    use tests::ProofData;
    use zksync_era_verifier::{default_eth_vk, deserialize_eth_proof, verify, ZkSyncEthProof};

    let proof_data = serde_json::from_reader::<_, ProofData>(
        std::fs::File::open("./resources/proof.json").unwrap(),
    )
    .unwrap();

    let mut eth_proof: ZkSyncEthProof =
        deserialize_eth_proof(&proof_data.proof().collect::<Vec<_>>()).unwrap();
    eth_proof.inputs = proof_data.inputs();

    let vk = default_eth_vk();

    assert!(verify(&vk, &eth_proof).unwrap());
```

## Develop

This project uses [`cargo-make`](https://github.com/sagiegurari/cargo-make) to define
tasks and checks. Install this tool simply by `cargo install cargo-make` and run

```sh
cargo make ci
```

to run all CI's steps. You can also use `makers ci` and bypass `cargo` wrapper.

Another useful defined task is `coverage` that executes tests and compute code
coverage file `lcov.info`.

## License

These crates are released under the [APACHE 2.0 license](LICENSE-APACHE2)