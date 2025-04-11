#Representa el estado actual de los ciclistas:
cyclist_state = {}

def register_event(event: dict):
    cyclist_id = event["cyclist_id"]
    event_type = event["event"]
    time = event["time"]

    #Datos que cambian comunmente:
    cyclist_state[cyclist_id] = {
        "event" : event_type,
        "time" : time
    }

    #Si el evento es de tipo 'checkpoint', tambien guarda location:
    if event_type == "checkpoint":
        cyclist_state[cyclist_id]["location"] = event["location"]