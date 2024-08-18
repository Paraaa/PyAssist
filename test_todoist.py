from assistant.todoist_assistant import TodoistAssistant


def main():
    todoist_assistant = TodoistAssistant()
    response = todoist_assistant.respond("Schreibe Tomaten auf meine Einkausliste.")


if __name__ == "__main__":
    main()
