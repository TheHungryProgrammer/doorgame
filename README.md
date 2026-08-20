# doorgame
A simple game to showcase my OOP design skillset.
Initially when I first began programming, the example that helped me understand OOP design was by thinking about doors:

A door is an object that may have a locked state, and a key object to turn the locked state to unlocked.
I decided to take that idea as a project and make a simple game out of it.

The objective of the game is simple, and a re-imagining of the classic Monty Hall problem: There are 3 doors, 2 are locked, one is not. One has a treasure; the others are empty. Choose right and win.

Please note that I utilized Claude LLM for use in bug hunting and code design. While claude assisted me in finishing my project, the only parts that have been 'copy/pasted' are the method names and descriptions in the game class. All other code is my own, and should serve as a showcase of my work, as well as my ability to work with an LLM to finish a project speedily.

There are 4 classes:
Main1
- This file I created with my own code design, with minor bug hunting help from claude. It's where I run my portion of the game, and while it works, claude noted that it was messy and suggested separating all of that code into a separate game class (described below), and leaving main as a simple class with only 2 calls.

Game & Main2
- This class is what claude suggested I switch to. The code is cleaner, more organized, and taught me a lot about how I need to code going forward. I asked claude not to give me any code for this class, only to suggest where to start. As such claude only assisted in giving me the method names, and a short description of what each should do. The internal code of each method is my own. 

Door
- This class defines what a door is, what state it should be in, and what it should do. What color is it? Is it open? Is it locked? Does it have a treasure? 

Key
- This class contains our key, its a simple class because a Key really only needs to have a unique identifier, the door class should make sure that the key unlocks it if possible.

- To run the game you will need to have version 3.14.6 of Python. You can check if you have the python package by using: 

```py --python```

- You can run the program in either instance.

to run my original code:
```py main1.py```

to run the claude assisted game class
```py.main2.py```

<img width="566" height="144" alt="image" src="https://github.com/user-attachments/assets/653160fc-e291-484f-a255-06344ce076fb" />

Make your choice as yes to play, anything else quits the game. Continuing with Yes:

<img width="749" height="78" alt="image" src="https://github.com/user-attachments/assets/fe126e95-fbf0-4fe1-840e-858b24eaa9db" />

Make your final choice:

<img width="383" height="87" alt="image" src="https://github.com/user-attachments/assets/bd75f6be-14f7-4f27-8402-a4fd78d0fcde" />

Thanks for checking out my code and my simple game.
