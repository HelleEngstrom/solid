using System;

interface IDVD : ILibraryItem, IBorrowable {

    int RunTimeInMinutes { get; set; }

    string[] Actors { get; set; }

}
