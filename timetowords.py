def timeInWords(h, m):
    nums = ["zero","one","two","three","four","five","six","seven","eight","nine",
            "ten","eleven","twelve","thirteen","fourteen","quarter","sixteen",
            "seventeen","eighteen","nineteen","twenty","twenty one","twenty two",
            "twenty three","twenty four","twenty five","twenty six","twenty seven",
            "twenty eight","twenty nine","half"]

    if m == 0:
        return nums[h] + " o' clock"
    elif m == 15:
        return "quarter past " + nums[h]
    elif m == 30:
        return "half past " + nums[h]
    elif m == 45:
        return "quarter to " + nums[h+1]
    elif m < 30:
        if m == 1:
            return "one minute past " + nums[h]
        else:
            return nums[m] + " minutes past " + nums[h]
    else:
        m = 60 - m
        if m == 1:
            return "one minute to " + nums[h+1]
        else:
            return nums[m] + " minutes to " + nums[h+1]


# Input
h = int(input())
m = int(input())

# Output
print(timeInWords(h, m))