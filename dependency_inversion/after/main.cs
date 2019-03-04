//mcs -out:main.exe *.cs && mono main.exe

using System;

class Program {

    static void Main(){

        IPerson helle = Factory.CreatePerson();
        helle.Firstname = "Helle";
        helle.Lastname  = "Engström";
        helle.PhoneNumber = "070-1234567";
        helle.Email = "helle.engstrom@example.com";

        IBook book = Factory.CreateBook();
        book.Title = "Harry Potter and the Philosophers stone";
        book.Author = "J.K Rowling";


        Console.WriteLine();
        book.CheckOut(helle);
        book.SendReminder();
        book.CheckIn();

    }
}
