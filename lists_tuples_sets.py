# ******
# Lists
# ******
courses = ["History", "Math", "Physics", "CompSci"]
courses_2 = ["Art", "Education"]

# printing
print(len(courses))

# indexing
print(courses[0])  # first item
print(courses[-1])  # last item
print(courses[:2])  # all values from beginning up to but not including index 2
print(courses[2:])  # all values from index 2 until the end

print(f"The index of Math is: {courses.index('Math')}")
print("Art" in courses)  # determines if item is in the list


# adding
courses.append("Art")  # Append Art to the end of the list
courses.insert(3, "Art")  # Add Art to index 3
courses.extend(courses_2)  # use the courses_2 to extend courses - appending on the end
print(courses)

# removing items
courses.remove("Math")  # removes a specific item from the list
print(courses)
popped = courses.pop()  # removes the last item in the list
print(popped)

# sorting & reversing
courses.sort(reverse=True)  # sorting in-place
print(courses)

sorted_courses = sorted(
    courses
)  # the sorted keyword returns a sorted version of the input
print(sorted_courses)

# min, max,
nums = [1, 2, 3, 4, 5].sort(reverse=True)
print(nums)

# ENUMERATION
for (
    index,
    course,
) in enumerate(courses, start=1):
    print(index, course)

# Joining and splitting
course_str = ", ".join(
    courses
)  # returns a string version of the list, separated by ', '
print(course_str)

new_list = course_str.split(" - ")  # t
print(new_list)

# ************************************
# tuples
# immutable - we cannot modify tuples
# ************************************

# Illustration with lists
list_1 = ["History", "Math", "Physics", "CompSci"]
list_2 = list_1

list_1[0] = "Art"

print(list_1)
print(list_2)  # Notice that list_2 also got changed even though we only updated list_1


tuple_1 = ("History", "Math", "Physics", "CompSci")
tuple_2 = tuple_1

# tuple_1[0] = 'Art'  # this will throw an error because tuples don't allow item assignment


# ************************************
# Sets
# Unordered and contains no duplicates
# ************************************
cs_courses = {"History", "Math", "Physics", "CompSci"}
art_courses = {"History", "Math", "Art", "Design"}

print(f"union:  {cs_courses.union(art_courses)}")   # union
print(f"intersection:  {cs_courses.intersection(art_courses)}") # intersection
print(f"difference:  {cs_courses.difference(art_courses)}") # difference
print(cs_courses)

print("Math" in cs_courses)  # check for an element in a set
