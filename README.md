<h1 align="center">
    Credito
</h1>

<br/>

<div align="center">
 
## Credito is a program to make **instant** credits in any Python app.
`pip install credito`

<div align="center">
  <img alt="GitHub Issues or Pull Requests" src="https://img.shields.io/github/issues/james-beans/credito?style=for-the-badge&logo=Github">
  <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/james-beans/credito?style=for-the-badge&logo=Github">
  <img alt="GitHub Issues or Pull Requests" src="https://img.shields.io/github/issues-closed/james-beans/credito?style=for-the-badge&logo=Github">
  <br>
  <a href="https://pypi.org/project/credito/"><img alt="Python Version" src="https://img.shields.io/pypi/pyversions/credito?style=for-the-badge&logo=Pypi&logoColor=white"></a>
  <br>
  <a href="https://pypi.org/project/credito/"><img alt="88x31" src="https://licensebuttons.net/l/by-sa/4.0/88x31.png"></a>
</div>


</div>
 
<hr>
<div align="center">

# License
This project is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License. See [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) for details.
</div>
<hr>

<div align="left">

# Documentation
## Install with:

`pip3 install credito`
`pip install credito`

## Configure and Use `credito`:

## 1. Import and Configure the Module:

You can import `credito` from the `credito` package and configure it with the path to your custom `credits.cfg` file. If you don’t specify a path, the default `credits.cfg` file included in the package will be used.

```
from credito import Credito

# Create an instance of Credito
credito = Credito()

# If you put nothing in the brackets then it will
# automatically use the default credits.cfg file included in the package.
credito.config()
# Or,
# Configure with a custom credits.cfg file
credito.config('path/to/your/custom/credits.cfg')
```


## 2. Start the Handler:
To start listening for the key combination **(CTRL + O)** and display the credits, you can call the `handler` function.
```
credito.handler()
```

## 3. Run the Module:
To have `credito` run in the background and listen for the key combination, you can run it as a standalone script or integrate it into your application.

If running as a standalone script, you can simply execute:
```
python -m credito
```
Or, integrate it into your application by calling the `handler` function as shown above.

<hr>
</div>
<div align="left">

# How the Printing Works:

## 1. Configuration `(credito.config)`:
- When you call `credito.config("path/to/custom/credits.cfg")`, it loads the content of the `credits.cfg` file into memory by reading it and storing the content in the `self.credits` variable.
- If you don't pass a path to the `config` function, it will use the default `credits.cfg` file included in the package.

## 2. Keypress Handler(`handler`):
- When the `CTRL + O` key combination is detected by the `listen_for_keypress` function, it triggers the `handler()` function. The handler() function, in turn, calls `credito.show_credits()`.

## 3. Displaying Credits (`show_credits`):
- Inside `show_credits()`, the console is cleared using `os.system('cls' if os.name == 'nt' else 'clear')`, and then the content of `self.credits` (which contains the content from `credits.cfg`) is printed.
- The program pauses for 10 seconds (`time.sleep(10)`), allowing the user to see the credits, and then it optionally clears the screen again.

<hr>

<div align="left">

# Additional Notes

## Running in Background:
- The listen_for_keypress function runs in a separate thread, so the main program remains responsive. Make sure to handle this appropriately in your application.

## No cross platform:
- Don't ask me to add cross platform. I am way too busy to be doing that. It might work cross platform it's just I can't test it and it might not be reliable. Credito was made to work for **Windows** only. The example provided is tailored for Windows using `ctypes`. If you need cross-platform support, you may need to use different libraries or methods to handle global keypress events on other operating systems. 

## Permissions:
- Capturing global keypresses might require administrative or elevated permissions depending on the system and environment.

## Credits printing:
- Credito will print everything in the `credits.cfg` file. The `credits.cfg` file is like a text document for Credito. Make sure the file has the content you want to display, and that it is correctly loaded into the config using the method shown in the documentation above. The Credits will allways be visible for 10 seconds, then either the console will clear again, or the terminal application will resume as normal.

## What is the default/auto config?
```
Thank you for using our application!

Credits:
- Developer: Your Name
- Support: support@example.com

Enjoy using our software!
```

- I chose this so it could be a template for easy testing. You are free to copy and change the default/auto config.


</div>

</div>

<hr>

<div align="left">

## Directory Structure:

```
credito/ - # Base directory
├── credito/ - # Main package folder
│   ├── __init__.py - # Initializes the package
│   ├── credito.py - # Contains the Credito class and logic
│   └── data/ - # Contains seperate info
│       └── credits.cfg - # Default credits file 
├── tests/ - # Tests folder
│   ├── __init__.py - # Can be empty or contain shared fixtures
│   ├── conftest.py - # Global fixtures and hooks for tests
│   ├── test_credito.py - # Unit tests for Credito class
├── README.md - # Project description
├── setup.py - # Setup script for packaging
└── LICENSE - # Obviously just a license
```

</div>

<hr>

<div align="center">
    
⚡ **Quote**<br> "Talk is cheap. Show me the code." <br> **-- Linus Torvalds --**

</div>

<br/>
