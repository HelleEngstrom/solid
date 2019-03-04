using System;

class Book : IBook{
    IMessageSender _emailer;
    ILogger _logger;

    public string Title { get; set; }
    public string Author { get; set; }
    public IPerson Borrower { get; set; }
    public DateTime BorrowDate { get; set; }
    public int LoanPeriodInDays { get; set; } = 21;

    public Book(IMessageSender emailer, ILogger logger){
        _emailer = emailer;
        _logger = logger;
    }

    public void CheckOut(IPerson borrower) {
        Borrower = borrower;
        BorrowDate = DateTime.Now;
        _logger.Log(Borrower.Firstname + " has borrowed: " + Title + ".");
    }

    public void CheckIn(){
        _logger.Log(Borrower.Firstname + " has returned: " + Title + ".");
        Borrower = null;
    }

    public DateTime getDueDate(){
        return BorrowDate.AddDays(LoanPeriodInDays);
    }

    public void SendReminder(){
        _emailer.SendMessage("The due date for the book: " + Title + " is " + getDueDate() + ".", Borrower);
    }
}
