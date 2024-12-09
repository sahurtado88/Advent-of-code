using System;
using System.IO;

namespace AdventOfCode.Y2024.Day6 {
    class Program {
        static void Main(string[] args){
            string inputhPath="input.txt";
            string input = File.ReadAllText(inputhPath);
            Solution solution = new Solution();
            Console.WriteLine("Part One: " + solution.PartOne(input));
            Console.WriteLine("Part two: " + solution.PartTwo(input));
        }
    }
}