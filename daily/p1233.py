from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        result = []
        folder_tree = {}
        folder.sort(key=len)
        for f in folder:
            sub_folder_list = f.split("/")[1:]
            # print(folder_tree)

            is_sub = False
            check_tree = folder_tree.copy()
            for s_f in sub_folder_list:
                print("check_tree ", check_tree)
                if s_f in check_tree:
                    print(s_f)
                    print(check_tree[s_f])
                    if check_tree[s_f] == {}:
                        # 空的
                        # print(f)
                        is_sub = True
                        break
                    else:
                        check_tree = check_tree[s_f]
                else:
                    break
            if not is_sub:
                result.append(f)
                tmp = folder_tree
                for s_f in sub_folder_list:
                    if s_f not in tmp:
                        tmp[s_f] = {}
                    tmp = tmp[s_f]
                print(folder_tree)

        return result


folder = ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]
a = Solution()
print(a.removeSubfolders(folder=folder))
