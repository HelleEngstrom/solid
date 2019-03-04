using System;

interface ILibraryItem {

    string LibraryId { get; set; }
    
    string Title { get; set; }
    
    string Author { get; set; }
    
    int NumberOfPages { get; set; }
    
    int LoanPeriodInDays { get; set; }
    
    DateTime BorrowDate { get; set; }
    
    string Borrower { get; set; }

    void CheckOut(string borrower);

    void CheckIn();

    DateTime GetDueDate();
}
