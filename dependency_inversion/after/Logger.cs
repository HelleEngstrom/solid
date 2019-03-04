using System;

class Logger : ILogger{
    public void Log(string message){
        Console.WriteLine(message);
        Console.WriteLine();
    }
}
