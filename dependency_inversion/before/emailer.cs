using System;

class Emailer {
    public void SendEmail(string message, Person recipient){
        Console.WriteLine("Email with message: " + message + " sent to " + recipient.Firstname + ".");
        Console.WriteLine();
    }
}
