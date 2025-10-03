"""
SQLite3 Python Tutorial - Complete Beginner's Guide
====================================================
This tutorial covers everything you need to know about using SQLite3 with Python.
Each section includes detailed explanations and practical examples.
"""

import sqlite3
from datetime import datetime

# =============================================================================
# SECTION 1: CONNECTING TO A DATABASE
# =============================================================================
print("=" * 70)
print("SECTION 1: CONNECTING TO A DATABASE")
print("=" * 70)

# What is SQLite?
# - SQLite is a lightweight database that stores data in a single file
# - No separate server needed - it's built into Python!
# - Perfect for small to medium applications

# Connect to a database file (creates the file if it doesn't exist)
connection = sqlite3.connect('my_database.db')
print("✓ Connected to database 'my_database.db'")

# What is a cursor?
# - Think of it as a pointer that executes SQL commands
# - You need a cursor to run queries and get results
cursor = connection.cursor()
print("✓ Cursor created")

# Alternative: In-memory database (temporary, deleted when program ends)
# memory_connection = sqlite3.connect(':memory:')
# Useful for testing or temporary data

print()

# =============================================================================
# SECTION 2: CREATING TABLES
# =============================================================================
print("=" * 70)
print("SECTION 2: CREATING TABLES")
print("=" * 70)

# Drop existing table if it exists (for clean start)
cursor.execute('DROP TABLE IF EXISTS students')

# Create a table with different data types
cursor.execute('''
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    age INTEGER,
    gpa REAL,
    enrolled INTEGER DEFAULT 1
)
''')

# Let's break down the table structure:
# - id: Auto-incrementing number (1, 2, 3, ...) - PRIMARY KEY means unique identifier
# - name: TEXT type - stores strings (NOT NULL means it's required)
# - email: TEXT with UNIQUE constraint - no duplicate emails allowed
# - age: INTEGER - whole numbers
# - gpa: REAL - decimal numbers (like 3.75)
# - enrolled: INTEGER with default value 1 (1=true, 0=false in SQLite)

print("✓ Table 'students' created with columns: id, name, email, age, gpa, enrolled")

# IMPORTANT: commit() saves your changes to the database
connection.commit()
print("✓ Changes saved (committed) to database")

print()

# =============================================================================
# SECTION 3: INSERTING DATA (Adding Rows)
# =============================================================================
print("=" * 70)
print("SECTION 3: INSERTING DATA")
print("=" * 70)

# Method 1: Insert one row using ? placeholders
# The ? prevents SQL injection attacks - ALWAYS use placeholders!
cursor.execute('''
INSERT INTO students (name, email, age, gpa)
VALUES (?, ?, ?, ?)
''', ('Alice Johnson', 'alice@email.com', 20, 3.8))
print("✓ Inserted: Alice Johnson")

# Method 2: Insert multiple rows at once (faster!)
students_list = [
    ('Bob Smith', 'bob@email.com', 22, 3.5),
    ('Carol White', 'carol@email.com', 21, 3.9),
    ('David Brown', 'david@email.com', 23, 3.2),
    ('Eve Davis', 'eve@email.com', 20, 3.7)
]

cursor.executemany('''
INSERT INTO students (name, email, age, gpa)
VALUES (?, ?, ?, ?)
''', students_list)
print(f"✓ Inserted {len(students_list)} students using executemany()")

# Method 3: Named placeholders (more readable for complex queries)
cursor.execute('''
INSERT INTO students (name, email, age, gpa)
VALUES (:name, :email, :age, :gpa)
''', {'name': 'Frank Miller', 'email': 'frank@email.com', 'age': 22, 'gpa': 3.6})
print("✓ Inserted: Frank Miller (using named placeholders)")

# Get the ID of the last inserted row
print(f"✓ Last inserted student ID: {cursor.lastrowid}")

# Don't forget to commit!
connection.commit()
print("✓ All insertions saved to database")

print()

# =============================================================================
# SECTION 4: READING DATA (SELECT Queries)
# =============================================================================
print("=" * 70)
print("SECTION 4: READING DATA")
print("=" * 70)

# Query 1: Get ALL rows and ALL columns
print("\n--- All Students ---")
cursor.execute('SELECT * FROM students')
all_students = cursor.fetchall()  # fetchall() returns a list of tuples

for student in all_students:
    print(student)

# Query 2: Get specific columns only
print("\n--- Names and GPAs Only ---")
cursor.execute('SELECT name, gpa FROM students')
names_and_gpas = cursor.fetchall()

for name, gpa in names_and_gpas:
    print(f"{name}: GPA {gpa}")

