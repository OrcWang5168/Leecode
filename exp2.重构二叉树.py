class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree(preorder=None, inorder=None):
    index = {val: i for i,val in enumerate(inorder)}
    def build(preRootorder,inL,inR):
        if inL>inR:
            return
        rootValue = preorder[preRootorder]
        root = TreeNode(rootValue)
        print(root.val)
        leftsize=index[rootValue]-inL   #当前点减前一数组的第一个的下标是前一个数组的长度
        root.left = build(preRootorder+1,inL,index[rootValue]-1)   #一直左子树递归左边界不会变
        root.right = build(preRootorder+1+leftsize,index[rootValue]+1,inR)
        return root
    return build(0,0,len(inorder)-1)
#总结:这种方法是通过中序遍历中的左右边界来进行递归建树，思想比较新





a = buildTree(preorder=[0,1,3,7,8,4,9,2,5,6], inorder=[7,3,8,1,9,4,0,5,2,6])


#方法二



















