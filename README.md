# Semantic UI Testbed
> https://semantic-ui.com/introduction/advanced-usage.html  
> https://github.com/BearXP/SemanticUI_tb
-----------

## Background
I want to have a web page where users upload data, I process it in the background, and return the processed data.  
Unfortunately the processing takes a bit of time (a few minutes), and it's unfortunate that the end user has to just sit there, unsure whether something has crashed..

Looking at Tailwind, Bootstrap, Bulma, etc, I can see a lot of options available for me, but semantic-ui seems to have everything I want (?)

## Plan of attack.

|Status|Step|Reference|
|:---:|---|---|
| ✅ | Install Flask | `pip install flask` |
| ✅ | Setup flask to return a empty web page </br> See `/`,  `/hello`, and `/hello/bear` | [Flask - First Application](https://www.geeksforgeeks.org/flask-creating-first-simple-application/) </br> [Flask Quickstart - rendering-templates](https://flask.palletsprojects.com/en/2.1.x/quickstart/#rendering-templates) |
| - | Learn what Blueprints are? | [Flask - Blueprints](https://www.instructables.com/Setting-Up-a-Flask-Application/) |
| - | Setup a template with the Semantic CDN , headers, and footers | [CDN Link](https://semantic-ui.com/introduction/advanced-usage.html#cdn-releases) |
| - |  Setup a dummy page with a 'start work' button, and hidden progress bars | [HTML Cheat Sheet - Hidden Elements](https://htmlcheatsheet.com/) </br> [Semantic - Steps](https://semantic-ui.com/elements/step.html) </br> [Semantic - Progress Bar](https://semantic-ui.com/modules/progress.html) |
| - | Learn how to send the 'start work' command to flask </br>  - I may need to set up a cookie so the site / server know which file it asked for? | [Flask - Cookies](https://flask.palletsprojects.com/en/2.1.x/quickstart/#cookies) |
| - | Learn how to animate the introduction of the progress bars </br> `$("#demo").fadeIn();  // fade in a hidden ID` | [jQuery Cheat Sheet](https://htmlcheatsheet.com/jquery/) |
| - | Set up dummy processing in flask |   |
| - | Set up status responses in flask | [Flask API](https://flask.palletsprojects.com/en/2.1.x/quickstart/#apis-with-json) |
| - | Learn how to query the status from jQuery | |

## Lessons learnt
### Process
- **Forcing myself to write down the 'plan of attack'** seems helpful up front, my development process could be described as 'interrupted', and I feel better about the idea that future me can pick things up.

- This is my first time working entirely from VS Code. `Control ~` opens the terminal window and let me `python -m venv venv`, so I didn't need to have a separate command prompt open. ~~~Wish me luck with the git push, without having actually set it up in github prior~~~ - It worked great!.

### Markdown
- Adding the links seemed useful initially, I've just been doing a bit of initial research, and didn't want that to go to waste when I closed my web browser. But I think my implementation may have been... naive. It really interrupts the flow of the to do list, making it hard to tell at a glance what's happening.
  - Moving it to a **table makes it much easier to read** when rendered. It's a pain in markdown.
- You can use Windows' `Control ;` emoji and it renders in VS Code & github fine, that's how I got the ✅ in the Status column.