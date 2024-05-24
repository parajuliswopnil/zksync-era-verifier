//! A simple program to be proven inside the zkVM.

#![no_main]
sp1_zkvm::entrypoint!(main);

use tests::ProofData;
use verifier::verify;
use verifier::ZkSyncEthProof;
use verifier::deserialize_eth_proof;
use verifier::default_eth_vk;

pub fn main() {
    // NOTE: values of n larger than 186 will overflow the u128 type,
    // resulting in output that doesn't match fibonacci sequence.
    // However, the resulting proof will still be valid!
    let n = sp1_zkvm::io::read::<u32>();

    let proof_data = serde_json::from_reader::<_, ProofData>(
        std::fs::File::open("/Users/swopnilparajuli/workspace/cedro/zksync-era-verifier/verifier/resources/proof.json").
        unwrap(), 
    ).unwrap();

    let mut eth_proof: ZkSyncEthProof = deserialize_eth_proof(&proof_data.proof().collect::<Vec<_>>()).unwrap();
    eth_proof.inputs = proof_data.inputs();

    let vk = default_eth_vk();

    assert!(verify(&vk, &eth_proof).unwrap());
}
