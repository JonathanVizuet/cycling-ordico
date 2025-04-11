from app.state import cyclist_state, register_event

def setup_fun():
    "Corre antes de cada test para limpiar el estado"
    cyclist_state.clear()

def test_checkpoint_event_registered():
    #Este es el GIVEN
    event = {
        "cyclist_id" : "123",
        "event" : "checkpoint",
        "location" : "CP1",
        "time": "10:30:00"
    }

    #when
    register_event(event)

    #Then
    assert cyclist_state["123"] == {
        "event": "checkpoint",
        "location": "CP1",
        "time": "10:30:00"
    }

def test_abandoned_event_registered():
    #Given
    event = {
        "cyclist_id": "456",
        "event": "abandoned",
        "time": "11:15:00"
    }

    #When
    register_event(event)

    #Then
    assert cyclist_state["456"] == {
        "event": "abandoned",
        "time": "11:15:00"
    }