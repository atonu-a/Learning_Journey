nums = list(range(1,11))
print(nums)

result = { i: "Even" if i%2==0 else "Odd" for i in nums
}
print(result)

for k, v in result.items():
    print(f"{k} : {v}")
    