# Project Title

A simple database management system (DBMS) implemented in Python.

## Project Structure

```
.DS_Store
.vscode/
	launch.json
	tasks.json
src/
	__pycache__/
	commands.py
	dbms/
		random.csv
	main.py
	StorageManager.py
	Trie.py
	Utils.py
Tests/
	StorageManagerTest.py
```

## Description

This project is a basic DBMS that supports operations such as [`select`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fharounguessous%2FDesktop%2FLearning%2FDatabase%2Fsrc%2Fcommands.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A6%2C%22character%22%3A8%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fharounguessous%2FDesktop%2FLearning%2FDatabase%2Fsrc%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A10%2C%22character%22%3A15%7D%7D%5D%2C%22165ee369-be5c-4e1a-9973-a368ee70b7a8%22%5D "Go to definition"), [`insert`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fharounguessous%2FDesktop%2FLearning%2FDatabase%2Fsrc%2Fcommands.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A18%2C%22character%22%3A8%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fharounguessous%2FDesktop%2FLearning%2FDatabase%2Fsrc%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A16%2C%22character%22%3A13%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fharounguessous%2FDesktop%2FLearning%2FDatabase%2Fsrc%2FStorageManager.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A13%2C%22character%22%3A26%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fharounguessous%2FDesktop%2FLearning%2FDatabase%2Fsrc%2FTrie.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A9%2C%22character%22%3A8%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fharounguessous%2FDesktop%2FLearning%2FDatabase%2FTests%2FStorageManagerTest.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A4%2C%22character%22%3A9%7D%7D%5D%2C%22165ee369-be5c-4e1a-9973-a368ee70b7a8%22%5D "Go to definition"), [`create`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fharounguessous%2FDesktop%2FLearning%2FDatabase%2Fsrc%2Fcommands.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A48%2C%22character%22%3A8%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fharounguessous%2FDesktop%2FLearning%2FDatabase%2Fsrc%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A19%2C%22character%22%3A13%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fharounguessous%2FDesktop%2FLearning%2FDatabase%2FTests%2FStorageManagerTest.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A18%2C%22character%22%3A13%7D%7D%5D%2C%22165ee369-be5c-4e1a-9973-a368ee70b7a8%22%5D "Go to definition"), [`remove`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fharounguessous%2FDesktop%2FLearning%2FDatabase%2Fsrc%2Fcommands.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A46%2C%22character%22%3A8%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fharounguessous%2FDesktop%2FLearning%2FDatabase%2Fsrc%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A23%2C%22character%22%3A13%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fharounguessous%2FDesktop%2FLearning%2FDatabase%2Fsrc%2FStorageManager.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A34%2C%22character%22%3A15%7D%7D%5D%2C%22165ee369-be5c-4e1a-9973-a368ee70b7a8%22%5D "Go to definition"), and [`delete`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fharounguessous%2FDesktop%2FLearning%2FDatabase%2Fsrc%2Fcommands.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A43%2C%22character%22%3A8%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fharounguessous%2FDesktop%2FLearning%2FDatabase%2Fsrc%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A21%2C%22character%22%3A13%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fharounguessous%2FDesktop%2FLearning%2FDatabase%2Fsrc%2FStorageManager.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A35%2C%22character%22%3A22%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fharounguessous%2FDesktop%2FLearning%2FDatabase%2Fsrc%2FTrie.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A17%2C%22character%22%3A8%7D%7D%5D%2C%22165ee369-be5c-4e1a-9973-a368ee70b7a8%22%5D "Go to definition") on CSV files. The system uses a Trie data structure for efficient data management and includes utility functions for various operations.

## Files and Directories

