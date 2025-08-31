# Global list to store all calendar events
list_of_events: list[str] = []

def event_calendar():
    """
    Creates and returns three functions to manage a calendar of events:
    add_event, delete_event, and view_events.
    """
    def add_event(event: str) -> None:
        """Add a new event to the event list."""
        list_of_events.append(event)

    def delete_event(event: str) -> None:
        """Delete an event from the event list if it exists."""
        if event in list_of_events:
            list_of_events.remove(event)
        else:
            print(f"Event '{event}' not found.")

    def view_events() -> None:
        """Print all events in the event list with numbering."""
        if list_of_events:
            for idx, event in enumerate(list_of_events, 1):
                print(f"{idx}. {event}")
        else:
            print("The event list is empty.")

    return add_event, delete_event, view_events

# Get functions for managing the event calendar
add_event, delete_event, view_events = event_calendar()
