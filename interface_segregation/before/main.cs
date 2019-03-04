//mcs -out:main.exe *.cs && mono main.exe

using System;

class HelloWorld {
    static void Main() {

        ILibraryItem book =  new Book {
            Title = "Harry Potter and the Prisoner from Azkaban"
        };

        ILibraryItem audioBook =  new AudioBook {
            Title = "Harry Potter and the Order fo the Phoenix"
        };

        ILibraryItem dvd =  new DVD {
            Title = "Harry Potter and the Deathly Hallows Part 1"
        };

        ILibraryItem referenceBook =  new ReferenceBook {
            Title = "Magical Creatures and Where to Find Them"
        };


        Console.WriteLine(book.Title);
        Console.WriteLine(audioBook.Title);
        Console.WriteLine(dvd.Title);
        Console.WriteLine(referenceBook.Title);
    }
}
