using System;

interface IAudioBook : ILibraryItem, IBorrowable {

    int RunTimeInMinutes { get; set; }

}
