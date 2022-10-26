func checkSubarraySum(nums []int, k int) bool {
    lookup := make(map[int]int)
    lookup[0] = -1 
    
    cursum := 0 
    for i, val := range nums{
        cursum += val
        rem := cursum % k 
        if idx, found := lookup[rem]; found{
            if i - idx > 1{
                return true
            }
        }else{
            lookup[rem] = i
        }
        
    }
    return false
}