from typing import List
import pytest

class Solution:
    def encode(self, strs: List[str]) -> str:
        encode_str=''
        for s in strs:
            encode_str += f'#{str(len(s))}#{s}'
        return encode_str

    def decode(self, s: str) -> List[str]:
        decode_str_list = []

        index=0      
        n = len(s)
        while index<n:

            if s[index]=='#':
                index += 1
                
                s_len=''
                while s[index] != '#':
                    s_len += s[index]
                    index += 1
                s_len=int(s_len)
                index += 1
                
                w=s[index:index+s_len]
                index += s_len
                decode_str_list.append(w)
                    
        return decode_str_list

@pytest.mark.parametrize(
    "strs",
    [
        ["neet", "code", "love", "you"],
        ["we", "say", ":", "yes"],
        [],
    ],
)
def test_encode_decode(strs):
    s = Solution()
    encoded = s.encode(strs)
    decoded = s.decode(encoded)
    assert decoded == strs

