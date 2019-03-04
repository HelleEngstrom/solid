using System;

interface IBorrowable {

    int LoanPeriodInDays { get; set; }

    DateTime BorrowDate { get; set; }

    string Borrower { get; set; }

    void CheckOut(string borrower);

    void CheckIn();

    DateTime GetDueDate();
}
