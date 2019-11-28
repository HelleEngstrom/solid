using System;

public class ReferenceBook : ILibraryItem {

    public string LibraryId { get; set; }

    public string Title { get; set; }

    public string Author { get; set; }

    public int NumberOfPages { get; set; }

    public int LoanPeriodInDays { get; set; } = 0;

    public DateTime BorrowDate { get; set; }//är inte relevant

    public string Borrower { get; set; }//är inte relevant


    public void CheckOut(string borrower){
        throw new NotImplementedException();
    }

    public void CheckIn(){
        throw new NotImplementedException();
    }

    public DateTime GetDueDate(){
        throw new NotImplementedException();
    }




}
