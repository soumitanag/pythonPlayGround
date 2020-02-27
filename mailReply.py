import win32com.client
outlook = win32com.client.Dispatch("Outlook.Application")
user = outlook.Session.CreateRecipient("soumita.a.nag@ericsson.com")
inbox = outlook.Session.GetSharedDefaultFolder(user, 6)
ENE = inbox.Folders["RTA"]
messages = inbox.Items
message = messages.GetLast()
# reply =  message.Reply()
# reply.Body = "Hello"
# reply.Send
# message.Move(ENE)
# body_content = message.Subject
# print (body_content)

mail = outlook.CreateItem(0)
mail.To = "rashi.basavatia@ericsson.com"
mail.Subject = "test email"
mail.Body = "sending automated email"
mail.Send()
print("mail sent")
