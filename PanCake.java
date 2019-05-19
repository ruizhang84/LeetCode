class Solution {
    private class Node implements Comparable<Node>
    {
        public int index;
        public int val;
        public Node(int i, int v){
            index = i;
            val = v;
        }
        
        @Override
        public int compareTo (Node other){
            return other.val - val;
        }
    }
    
    public List<Integer> pancakeSort(int[] A) {
        List<Integer> ans = new ArrayList<>();
        
        Node[] B = new Node[A.length];
        for (int i = 0; i < A.length; i++){
            B[i] = new Node(i, A[i]);
        }
        
        Arrays.sort(B);
        for (int i = 0; i < B.length; i++){
            if (B[i].index > 0){
                ans.add(B[i].index);
                ans.add(B[i].index+1);   
            }
            for (int j = 0; j < B.length; j++){
                if (B[j].index < B[i].index)
                    B[j].index++;
            }
        }

        return ans;
    }
    
}
