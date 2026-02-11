
class StudentDetails
{
    public int student_id;
    public string name;
    public string department;
    public int marks;
}

class Program
{
    static void Main()
    {
        List<StudentDetails> students = new List<StudentDetails>();

        Console.Write("Enter number of students: ");
        int n = Convert.ToInt32(Console.ReadLine());

        // 1. Accept student details
        for (int i = 0; i < n; i++)
        {
            StudentDetails s = new StudentDetails();

            Console.WriteLine($"\nEnter details for Student {i + 1}");

            Console.Write("Student ID: ");
            s.student_id = Convert.ToInt32(Console.ReadLine());

            Console.Write("Name: ");
            s.name = Console.ReadLine();

            Console.Write("Department: ");
            s.department = Console.ReadLine();

            Console.Write("Marks: ");
            s.marks = Convert.ToInt32(Console.ReadLine());

            students.Add(s);
        }

        // 2. Display all student records
        Console.WriteLine("\nAll Student Records:");
        foreach (var s in students)
        {
            Console.WriteLine($"{s.student_id} | {s.name} | {s.department} | {s.marks}");
        }

        // 3. Display only name and department
        Console.WriteLine("\nName and Department:");
        foreach (var s in students)
        {
            Console.WriteLine($"{s.name} - {s.department}");
        }

        // 4. Students with marks > 75
        Console.WriteLine("\nStudents with marks > 75:");
        var highScorers = students.Where(s => s.marks > 75);
        foreach (var s in highScorers)
        {
            Console.WriteLine($"{s.name} - {s.marks}");
        }

        // 5. Students from specific department
        Console.Write("\nEnter department to filter: ");
        string dept = Console.ReadLine();

        var deptStudents = students.Where(s => s.department.Equals(dept, StringComparison.OrdinalIgnoreCase));
        Console.WriteLine($"\nStudents from {dept} Department:");
        foreach (var s in deptStudents)
        {
            Console.WriteLine($"{s.name}");
        }

        // 6. Sort by marks (descending)
        var sortedStudents = students.OrderByDescending(s => s.marks);
        Console.WriteLine("\nStudents sorted by marks (Descending):");
        foreach (var s in sortedStudents)
        {
            Console.WriteLine($"{s.name} - {s.marks}");
        }

        // 7. Display top scorer
        var topScorer = students.OrderByDescending(s => s.marks).FirstOrDefault();
        Console.WriteLine($"\nTop Scorer: {topScorer.name} - {topScorer.marks}");
    }
}
