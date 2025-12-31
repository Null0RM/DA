from reedsolo import RSCodec

''' reed sol 기초 사용법 '''
''' GF(2^8) 기반이라서, 기본적으로 1byte = 1 symbol '''
rsc = RSCodec(10)
# parity symbol 10개 추가 
# 10 = 1/2만큼 복구가능(5개 복구 가능)
data = b"hello ethereum"
encoded = rsc.encode(data)
print(encoded) # bytearray(b'hello ethereum\xf6\x12\x120\x85\xb9\x0e\xfc\xb8\xe1')

# encoded array에 오류 발생
corrupted = bytearray(encoded)
corrupted[0] ^= 0xFF
corrupted[1] ^= 0xFF
corrupted[2] ^= 0xFF
corrupted[3] ^= 0xFF
corrupted[4] ^= 0xFF
# corrupted[5] ^= 0xFF # 에러발생

''' 복원 '''
decoded, _, _ = rsc.decode(corrupted)
print(decoded) # bytearray(b'hello ethereum')

''' 오류 위치를 알고있는 경우 두 배 효율 '''
corrupted[5] ^= 0xFF
corrupted[6] ^= 0xFF
corrupted[7] ^= 0xFF
corrupted[8] ^= 0xFF
corrupted[9] ^= 0xFF
# corrupted[10] ^= 0xFF # 이거까지는 안됨

decoded, _, _ = rsc.decode(corrupted, erase_pos=[0,1,2,3,4,5,6,7,8,9])
print(decoded) # bytearray(b'hello ethereum')

''' DA/sharding 관점 '''
k = 16 # 원본데이터 조각 개수 (하나의 blob, block body, row단위 데이터 등이 될 수 있음)
parity = 16 # polynomial interpolation을 통한 추가 parity 조각
rsc = RSCodec(parity) 

data = bytes(range(k))
extended = rsc.encode(data)
print(extended) # bytearray(b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x17\xc1\x1f\x84\xf4S\x19\xa5\xef\x87\x93\xa1K\xaaW\xba')
# data + parity -> n=32
# n=32 중에서, k(16)개의 임의의 data또는 parity조각만 있어도 전체 data를 복원 가능
