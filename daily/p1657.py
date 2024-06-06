# Example 1:

# Input: word1 = "abc", word2 = "bca"
# Output: true
# Explanation: You can attain word2 from word1 in 2 operations.
# Apply Operation 1: "abc" -> "acb"
# Apply Operation 1: "acb" -> "bca"
# Example 2:

# Input: word1 = "a", word2 = "aa"
# Output: false
# Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
# Example 3:

# Input: word1 = "cabbba", word2 = "abbccc"
# Output: true
# Explanation: You can attain word2 from word1 in 3 operations.
# Apply Operation 1: "cabbba" -> "caabbb"
# Apply Operation 2: "caabbb" -> "baaccc"
# Apply Operation 2: "baaccc" -> "abbccc"

# word1 = "cabbba", word2 = "abbccc"
# word1 = "cb", word2 = "bc"

from collections import Counter


class Solution:
    def operation2(self, word1: str, word2: str):
        pointer = 0
        memory = set()
        word2_c = Counter(word2)
        word1_c = Counter(word1)
        for key in word2_c:
            if key not in word1_c:
                return None, None

            if word1_c[key] != word2_c[key]:
                this_k = None
                for k, v in word1_c.items():
                    if v == word2_c[key] and k not in memory:
                        this_k = k
                        break
                if not this_k:
                    return None, None

                word1 = word1.replace(key, "9")  # 9: tmp
                word1 = word1.replace(this_k, key)
                word1 = word1.replace("9", this_k)

                tmp = word1_c[key]
                word1_c[key] = word2_c[key]
                word1_c[this_k] = tmp

            memory.add(key)

        return word1, word2

    def operation1(self, word1: str, word2: str):
        pointer = 0
        memory = {}
        while pointer < len(word1):
            if word1[pointer] != word2[pointer]:
                if word1[pointer] in memory:
                    # if memory[word1[pointer]][0] == word2[pointer]:
                    tmp_pop = word1[pointer]
                    change_pointer = memory[word1[pointer]][1]
                    tmp = word1[change_pointer]
                    word1[change_pointer] = word1[pointer]
                    word1[pointer] = tmp
                    memory.pop(tmp_pop)
                else:
                    memory[word2[pointer]] = [word1[pointer], pointer]
            pointer += 1
        return "".join(word1), "".join(word2)

    def pop_same(self, word1: str, word2: str):
        tmp = [i for i, w in enumerate(zip(word1, word2)) if w[0] == w[1]]
        while tmp:
            this_pop = tmp.pop()
            word1.pop(this_pop)
            word2.pop(this_pop)
        return "".join(word1), "".join(word2)

    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        word1, word2 = self.operation2(word1, word2)
        if not word1:
            return False

        # while word1 or word2:
        #     word1, word2 = self.operation1(list(word1), list(word2))
        #     print(123)
        return True
        # if not (new_word := self.operation2(word1, word2)):
        #     return False

        # pass


a = Solution()
word1 = "abc"
word2 = "bca"

# word1 = "cabbbc"
# word2 = "abbccc"

word1 = "kmihff"
word2 = "kffmmi"
a.closeStrings(word1, word2)
