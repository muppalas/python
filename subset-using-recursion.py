def find_subsets(nums):
    def nsub(start, current):
        # adds current subset to output
        subsets.append(current[:])
        
        for i in range(start, len(nums)):
            # Include the element nums[i] in the current subset
            current.append(nums[i])
            # Recur with the next element
            nsub(i + 1, current)
            # Exclude the element nums[i] from the current subset (backtrack)
            current.pop()
    
    subsets = []
    nsub(0, [])
    return subsets

#get input
def main():
    user_input = input("Enter numbers or words separated using spaces: ")
    
    # seperate into a list
    items = user_input.split()
    
    result = find_subsets(items)
    
    print("All subsets:")
    for subset in result:
        print(subset)

# Run the main function
if __name__ == "__main__":
    main()