- **.vscode/**: Contains configuration files for Visual Studio Code.
  - 

launch.json

: Configuration for debugging.
  - 

tasks.json

: Configuration for build tasks.

- **src/**: Contains the source code of the project.
  - 

commands.py

: Implements the [`Commands`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fharounguessous%2FDesktop%2FLearning%2FDatabase%2Fsrc%2Fcommands.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A2%2C%22character%22%3A6%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fharounguessous%2FDesktop%2FLearning%2FDatabase%2Fsrc%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A1%2C%22character%22%3A21%7D%7D%5D%2C%22165ee369-be5c-4e1a-9973-a368ee70b7a8%22%5D "Go to definition") class which handles DBMS operations.
  - [`dbms/`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fharounguessous%2FDesktop%2FLearning%2FDatabase%2FTests%2FStorageManagerTest.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A21%2C%22character%22%3A40%7D%7D%5D%2C%22165ee369-be5c-4e1a-9973-a368ee70b7a8%22%5D "Go to definition"): Directory where database files (CSV) are stored.
    - 

random.csv

: Sample CSV file with data.
  - 

main.py

: Entry point of the application.
  - 

StorageManager.py

: Implements the [`StorageManager`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fharounguessous%2FDesktop%2FLearning%2FDatabase%2Fsrc%2Fcommands.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A0%2C%22character%22%3A5%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fharounguessous%2FDesktop%2FLearning%2FDatabase%2Fsrc%2FStorageManager.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A4%2C%22character%22%3A6%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fharounguessous%2FDesktop%2FLearning%2FDatabase%2FTests%2FStorageManagerTest.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A6%2C%22character%22%3A5%7D%7D%5D%2C%22165ee369-be5c-4e1a-9973-a368ee70b7a8%22%5D "Go to definition") class for managing storage operations.
  - 

Trie.py

: Implements the [`Trie`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fharounguessous%2FDesktop%2FLearning%2FDatabase%2Fsrc%2FStorageManager.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A2%2C%22character%22%3A5%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fharounguessous%2FDesktop%2FLearning%2FDatabase%2Fsrc%2FTrie.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A5%2C%22character%22%3A6%7D%7D%5D%2C%22165ee369-be5c-4e1a-9973-a368ee70b7a8%22%5D "Go to definition") and [`TrieNode`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fharounguessous%2FDesktop%2FLearning%2FDatabase%2Fsrc%2FTrie.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A0%2C%22character%22%3A6%7D%7D%5D%2C%22165ee369-be5c-4e1a-9973-a368ee70b7a8%22%5D "Go to definition") classes for efficient data storage.
  - 

Utils.py

: Contains utility functions such as [`printOut`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fharounguessous%2FDesktop%2FLearning%2FDatabase%2Fsrc%2Fcommands.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A1%2C%22character%22%3A18%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fharounguessous%2FDesktop%2FLearning%2FDatabase%2Fsrc%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A2%2C%22character%22%3A18%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fharounguessous%2FDesktop%2FLearning%2FDatabase%2Fsrc%2FStorageManager.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A3%2C%22character%22%3A30%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fharounguessous%2FDesktop%2FLearning%2FDatabase%2Fsrc%2FUtils.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A2%2C%22character%22%3A4%7D%7D%5D%2C%22165ee369-be5c-4e1a-9973-a368ee70b7a8%22%5D "Go to definition"), [`Conditional`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fharounguessous%2FDesktop%2FLearning%2FDatabase%2Fsrc%2Fcommands.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A1%2C%22character%22%3A38%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fharounguessous%2FDesktop%2FLearning%2FDatabase%2Fsrc%2FStorageManager.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A3%2C%22character%22%3A18%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fharounguessous%2FDesktop%2FLearning%2FDatabase%2Fsrc%2FUtils.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A19%2C%22character%22%3A4%7D%7D%5D%2C%22165ee369-be5c-4e1a-9973-a368ee70b7a8%22%5D "Go to definition"), and [`cleanInput`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fharounguessous%2FDesktop%2FLearning%2FDatabase%2Fsrc%2Fcommands.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A1%2C%22character%22%3A27%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fharounguessous%2FDesktop%2FLearning%2FDatabase%2Fsrc%2FUtils.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A35%2C%22character%22%3A4%7D%7D%5D%2C%22165ee369-be5c-4e1a-9973-a368ee70b7a8%22%5D "Go to definition").

- **Tests/**: Contains unit tests for the project.
  - 

StorageManagerTest.py

: Unit tests for the [`StorageManager`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fharounguessous%2FDesktop%2FLearning%2FDatabase%2Fsrc%2Fcommands.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A0%2C%22character%22%3A5%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fharounguessous%2FDesktop%2FLearning%2FDatabase%2Fsrc%2FStorageManager.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A4%2C%22character%22%3A6%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fharounguessous%2FDesktop%2FLearning%2FDatabase%2FTests%2FStorageManagerTest.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A6%2C%22character%22%3A5%7D%7D%5D%2C%22165ee369-be5c-4e1a-9973-a368ee70b7a8%22%5D "Go to definition") class.

## Usage

### Running the Application

To run the application, use the following command:

```sh
python src/main.py <command> <arguments>
```

### Commands

- **INSERT**: Insert row values into a table.
  ```sh
  python src/main.py insert <row_values> into <table_name> format <column_format>
  ```

- **SELECT**: Select row values from a table.
  ```sh
  python src/main.py select <row_values> from <table_name> where <conditional>
  ```

- **CREATE**: Create a new table.
  ```sh
  python src/main.py create table <table_name> <columns>
  ```

- **REMOVE**: Remove rows from a table based on a condition.
  ```sh
  python src/main.py remove <table_name> where <conditional>
  ```

- **DELETE**: Delete a table.
  ```sh
  python src/main.py delete <table_name>
  ```

- **HELP**: Display help information.
  ```sh
  python src/main.py help
  ```

### Running Tests

To run the unit tests, use the following command:

```sh
python -m unittest discover -s Tests
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- [Tabulate](https://pypi.org/project/tabulate/) for pretty-printing tables.
- Python's [`unittest`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fharounguessous%2FDesktop%2FLearning%2FDatabase%2FTests%2FStorageManagerTest.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A0%2C%22character%22%3A7%7D%7D%5D%2C%22165ee369-be5c-4e1a-9973-a368ee70b7a8%22%5D "Go to definition") module for testing.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
