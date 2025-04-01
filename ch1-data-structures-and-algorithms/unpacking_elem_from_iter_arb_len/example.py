from statistics import mean

def drop_first_last(grades):
	first, *middle, last = grades
	return mean(middle)

grades = (22, 20, 30, 40, 50, 21)

avg_grd = drop_first_last(grades)
print(avg_grd)

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(name)
print(email)
print(phone_numbers)

*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing)
print(current)