# Query 3: Get ONE row only
print("\n--- First Student ---")
cursor.execute('SELECT * FROM students')
first_student = cursor.fetchone()  # fetchone() returns a single tuple
print(first_student)

# Query 4: Get limited number of rows
print("\n--- First 3 Students ---")
cursor.execute('SELECT * FROM students')
three_students = cursor.fetchmany(3)  # fetchmany(n) returns n rows
for student in three_students:
    print(student)

# Query 5: Filtering with WHERE clause
print("\n--- Students with GPA > 3.5 ---")
cursor.execute('SELECT name, gpa FROM students WHERE gpa > ?', (3.5,))
high_gpa_students = cursor.fetchall()

for name, gpa in high_gpa_students:
    print(f"{name}: {gpa}")

# Query 6: Multiple conditions with AND/OR
print("\n--- Students: age 20 AND gpa > 3.5 ---")
cursor.execute('SELECT name, age, gpa FROM students WHERE age = ? AND gpa > ?', (20, 3.5))
filtered_students = cursor.fetchall()

for student in filtered_students:
    print(student)

# Query 7: Pattern matching with LIKE
print("\n--- Students with 'email.com' address ---")
cursor.execute("SELECT name, email FROM students WHERE email LIKE ?", ('%email.com',))
# % is a wildcard: %email.com matches anything ending with email.com

for name, email in cursor.fetchall():
    print(f"{name}: {email}")

# Query 8: Sorting with ORDER BY
print("\n--- Students Sorted by GPA (Highest First) ---")
cursor.execute('SELECT name, gpa FROM students ORDER BY gpa DESC')
# DESC = descending (high to low), ASC = ascending (low to high)

for name, gpa in cursor.fetchall():
    print(f"{name}: {gpa}")

# Query 9: Using aggregate functions
print("\n--- Statistics ---")
cursor.execute('''
SELECT 
    COUNT(*) as total_students,
    AVG(gpa) as average_gpa,
    MAX(gpa) as highest_gpa,
    MIN(gpa) as lowest_gpa
FROM students
''')
stats = cursor.fetchone()
print(f"Total Students: {stats[0]}")
print(f"Average GPA: {stats[1]:.2f}")
print(f"Highest GPA: {stats[2]}")
print(f"Lowest GPA: {stats[3]}")

# Query 10: Grouping data
print("\n--- Count Students by Age ---")
cursor.execute('''
SELECT age, COUNT(*) as student_count
FROM students
GROUP BY age
ORDER BY age
''')
# GROUP BY combines rows with the same value

for age, count in cursor.fetchall():
    print(f"Age {age}: {count} student(s)")

print()

# =============================================================================
# SECTION 5: UPDATING DATA (Modifying Existing Rows)
# =============================================================================
print("=" * 70)
print("SECTION 5: UPDATING DATA")
print("=" * 70)

# Update one student's GPA
print("\n--- Updating Bob's GPA ---")
cursor.execute('''
UPDATE students 
SET gpa = ? 
WHERE name = ?
''', (3.9, 'Bob Smith'))

print(f"✓ Updated {cursor.rowcount} row(s)")
# cursor.rowcount tells you how many rows were affected

# Update multiple students at once
print("\n--- Increasing GPA by 0.1 for students over 22 ---")
cursor.execute('''
UPDATE students 
SET gpa = gpa + 0.1 
WHERE age > ?
''', (22,))

print(f"✓ Updated {cursor.rowcount} row(s)")

# Verify the changes
cursor.execute('SELECT name, age, gpa FROM students WHERE age > 22')
print("Students over 22:")
for student in cursor.fetchall():
    print(student)

connection.commit()
print("\n✓ Updates saved to database")

print()

# =============================================================================
# SECTION 6: DELETING DATA
# =============================================================================
print("=" * 70)
print("SECTION 6: DELETING DATA")
print("=" * 70)

# Insert a test student to delete
cursor.execute('''
INSERT INTO students (name, email, age, gpa)
VALUES (?, ?, ?, ?)
''', ('Test Student', 'test@email.com', 19, 2.5))
connection.commit()

# Delete specific row
print("\n--- Deleting Test Student ---")
cursor.execute('DELETE FROM students WHERE name = ?', ('Test Student',))
print(f"✓ Deleted {cursor.rowcount} row(s)")

# Delete multiple rows with condition
print("\n--- Deleting students with GPA < 3.0 ---")
cursor.execute('DELETE FROM students WHERE gpa < ?', (3.0,))
print(f"✓ Deleted {cursor.rowcount} row(s)")

connection.commit()
print("✓ Deletions saved to database")

# WARNING: DELETE without WHERE deletes ALL rows!
# cursor.execute('DELETE FROM students')  # Deletes everything!

print()

