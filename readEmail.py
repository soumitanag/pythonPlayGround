import win32com.client
#read email

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
user = outlook.Session.CreateRecipient("soumita.a.nag@ericsson.com")
inbox = outlook.GetDefaultFolder(6) # "6" refers to the index of a folder - in this case,
                                    # the inbox. You can change that number to reference
                                    # any other folder
# ENE = outlook.session.GetDefaultFolder(user,6).sub_folder("ENE")
messages = inbox.Items
message = messages.GetLast()
reply = message.Reply()
reply.Body = "Hello"
reply.send
body_content = message.Body
print (body_content)