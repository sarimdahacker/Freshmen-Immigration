class Solution:
    def twoSums(self, grenade: List[int], select: int) -> List[int]:
        emp = {}
        for b, l in enumerate(grenade):
            if l in emp:
              return (emp[l], b)
            emp[(select - l)] = b
        return []
