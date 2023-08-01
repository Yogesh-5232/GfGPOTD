def getMaxArea(self,arr):
     st = []
     res = 0
     for i in range(len(arr)):
        while st and arr[st[-1]]>= arr[i]:
            tp = st[-1]
            st.pop()
            curr_width = (i-st[-1]-1) if st else i
            res = max(res,curr_width* arr[tp])
        st.append(i)
     while st:
        tp = st[-1]
        st.pop()
        curr_width = (len(arr)- st[-1]-1) if st else len(arr)
        res = max(res,curr_width*arr[tp])
     return res
