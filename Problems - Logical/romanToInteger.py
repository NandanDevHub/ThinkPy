class Solution(object):
    def romanToInt(self, s):
        romans = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0
        for x in range(len(s) - 1):
            current_val = romans[s[x]]
            next_val = romans[s[x + 1]]

            if current_val < next_val:
                total = total - current_val
            else:
                total = total + current_val
        total = total + romans[s[-1]]
        return total
    
if __name__ == "__main__":
    solution = Solution()
    roman_string = input("Enter the Roman Numeral:")
    result = solution.romanToInt(roman_string)
    print(f"The Integer value is {result}")