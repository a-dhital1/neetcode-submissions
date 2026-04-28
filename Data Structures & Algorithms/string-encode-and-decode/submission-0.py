class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_parts = []

        for string in strs:
            prefix = f"{len(string):4}"

            encoded_parts.append(prefix + string)

        return "".join(encoded_parts)



    def decode(self, s: str) -> List[str]:
        decoded_strings = []
        index = 0
        total_length = len(s)

        while (index < total_length):
            string_length = int(s[index:index + 4])

            index += 4

            decoded_string = s[index:index + string_length]
            decoded_strings.append(decoded_string)

            index += string_length

        return decoded_strings 
