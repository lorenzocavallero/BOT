from datetime import datetime 

def sample_responsed(input_text):
  user_message = str(input_text).lower()
  
  if user_message in ("hello", "hi", "sup"):
    return "Hey! How's it going?"
  if user_message in ("who are you", "sho are you?"):
    return "I'm a Bot!"
  if user_message in ("time", "time?):
    now = datetime.now()
    date_time = now.strftime("%d/%m/%y, %H:%M:%S")
                      
    return str(date_time)
  return "I don't understand you."
