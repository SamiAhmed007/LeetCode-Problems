class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        st = set()
        for i in range(len(nums)):
            hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1
        sorted_items = sorted(hash_map.items(), key=lambda kv: (kv[1], kv[0]))
        print(sorted_items)
        sorted_items = sorted_items[len(sorted_items)-k:]
        ans = []
        for ls in sorted_items:
            ans.append(ls[0])
        return ans