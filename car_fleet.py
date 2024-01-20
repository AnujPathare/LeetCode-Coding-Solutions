class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:

        # cars = sorted(list(zip(position, speed)), key = lambda x: x[0], reverse = True)
        # stack = []

        # for position, speed in cars:
        #     time = (target-position)/speed
        #     stack.append(time)
        #     if len(stack) > 1 and stack[-1] <= stack[-2]:
        #         stack.pop()
        # return len(stack)

        fleet = 0
        prev_time = 0

        for position, speed in sorted(list(zip(position, speed)), reverse = True):
            time = (target-position)/speed
            if prev_time < time:
                fleet += 1
                prev_time = time
        return fleet

obj = Solution()

target = 10
position = [3]
speed = [3]

print(obj.carFleet(target, position, speed))