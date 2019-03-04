using System;

class Factory {

    public static IPerson CreatePerson(){
        return new Person();
    }

    public static IBook CreateBook(){
        return new Book(CreateMessageSender(), CreateLogger());
    }

    public static IMessageSender CreateMessageSender(){
        return new Emailer();
    }

    public static ILogger CreateLogger(){
        return new Logger();
    }
}
