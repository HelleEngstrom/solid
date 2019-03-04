//mcs -out:main.exe *.cs && mono main.exe

using System;

class HelloWorld {
    static void Main() {

        IBorrowableBook book =  new Book {
            Title = "Harry Potter and the Prisoner from Azkaban"
        };

        IAudioBook audioBook =  new AudioBook {
            Title = "Harry Potter and the Order fo the Phoenix"
        };

        IDVD dvd =  new DVD {
            Title = "Harry Potter and the Deathly Hallows Part 1"
        };

        IBook referenceBook =  new ReferenceBook {
            Title = "Magical Creatures and Where to Find Them"
        };


        Console.WriteLine(book.Title);
        Console.WriteLine(audioBook.Title);
        Console.WriteLine(dvd.Title);
        Console.WriteLine(referenceBook.Title);
    }
}
