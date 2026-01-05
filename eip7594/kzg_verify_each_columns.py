import hashlib

def sha256(data):
    return hashlib.sha256(data).digest()

def hash_node(left, right):
    return sha256(left + right)

def compute_merkle_root_from_proof(leaf_hash, proof, generalized_index):
    """
    leaf_hash: 검증하려는 commitments의 해시
    proof: inclusion_proof 노드들의 list
    generalized_index: tree index
    """
    current_hash = leaf_hash
    index = generalized_index
    
    for sibling in proof:
        if index % 2 == 1:
            current_hash = hash_node(sibling, current_hash)
        else:
            current_hash = hash_node(current_hash, sibling)
        
        index //= 2
        
    return current_hash

# --- 검증 과정 예시 ---

# 1. 수신한 데이터 (가정)
# 실제로는 ssz_hash_tree_root(kzg_commitments) 함수를 사용해야 합니다.
mock_commitments_root = sha256(b"kzg_commitments_data") # 원래는 48bytes commitments 배열을 hash하여 32byte로 나타냄

# 2. received inclusion_proof (32바이트 hash 리스트)
# tree depth 4라고 가정
mock_inclusion_proof = [sha256(b"inclusion1"), sha256(b"inclusion2"), 
                        sha256(b"inclusion3"), sha256(b"inclusion4")]

# Tree index
GEN_INDEX = 23 # 예시 idx

# 4. 계산 시작
calculated_body_root = compute_merkle_root_from_proof(
    mock_commitments_root, 
    mock_inclusion_proof, 
    GEN_INDEX
)

# 5. 블록 헤더의 body_root와 비교
header_body_root = sha256(b"actual_body_root_from_header") # 실제 헤더값

if calculated_body_root == header_body_root:
    print("검증 성공")
else:
    print("검증 실패")