# TODO List Application

A Django-based web application for managing tasks and organizing them with customizable tags.

## Features

### Task Management
- **Create Tasks**: Add new tasks with custom content and deadlines
- **Update Tasks**: Edit task details including content, deadlines, and completion status
- **Delete Tasks**: Remove tasks you no longer need
- **Mark Complete**: Check off completed tasks with a single click
- **Undo Actions**: Revert task completion status if needed

### Tag System
- **Create Tags**: Organize your tasks by creating custom tags (e.g., "work", "shop", "home")
- **Update Tags**: Modify existing tag names
- **Delete Tags**: Remove tags with confirmation dialog
- **Tag Tasks**: Assign multiple tags to individual tasks for better organization
- **Filter by Tags**: View all tasks associated with specific tags

### User Interface
- Clean, intuitive interface with a sidebar navigation
- Real-time task status indicators ("Done", "Not Done")
- Deadline tracking with date and time stamps
- Quick action buttons for task management

## Technology Stack

- **Backend**: Django (Python web framework)
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite (default Django configuration)
- **URL Routing**: Django URL patterns

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd todo-list-app
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   Open your browser and navigate to `http://127.0.0.1:8000`

## Usage

### Creating a Task
1. Click the "Add Task" button on the home page
2. Enter the task content/description
3. Set a deadline (date and time)
4. Optionally select tags to categorize the task
5. Click "Submit" to create the task

### Updating a Task
1. Click the "Update" link on a task
2. Modify the task content, deadline, or completion status
3. Adjust tag assignments as needed
4. Click "Submit" to save changes

### Completing a Task
1. Click the "Complete" button on a task to mark it as done
2. Use the "Undo" button to revert completion if needed

### Managing Tags
1. Go to the "Tags" section in the sidebar
2. View all existing tags in the tag list
3. Click "Add Tag" to create a new tag
4. Use "Update" to modify a tag name
5. Use "Delete" to remove a tag (with confirmation)

## Model Overview

### Task Model
- **Content**: The task description/title
- **Created**: Timestamp when task was created
- **Deadline**: Due date and time for the task
- **Completed**: Boolean flag for completion status
- **Tags**: Many-to-many relationship with Tag model

### Tag Model
- **Name**: The tag identifier (e.g., "work", "urgent")
- **ID**: Unique identifier

## Key Features Details

### Task Status Indicators
- **Not Done**: Red badge for pending tasks
- **Done**: Green badge for completed tasks

### Confirmation Dialogs
- Delete operations include a confirmation prompt to prevent accidental deletion
- Confirmation dialog displays the item being deleted

### Task Organization
- Tasks display creation time and deadline
- Multiple tags can be assigned to a single task
- Easy visual identification of tagged tasks

## Future Enhancements

Potential features for future development:
- User authentication and multi-user support
- Task priority levels
- Search functionality
- Task categories
- Recurring tasks
- Task notes or descriptions
- Email deadline reminders
- Task statistics and analytics
- Dark mode theme
- Mobile-responsive design improvements

## Contributing

To contribute to this project:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Troubleshooting

### Database Issues
If you encounter database issues, you can reset the database:
```
rm db.sqlite3
python manage.py migrate
```

### Port Already in Use
If port 8000 is already in use, specify a different port:
```
python manage.py runserver 8001
```

### Missing Migrations
Run migrations to ensure your database schema is up to date:
```
python manage.py migrate
```

## Support

For issues, questions, or suggestions, please open an issue on the repository or contact the project maintainers.

---

**Last Updated**: February 13, 2026