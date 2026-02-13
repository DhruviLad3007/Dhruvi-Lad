using System;
using System.Collections.Generic;
using System.Linq;

namespace StudentApp
{
    class Student
    {
        // Private fields (Encapsulation)
        private int studentId;
        private string name;
        private string department;
        private int year;
        private int marks;

        // Constructor
        public Student(int studentId, string name, string department, int year, int marks)
        {
            this.studentId = studentId;
            this.name = name;
            this.department = department;
            this.year = year;
            this.marks = marks;
        }

        // Getters and Setters
        public int StudentId
        {
            get { return studentId; }
            set { studentId = value; }
        }

        public string Name
        {
            get { return name; }
            set { name = value; }
        }

        public string Department
        {
            get { return department; }
            set { department = value; }
        }

        public int Year
        {
            get { return year; }
            set { year = value; }
        }

        public int Marks
        {
            get { return marks; }
            set { marks = value; }
        }

        // Display Method
        public void Display()
        {
            Console.WriteLine($"ID: {studentId}, Name: {name}, Dept: {department}, Year: {year}, Marks: {marks}");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            // Create multiple student objects
            List<Student> students = new List<Student>()
            {
                new Student(1, "Rahul", "IT", 2, 85),
                new Student(2, "Priya", "CS", 3, 92),
                new Student(3, "Amit", "IT", 1, 70),
                new Student(4, "Sneha", "CS", 4, 88),
                new Student(5, "Karan", "IT", 2, 76)
            };

            Console.WriteLine("----- All Students -----");
            foreach (var student in students)
            {
                student.Display();
            }

            Console.WriteLine("\n----- Students with Marks > 75 -----");
            var highScorers = students.Where(s => s.Marks > 75);
            foreach (var student in highScorers)
            {
                student.Display();
            }

            Console.WriteLine("\n----- Students Sorted by Marks -----");
            var sortedStudents = students.OrderByDescending(s => s.Marks);
            foreach (var student in sortedStudents)
            {
                student.Display();
            }

            Console.WriteLine("\n----- Top 3 Scorers -----");
            var top3 = students.OrderByDescending(s => s.Marks).Take(3);
            foreach (var student in top3)
            {
                student.Display();
            }
        }
    }
}
