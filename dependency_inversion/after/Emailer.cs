using System;

class Emailer :IMessageSender {
    public void SendMessage(string message, IPerson recipient){
        Console.WriteLine("Email with message: " + message + " sent to " + recipient.Firstname + ".");
        Console.WriteLine();
    }
}
