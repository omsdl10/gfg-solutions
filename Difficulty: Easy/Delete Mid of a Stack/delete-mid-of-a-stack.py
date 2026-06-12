def delete(mid,iteration,st):
    if not st:
        return
    if mid==iteration:
        st.pop()
        return
    top=st.pop()
    delete(mid,iteration-1,st)
    st.append(top)
class Solution:
    def deleteMid(self, stack):
        #code here
        if len(stack)%2==0:
            mid=(len(stack)//2)-1
        else:
            mid=len(stack)//2
        delete(mid,len(stack)-1,stack)
        