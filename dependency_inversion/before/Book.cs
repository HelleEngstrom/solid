using System;

class Book {
    public string Title { get; set; }
    public string Author { get; set; }
    public Person Borrower { get; set; }
    public DateTime BorrowDate { get; set; }
    public int LoanPeriodInDays { get; set; } = 21;

    public void CheckOut(Person borrower) {
        Borrower = borrower;
        BorrowDate = DateTime.Now;
        Logger logger = new Logger{};
        logger.Log(Borrower.Firstname + " has borrowed: " + Title + ".");
    }

    public void CheckIn(){
        Logger logger = new Logger{};
        logger.Log(Borrower.Firstname + " has returned: " + Title + ".");
        Borrower = null;
    }

    public DateTime getDueDate(){
        return BorrowDate.AddDays(LoanPeriodInDays);
    }

    public void SendReminder(){
        Emailer emailer = new Emailer{};
        emailer.SendEmail("The due date for the book: " + Title + " is " + getDueDate() + ".", Borrower);
    }
}
