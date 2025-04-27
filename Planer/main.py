from nicegui import ui
from datetime import datetime, date, timedelta
from Planer import Tasklist, Event

def printTasks(tasks):
    for task in tasks:
        print(task.description , task.type , task.date ,task.id)


# --- Frontend with NiceGUI ---
class CalendarApp:
    def __init__(self):
        self.tasklist = Tasklist()  # Initialize your Tasklist

        with ui.card().classes('w-full max-w-4xl mx-auto mt-10'):
            with ui.row().classes('items-center justify-between w-full'):
                ui.label('Calendar').classes('text-xl font-bold')
                
                # Two buttons next to each other
                ui.button('Add Event', on_click=self.open_add_event_dialog)
                ui.button('Weekly Tasks', on_click=self.show_weekly_tasks)

            # Big calendar
            self.calendar = ui.date(value=str(date.today()), on_change=self.update_selected_date).classes('w-full h-96 text-lg')
            self.selected_date = date.today()

            self.result = ui.label()

    def update_selected_date(self, e):
        self.selected_date = datetime.strptime(e.value, '%Y-%m-%d').date()
        self.result.set_text(f"Selected date: {self.selected_date}")

    def open_add_event_dialog(self):
        with ui.dialog() as dialog, ui.card():
            ui.label('Add New Event')

            event_description = ui.input('Description')
            event_type = ui.input('Type')

            def save_event():
                new_event = Event(
                    date=self.selected_date,
                    description=event_description.value,
                    type=event_type.value
                )
                self.tasklist.addtask(new_event)
                ui.notify(f"Added: {new_event.description} on {new_event.date}")
                print(f"Tasklist now has {len(self.tasklist.gettasks())} events")

                dialog.close()

            ui.button('Save', on_click=save_event)
            ui.button('Cancel', on_click=dialog.close)

        dialog.open()

    
    def show_weekly_tasks(self):
        tasks = self.tasklist.weeklyTasks()
        print("weekly tasks: ", len(tasks))
        printTasks(tasks)

        with ui.dialog() as dialog, ui.card():
            ui.label('Weekly Tasks').classes('text-xl font-bold')

            if not tasks:
                ui.label('No tasks for this week.')
            else:
                # TABLE of ALL weekly tasks
                ui.table(
                    columns=[
                        {'name': 'date', 'label': 'Date', 'field': 'date'},
                        {'name': 'description', 'label': 'Description', 'field': 'description'},
                        {'name': 'type', 'label': 'Type', 'field': 'type'},
                    ],
                    rows=[
                        {'date': str(task.date), 'description': task.description, 'type': task.type}
                        for task in tasks
                    ],
                    row_key='date',  # We can use date or any unique thing for now
                ).classes('max-h-64 w-full').props('virtual-scroll')

            ui.button('Close', on_click=dialog.close)

        dialog.open()
        
# Run app
print("starting...")
CalendarApp()
ui.run(port=8000)