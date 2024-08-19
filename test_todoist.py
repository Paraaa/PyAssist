from assistant.todoist_assistant import TodoistAssistant
import time


def main():
    todoist_assistant = TodoistAssistant()
    todoist_assistant.respond("Schreibe Tomaten auf meine Einkausliste.")
    time.sleep(1)
    todoist_assistant.respond("Erinnere mich daran den Abwasch zu machen.")
    time.sleep(1)
    todoist_assistant.respond("Schreibe Basilikum, Gurke, Feta und Hummus auf.")
    time.sleep(1)
    todoist_assistant.respond(
        "Erinnere mich daran auf die Email von Frank zu antworten."
    )


if __name__ == "__main__":
    main()
