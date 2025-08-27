print("Result:", 2 + 3 * 4 > 10 and not (5 in [1, 2, 3]))
"""Step-by-step breakdown (showing precedence):
Parentheses first
(5 in [1, 2, 3]) → False

Multiplication before addition
3 * 4 → 12
2 + 12 → 14

Comparison (>)
14 > 10 → True

not applies to result of parentheses
not False → True

and (boolean operator) last
True and True → True"""


#Rule of THUMB for +  and , in print
#Use commas in print when you want space-separated items without worrying about conversions.
#Use + with str() only when you explicitly need string concatenation

print("Hello", "World", 123)
print("Hello" + "World")
print("Hello" + " " + str(123))
person={"age":18,"height":6*2+2}
print("Does age exists :" , 'age' in person)
print("Does age exists :" + 'age' in person)

"""
Difference between , and + in print, (comma inside print)
In Python, print can take multiple arguments separated by commas.
Each argument is converted to a string (if not already).
Python automatically inserts a space between them.
+ (string concatenation)
+ joins two strings into one.
But both sides must be strings. If not, you must convert manually with str().
Coming back to your code
print("Does age exists :" , 'age' in person)
print("Does age exists :" + 'age' in person)

First line

"Does age exists :" and 'age' in person are two separate arguments.

print handles them separately, puts a space in between.

'age' in person → True because 'age' is a key in the dictionary.

Output:

Does age exists : True

Second line

Python sees + first (string concatenation has higher precedence than in).

"Does age exists :" + 'age' → "Does age exists :age"

Then it checks: "Does age exists :age" in person
→ This means: is "Does age exists :age" a key in the dictionary?
→ No, that’s not one of the keys.

So result is False.

Output:

False

✅ Why one is True and the other is False?

First case: You directly tested 'age' in person → True.

Second case: You accidentally tested "Does age exists :age" in person → False, because that string isn’t a key.

"""
