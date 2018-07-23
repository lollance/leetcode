class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        maxN = len(nums)-1
        for i in range(len(nums)):
            if nums[i] > nums[maxN]:
                maxN = i
        
        tree = TreeNode(nums[maxN])
        left = []
        right = []
        for i in range(maxN):
            left.append(nums[i])
            
        for i in range(maxN+1,len(nums)):
            right.append(nums[i])
    
        if left != []:
            tree.left = self.constructMaximumBinaryTree(left)
        if right != []:
            tree.right = self.constructMaximumBinaryTree(right)
        
        return tree
