class Solution:
    def get_one_loc(self, version_list):
        result = []
        for i, ele in enumerate(version_list):
            if int(ele) != 0:
                result.append(i)
        return result

    def compareVersion(self, version1: str, version2: str) -> int:
        version_list1 = version1.split(".")
        version_list2 = version2.split(".")
        oneloc1, oneloc2 = map(self.get_one_loc, (version_list1, version_list2))

        pointer = 0
        if oneloc1 and not oneloc2:
            return 1
        elif not oneloc1 and oneloc2:
            return -1

        while pointer < len(oneloc1) and pointer < len(oneloc2):
            if oneloc1[pointer] < oneloc2[pointer]:
                return 1
            elif oneloc1[pointer] > oneloc2[pointer]:
                return -1
            else:
                if int(version_list1[oneloc1[pointer]]) > int(version_list2[oneloc2[pointer]]):
                    return 1
                elif int(version_list1[oneloc1[pointer]]) < int(version_list2[oneloc2[pointer]]):
                    return -1

            pointer += 1

            if pointer == len(oneloc1) and pointer == len(oneloc2):
                return 0
            else:
                if pointer == len(oneloc1):
                    return -1
                elif pointer == len(oneloc2):
                    return 1

        return 0


a = Solution()
version1 = "1"
version2 = "0"
print(a.compareVersion(version1=version1, version2=version2))
