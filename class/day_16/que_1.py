nums = [10,12,14,15,18,21,22,25,28,30,2,-10]
nums.sort()

q1 = 0.25 * (len(nums) - 1)
q3 = 0.75 * (len(nums) - 1)
q1 = int(q1)
q3 = int(q3)

l1 = nums[q1] + (nums[q1 + 1] - nums[q1]) * (0.25 * (len(nums) - 1) - q1)
l3 = nums[q3] + (nums[q3 + 1] - nums[q3]) * (0.75 * (len(nums) - 1) - q3)

print("Q1: ", nums[q1], "Q3: ", nums[q3])
print("Q1: ", l1, "Q3: ", l3)
print("IQR: ", l3 - l1)

uv = l3 + 1.5 * (l3 - l1)
lv = l1 - 1.5 * (l3 - l1)
print("Upper Value: ", uv)
print("Lower Value: ", lv)

outliers = []
for i in range(len(nums)):
    if nums[i] > uv or nums[i] < lv:
        outliers.append(nums[i])
print("Outliers: ", outliers)


# The above code calculates the first and third quartiles (Q1 and Q3) of a sorted list of numbers,
# and then uses these quartiles to calculate the interquartile range (IQR).
# It also identifies any outliers in the data based on the IQR method.
# The code uses linear interpolation to calculate the quartiles, which is a method of estimating values