# Task Tracker

A simple command-line application to manage your tasks. Add, view, update, delete, and track the status of your tasks with ease.

## Features

- Add new tasks
- View all tasks
- Update task titles
- Delete tasks
- Mark tasks as "In Progress" or "Completed"
- Persistent storage using JSON

## Project Structure

```
task_tracker/
├── main.py
├── task_manager.py
├── data/
│   └── tasks.json
├── README.md
```

## Getting Started

### Prerequisites

- Python 3.7 or higher

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/task_tracker.git
    cd task_tracker
    ```

### Usage

Run the application:
```sh
python main.py
```

Follow the on-screen menu to manage your tasks.

## Data Storage

All tasks are stored in `data/tasks.json`. The file is created automatically if it does not exist.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](LICENSE)