# =============================================================================
# SECTION 7: WORKING WITH DICTIONARIES (Easier Data Access)
# =============================================================================
print("=" * 70)
print("SECTION 7: ACCESSING DATA AS DICTIONARIES")
print("=" * 70)

# By default, rows are returned as tuples
# With Row factory, you can access columns by name like a dictionary

connection.row_factory = sqlite3.Row  # Enable dictionary-like access
cursor = connection.cursor()  # Create new cursor with row factory

cursor.execute('SELECT * FROM students LIMIT 2')
students = cursor.fetchall()

print("\n--- Students as Dictionaries ---")
for student in students:
    # Access by column name instead of index
    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Email: {student['email']}")
    print(f"Age: {student['age']}")
    print(f"GPA: {student['gpa']}")
    print(f"Enrolled: {student['enrolled']}")
    print("-" * 40)

# Convert to regular dictionary
student_dict = dict(student)
print(f"As dict: {student_dict}")

# Reset to normal tuples
connection.row_factory = None
cursor = connection.cursor()

print()

# =============================================================================
# SECTION 8: TRANSACTIONS (All-or-Nothing Operations)
# =============================================================================
print("=" * 70)
print("SECTION 8: TRANSACTIONS")
print("=" * 70)

# What is a transaction?
# - A group of operations that either ALL succeed or ALL fail
# - Example: Transferring money between accounts - both must succeed

print("\n--- Transaction Example: Transfer GPA Points ---")
print("Before: ")
cursor.execute('SELECT name, gpa FROM students WHERE name IN (?, ?)', 
               ('Alice Johnson', 'Bob Smith'))
for student in cursor.fetchall():
    print(f"  {student[0]}: {student[1]}")

try:
    # Start transaction (happens automatically with execute)
    # Take 0.2 from Alice
    cursor.execute('UPDATE students SET gpa = gpa - 0.2 WHERE name = ?', 
                   ('Alice Johnson',))
    
    # Give 0.2 to Bob
    cursor.execute('UPDATE students SET gpa = gpa + 0.2 WHERE name = ?', 
                   ('Bob Smith',))
    
    # If both succeed, commit (save changes)
    connection.commit()
    print("\n✓ Transaction successful!")
    
except sqlite3.Error as error:
    # If anything fails, rollback (undo all changes)
    connection.rollback()
    print(f"\n✗ Transaction failed: {error}")
    print("✓ All changes rolled back")

print("\nAfter: ")
cursor.execute('SELECT name, gpa FROM students WHERE name IN (?, ?)', 
               ('Alice Johnson', 'Bob Smith'))
for student in cursor.fetchall():
    print(f"  {student[0]}: {student[1]}")

print()

# =============================================================================
# SECTION 9: WORKING WITH MULTIPLE TABLES (Relationships)
# =============================================================================
print("=" * 70)
print("SECTION 9: MULTIPLE TABLES AND JOINS")
print("=" * 70)

# Create a courses table
cursor.execute('DROP TABLE IF EXISTS courses')
cursor.execute('''
CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    course_name TEXT,
    grade TEXT,
    FOREIGN KEY (student_id) REFERENCES students(id)
)
''')
# FOREIGN KEY links course to a student

print("✓ Created 'courses' table")

# Add some courses
courses_data = [
    (1, 'Math 101', 'A'),
    (1, 'English 101', 'B'),
    (2, 'Math 101', 'A'),
    (3, 'History 101', 'B'),
]

cursor.executemany('''
INSERT INTO courses (student_id, course_name, grade)
VALUES (?, ?, ?)
''', courses_data)
connection.commit()
print("✓ Added sample courses")

# INNER JOIN: Get students with their courses
print("\n--- Students and Their Courses (INNER JOIN) ---")
cursor.execute('''
SELECT students.name, courses.course_name, courses.grade
FROM students
INNER JOIN courses ON students.id = courses.student_id
''')
# INNER JOIN only shows students who have courses

for name, course, grade in cursor.fetchall():
    print(f"{name} - {course}: {grade}")

# LEFT JOIN: Get ALL students, even those without courses
print("\n--- All Students and Their Courses (LEFT JOIN) ---")
cursor.execute('''
SELECT students.name, courses.course_name, courses.grade
FROM students
LEFT JOIN courses ON students.id = courses.student_id
''')
# LEFT JOIN shows all students; course columns are NULL if no match

for name, course, grade in cursor.fetchall():
    course_info = f"{course}: {grade}" if course else "No courses"
    print(f"{name} - {course_info}")

print()

# =============================================================================
# SECTION 10: CHECKING TABLE INFORMATION
# =============================================================================
print("=" * 70)
print("SECTION 10: DATABASE INTROSPECTION")
print("=" * 70)

