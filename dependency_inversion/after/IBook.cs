using System;

interface IBook {
    string Title { get; set; }
    string Author { get; set; }
    IPerson Borrower { get; set; }
    DateTime BorrowDate { get; set; }
    int LoanPeriodInDays { get; set; }

    void CheckOut(IPerson borrower);

    void CheckIn();

    DateTime getDueDate();

    void SendReminder();
}
