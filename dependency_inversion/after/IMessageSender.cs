using System;

interface IMessageSender {
    void SendMessage(string message, IPerson recipient);
}
