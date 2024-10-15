class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        # heap = []
        # heappush(heap, (nums1[0] + nums2[0], 0, 0))
        # nums1 = nums1[:k]
        # nums2 = nums2[:k]
        # smallest = []

        # for _ in range(k):
        #     print(heap, smallest)
        #     if heap: 
        #         val, i, j = heappop(heap)
        #         smallest.append([nums1[i], nums2[j]])

        #         if j == 0 and i + 1 < len(nums1):
        #             heappush(heap, (nums1[i + 1] + nums2[0], i + 1, 0))
                
        #         if j + 1 < len(nums2):
        #             heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

                
        
        # return smallest

        # if not nums1 or not nums2 or k == 0:
        #     return []
        
        # # Min-heap to store the smallest pairs
        # min_heap = []
        
        # # Initialize the heap with the first element from nums2 paired with all elements from nums1
        # for i in range(min(k, len(nums1))):  # Only take up to k elements from nums1
        #     heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))  # (sum, index in nums1, index in nums2)
        
        # result = []
        
        # # Extract the smallest pairs from the heap
        # while k > 0 and min_heap:
        #     current_sum, i, j = heapq.heappop(min_heap)
        #     result.append([nums1[i], nums2[j]])
        #     k -= 1
            
        #     # If there are more elements in nums2 to pair with nums1[i], add the next pair (nums1[i], nums2[j+1])
        #     if j + 1 < len(nums2):
        #         heapq.heappush(min_heap, (nums1[i] + nums2[j+1], i, j+1))
        
        # return result
        l = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                
                if len(l)<k:
                    heapq.heappush(l, [-(nums1[i]+nums2[j]),[nums1[i], nums2[j]]])
                elif - l[0][0]> nums1[i]+nums2[j]:
                    print(heapq.heappop(l))
                    heapq.heappush(l, [-(nums1[i]+nums2[j]),[nums1[i], nums2[j]]])
                else:
                    break

        ans = []
        for i in range(k):
            ls = heapq.heappop(l)
            ans.append(ls[1])
        return ans
