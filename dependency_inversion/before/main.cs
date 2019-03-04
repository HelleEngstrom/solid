//mcs -out:main.exe *.cs && mono main.exe

using System;

class Program {

    static void Main(){

        Person helle = new Person{
            Firstname = "Helle",
            Lastname  = "Engström",
            PhoneNumber = "070-1234567",
            Email = "helle.engstrom@example.com"
        };

        Book book = new Book{
            Title = "Harry Potter and the Philosophers stone",
            Author = "J.K Rowling"
        };

        Console.WriteLine();
        book.CheckOut(helle);
        book.SendReminder();
        book.CheckIn();

    }
}
