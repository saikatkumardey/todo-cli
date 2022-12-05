# Todo App

A simple todo app that allows you to add, delete, and mark todos as complete or incomplete.

## Installation

To install the todo app, run the following command:

```
pip install -e .
```

## Usage

To use the todo app, run the following command:

```
todo
```

This will display the available command line options for the app. 

You can use 
- the `-a` or `--add` option to add a new todo
- the `-d` or `--delete` option to delete a todo
- the `-c` or `--complete` option to mark a todo as complete
- the `-uc` or `--uncomplete` option to mark a todo as incomplete,and 
- the `-s` or `--show` option to show all todos.


## Add

For example, to add a new todo, you would run the following command:

```
todo -a "Buy groceries"
```

## Delete

To delete a todo, you would run the following command, where `<task_id>` is the ID of the todo you want to delete:

```
todo -d <task_id>
```

## Complete

```
todo -c <task_id>
```

## Incomplete

```
todo -uc <task_id>
```


## Show all todos

```
todo -s
```

