using System;

public class AudioBook : IAudioBook {

    public string LibraryId { get; set; }

    public string Title { get; set; }

    public string Author { get; set; }

    public int NumberOfPages { get; set; } = 0;

    public int LoanPeriodInDays { get; set; } = 14;

    public DateTime BorrowDate { get; set; }

    public string Borrower { get; set; }

    public int RunTimeInMinutes { get; set; }


    public void CheckOut(string borrower){
        Borrower = borrower;
        BorrowDate = DateTime.Now;
    }

    public void CheckIn(){
        Borrower = "";
    }

    public DateTime GetDueDate(){
        return BorrowDate.AddDays(LoanPeriodInDays);
    }






}
