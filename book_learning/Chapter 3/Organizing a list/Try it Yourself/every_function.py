transportation = ["trucks", "cars", "horses", "trains", "airplanes", "walking", "bicycle"]
print(transportation[0])
print(transportation[3].title())
print(transportation[-2])
print(f"I love to drive {transportation[1].title()} over all other types!")

transportation[0] = "taxis"
print(transportation)

transportation.append("trucks")
print(transportation)

transportation.insert(4, "big rigs")
print(transportation)

del transportation[0]
print(transportation)

print(transportation.pop())

print(transportation.pop(4))

transportation.remove("horses")

print(sorted(transportation))
print(sorted(transportation, reverse=True))

transportation.sort()
print(transportation)

transportation.sort(reverse=True)
print(transportation)

transportation.reverse()
print(transportation)

print(len(transportation))