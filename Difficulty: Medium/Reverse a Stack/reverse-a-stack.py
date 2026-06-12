def insert(item,st):
    if not st:
        st.append(item)
        return
    top=st.pop()
    insert(item,st)
    st.append(top)
class Solution:
    def reverseStack(self, st):
        if not st:
            return
        top=st.pop()
        self.reverseStack(st)
        insert(top,st)
    