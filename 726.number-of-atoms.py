#
# @lc app=leetcode id=726 lang=python3
#
# [726] Number of Atoms
#

# @lc code=start
from collections import Counter


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        formula = 'K435(HO(HHe238Be26He)9)34'
        cnt = len(formula)
        i = 0
        stack = [collections.Counter()]
        
        while (cnt > i):
            s = formula[i]

            if s == '(':
                stack.append(collections.Counter())
                i += 1
            elif s == ')':
                cur_counter = stack.pop()

                i += 1
                start  = i

                while i < cnt and formula[i].isdigit():
                    i +=1
                
                multiplier = int(formula[start:i]) if formula[start:i] else 1

                for atom in cur_counter:
                    count = cur_counter[atom]
                    stack[-1][atom] += count * multiplier
            else:
                atom = s
                i += 1
                start = i

                while i < cnt and formula[i].islower():
                    i += 1
                
                atom += formula[start:i]

                start = i

                while i < cnt and formula[i].isdigit():
                    i += 1

                count = int(formula[start:i]) if formula[start:i] else 1

                stack[-1][atom] += count

        ans = ''
        counter = stack[-1]

        for atom in sorted(counter):
            ans += atom
            if counter[atom] > 1:
                ans += str(counter[atom])

        return ans
        
# @lc code=end