# Check if a table exists
cursor.execute('''
SELECT name FROM sqlite_master 
WHERE type='table' AND name='students'
''')
table_exists = cursor.fetchone() is not None
print(f"\n✓ Table 'students' exists: {table_exists}")

# Get table structure (columns info)
print("\n--- Table Structure ---")
cursor.execute('PRAGMA table_info(students)')
columns = cursor.fetchall()

for col in columns:
    col_id, name, data_type, not_null, default_val, is_pk = col
    print(f"Column: {name}")
    print(f"  Type: {data_type}")
    print(f"  Required: {'Yes' if not_null else 'No'}")
    print(f"  Default: {default_val if default_val else 'None'}")
    print(f"  Primary Key: {'Yes' if is_pk else 'No'}")
    print()

# List all tables in database
print("--- All Tables in Database ---")
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
for table in tables:
    print(f"  - {table[0]}")

print()

# =============================================================================
# SECTION 11: ERROR HANDLING
# =============================================================================
print("=" * 70)
print("SECTION 11: ERROR HANDLING")
print("=" * 70)

# Example 1: Duplicate unique value
print("\n--- Trying to insert duplicate email ---")
try:
    cursor.execute('''
    INSERT INTO students (name, email, age, gpa)
    VALUES (?, ?, ?, ?)
    ''', ('Another Alice', 'alice@email.com', 21, 3.5))
    connection.commit()
except sqlite3.IntegrityError as error:
    print(f"✗ Error: {error}")
    print("  (Email must be unique!)")

# Example 2: Invalid SQL
print("\n--- Trying invalid SQL ---")
try:
    cursor.execute('SELECT * FROM nonexistent_table')
except sqlite3.OperationalError as error:
    print(f"✗ Error: {error}")
    print("  (Table doesn't exist!)")

# General error handling pattern
print("\n--- Safe Query Pattern ---")
try:
    cursor.execute('SELECT * FROM students WHERE age = ?', (20,))
    results = cursor.fetchall()
    print(f"✓ Found {len(results)} student(s)")
except sqlite3.Error as error:
    print(f"✗ Database error: {error}")

print()

# =============================================================================
# SECTION 12: USING CONTEXT MANAGERS (Automatic Cleanup)
# =============================================================================
print("=" * 70)
print("SECTION 12: CONTEXT MANAGERS")
print("=" * 70)

# The 'with' statement automatically commits or rolls back
print("\n--- Using 'with' for automatic commit ---")

with sqlite3.connect('my_database.db') as conn:
    cur = conn.cursor()
    cur.execute('SELECT COUNT(*) FROM students')
    count = cur.fetchone()[0]
    print(f"✓ Total students: {count}")
    # Automatically commits when block ends (if no error)
    # Automatically rolls back if an error occurs

print("✓ Connection auto-committed and closed")

print()

# =============================================================================
# SECTION 13: USEFUL TIPS AND BEST PRACTICES
# =============================================================================
print("=" * 70)
print("SECTION 13: TIPS AND BEST PRACTICES")
print("=" * 70)

print("""
1. ALWAYS use ? placeholders, never string formatting:
   ✓ Good: cursor.execute('SELECT * FROM users WHERE name = ?', (name,))
   ✗ Bad:  cursor.execute(f'SELECT * FROM users WHERE name = {name}')
   
2. Commit your changes:
   - After INSERT, UPDATE, DELETE operations
   - Use connection.commit()
   
3. Close connections when done:
   - cursor.close()
   - connection.close()
   - Or use 'with' statement
   
4. Use executemany() for bulk inserts:
   - Much faster than multiple execute() calls
   
5. Check rowcount after UPDATE/DELETE:
   - Verify operations affected expected number of rows
   
6. Enable foreign keys (they're off by default):
   connection.execute('PRAGMA foreign_keys = ON')
   
7. Use transactions for related operations:
   - Wrap multiple operations in try/except
   - Commit if all succeed, rollback if any fail
   
8. Use LIMIT when testing queries:
   - Prevents accidentally returning millions of rows
   
9. Create indexes for frequently queried columns:
   cursor.execute('CREATE INDEX idx_email ON students(email)')
   
10. Use row_factory for easier column access:
    connection.row_factory = sqlite3.Row
""")

# =============================================================================
# CLEANUP
# =============================================================================
print("=" * 70)
print("CLEANUP")
print("=" * 70)

cursor.close()
connection.close()
print("\n✓ Cursor closed")
print("✓ Connection closed")
print("\n" + "=" * 70)
print("TUTORIAL COMPLETE! You now know SQLite3 with Python!")
print("=" * 70)