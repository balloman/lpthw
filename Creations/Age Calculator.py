print "Welcome to my Age Calculator, Calculate your age for free, if for some weird reason you don't already know it"

print "What year is it?"
year = int(raw_input())
print "What year were you born?"
year_of_birth = int(raw_input())
age = year - year_of_birth
unless = age - 1
print "Your age is either %s, or %s if your birthday hasn't happened yet." % (age, unless)