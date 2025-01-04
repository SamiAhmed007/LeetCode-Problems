class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==1:
            return 1
        i = 0
        j = i
        st = set()
        # cnt = 1
        max_cnt = 0
        while(j<len(s)):
            if s[j] not in st:
                st.add(s[j])
                j+=1
            else:
                max_cnt = max(len(st), max_cnt)
                st.remove(s[i])
                i+=1


        return max(len(st), max_cnt)

















        # sett=set();
        # longest=0;
        # l=0;
        # for j in range(len(s)):
        #     while(s[j] in sett):
        #         print(sett)
        #         sett.remove(s[l]);
        #         l+=1
        #     w=j-l+1;
        #     sett.add(s[j]);
        #     longest=max(longest,w);
        # return longest

        # # sett=set();
        # longest=0;
        # l=0;
        # for j in range(len(s)):
        #     while(s[j] in sett):
        #         sett.remove(s[l]);
        #         l+=1
        #         # print("after remove",sett)
        #     w=j-l+1;
        #     sett.add(s[j]);
        #     print(sett)
        #     longest=max(longest,w);
        # return longest