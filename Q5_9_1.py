mountain_in_japan = {'fuji': 3776, 'kitadake': 3139,'okuhodakadake' : 3139, 'dummy': 0}

mountsin_in_japan_sorted = sorted(muntain_in_japan.items(),key=lambda x: x[1], reverse=True)

print(mountsin_in_japan_sorted)

