from todoist_api_python.api import TodoistAPI
from utils.env import TODOIST_API_KEY
import asyncio


async def main():
    api = TodoistAPI(TODOIST_API_KEY)
    try:
        projects = await api.get_projects()
        tasks = await api.get_tasks()
        print(projects)
        print(tasks)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    asyncio.run(main())
