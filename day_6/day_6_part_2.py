import math

test_input = """Time: 71530
Distance: 940200"""

input = """Time: 47847467
Distance: 207139412091014"""

time_line, dist_line = input.split("\n")
times = list(map(int, time_line.split(": ")[1].split()))
dists = list(map(int, dist_line.split(": ")[1].split()))
time_dists = zip(times, dists)

values = []
for time, dist in time_dists:
    halfway_point = int(time / 2) + 1
    for i in range(halfway_point):
        if i * (time - i) > dist:
            break
    value = (halfway_point - i) * 2
    if time % 2 == 0:
        value -= 1
    values.append(value) 
print(math.prod(values))
# Answer: 38,220,708 - Correct