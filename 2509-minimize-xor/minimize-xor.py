class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        set_bits = bin(num2).count('1')
        val = bin(num1)[2:]
        result = ['0'] * len(val)

        for i in range(len(val)):
            if set_bits and val[i] == '1':
                result[i] = '1'
                set_bits -= 1
            else:
                result[i] = '0'
        
        curr_bit = 1
        result = ['0'] * (32 - len(val)) + result

        for _ in range(1, set_bits+1):
            while result[-curr_bit] == '1':
                curr_bit += 1
            result[-curr_bit] = '1'
            curr_bit += 1
           
        return int(''.join(result), 2)