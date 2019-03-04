using System;

interface IBook : ILibraryItem{

    string Author { get; set; }

    int NumberOfPages { get; set; }
}
