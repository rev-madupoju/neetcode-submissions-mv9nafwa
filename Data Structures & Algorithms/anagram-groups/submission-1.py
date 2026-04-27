class Solution:
    def groupAnagrams(self, A: list[str]) -> list[list[str]]:
        """
        One-shot solution, without isAnagram() helper function
        """
        groups = dict[str, list[str]]()

        for word in A:
            found_group = False

            for key in groups.keys():
                if len(key) != len(word):
                    continue

                counts = [0] * 26

                for i in range(len(word)):
                    counts[ord(key[i]) - ord("a")] += 1
                    counts[ord(word[i]) - ord("a")] -= 1

                for c in counts:
                    if c != 0:
                        break
                else:
                    found_group = True
                    groups[key].append(word)
                    break

            if not found_group:
                groups[word] = [word]

        return list(groups.values())

