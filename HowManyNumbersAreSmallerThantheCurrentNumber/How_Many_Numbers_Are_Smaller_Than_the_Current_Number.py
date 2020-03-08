from typing import Type


def smallerNumbersThanCurrent(nums):
    for num in nums:
        if (type(num) != int):
            raise TypeError("Input must be an integer")

    if len(nums) == 0:
        raise IndexError("List is empty")
    container_for_nums = nums.copy()
    solution = []

    for num in nums:
        if (num == max(container_for_nums) and container_for_nums.count(num) == 1):
            container_for_nums.pop(container_for_nums.index(num))
            solution.append(len(container_for_nums))

        elif (num == max(container_for_nums) and container_for_nums.count(num) != 1):
            solution.append(len(container_for_nums) -
                            container_for_nums.count(num))
            list(filter((num).__ne__, container_for_nums))

        elif num == min(container_for_nums):
            solution.append(0)

        else:
            to_append = filter(lambda x: x < num, container_for_nums)
            solution.append(len(list(to_append)))

    return solution
