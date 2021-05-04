from datetime import datetime 

def sample_responses(input_text):
  user_message = str(input_text).lower()
  
  if user_message in ("Hello", "Hi", "Hello!"):
    return "Welcome"
  if user_message in ("who are you", "sho are you?"):
    return "I'm a Bot!"
  if user_message in ("time", "time?"):
    now = datetime.now()
    date_time = now.strftime("%d/%m/%y, %H:%M:%S")
                      
    return str(date_time)
  return "I don't understand you."
