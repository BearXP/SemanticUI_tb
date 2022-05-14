# Semantic UI Testbed
> ~~https://semantic-ui.com/introduction/advanced-usage.html~~  
> https://fomantic-ui.com/introduction/advanced-usage.html  
> https://github.com/BearXP/SemanticUI_tb
-----------

## Background
I want to have a web page where users upload data, I process it in the background, and return the processed data.  
Unfortunately the processing takes a bit of time (a few minutes), and it's unfortunate that the end user has to just sit there, unsure whether something has crashed..

## Requirements:
| Status | ID | Requirement | Resolution |
|:--:|:--:|---|---|
| ✅ | 1 | The webpage must be via by Flask to match the rest of the project | See main.py |
| ✅ | 2 | The web page must have inhereted headers. I want to reuse the header banner on other pages. | See `base.html`, `UploadWhereUsed.html`, and `main.py` |
| ✅ | 3 | The css library must support 'steps' showing which step is being processed | See CSS library below |
| ✅ | 4 | The css library must support 'progress bars' | See CSS library below|
| - | 5 | The test bed must show updates to the status of the progress | |
| - | 6 | The 'Start work' button must disappear when processing begins | |
| - | 7 | The 'Progress' must only appear when processing is happening, i.e. not on startup | |
| - | 8 | I would like to learn jQuery, so all client code is to be in jQuery | |
| - | 9 | The website is to be pretty, both on desktop and mobile. I don't expect mobile users, but I do want to have a website that actually looks nice for a change | |



## Plan of attack.
### CSS Library
Step 0 has been to look at different CSS libraries for this project.  
Looking at Tailwind, Bootstrap, Bulma, etc, I can see a lot of options available for me, but semantic-ui seems to have everything I want out of the box.

Unfortunately semantic-ui is apparently [abandoned](https://github.com/fomantic/Fomantic-UI-Docs/), the last update was 4 years ago, on 22/Oct/2018.  
It looks like there's a fork called [fomantic-ui](https://fomantic-ui.com/) which seems to still be active. The last release was almost a year ago, but I can see commits as recently as 18 hours ago, which is promising.

### Steps 1 onwards:

Note, I've pushed as much of the flask stuff as possible until the end. This is intentional. **LEARN jQUERY MARK**!

|Status|Step|Reference|
|:---:|---|---|
| ✅ | Install Flask | `pip install flask` |
| ✅ | Setup flask to return a empty web page </br> > *See `/`,  `/hello`, and `/hello/bear`* | [Flask - First Application](https://www.geeksforgeeks.org/flask-creating-first-simple-application/) </br> [Flask Quickstart - rendering-templates](https://flask.palletsprojects.com/en/2.1.x/quickstart/#rendering-templates) |
| ✅ | Setup a template with the Semantic CDN , headers, ~~and footers~~ | [CDN Link](https://fomantic-ui.com/introduction/advanced-usage.html#cdn-releases) </br> [Flask - Templates](https://flask.palletsprojects.com/en/2.1.x/tutorial/templates/) |
| ✅ |  Setup a dummy page with a 'start work' button, and hidden progress bars | [HTML Cheat Sheet - Hidden Elements](https://htmlcheatsheet.com/) </br> [Semantic - Steps](https://fomantic-ui.com/elements/step.html) </br> [Semantic - Progress Bar](https://fomantic-ui.com/modules/progress.html) |
| ✅ | Learn how to send the 'start work' command to flask </br>  - I may need to set up a cookie so the site / server know which file it asked for? | |
| - | Learn how to query the status of the process using jQuery </br>  - I may need to set up a cookie so the site / server know which file it asked for? | [Flask - Cookies](https://flask.palletsprojects.com/en/2.1.x/quickstart/#cookies) </br> [Repeated Queries](https://stackoverflow.com/questions/5140939/repeat-jquery-ajax-call#5140963)|
| - | Learn how to animate the introduction of the progress bars </br> `$("#demo").fadeIn();  // fade in a hidden ID` | [jQuery Cheat Sheet](https://htmlcheatsheet.com/jquery/) |
| - | Learn what Blueprints are? | [Instructables - Blueprints](https://www.instructables.com/Setting-Up-a-Flask-Application/) </br> [Flask - Blueprints](https://flask.palletsprojects.com/en/2.1.x/tutorial/views/) |
| - | Set up dummy processing in flask |   |
| - | Set up status responses in flask | [Flask API](https://flask.palletsprojects.com/en/2.1.x/quickstart/#apis-with-json) |
| - | Learn how to query the status from jQuery | |

## Lessons learnt
### Process
- **Forcing myself to write down the 'plan of attack'** seems helpful up front, my development process could be described as 'interrupted', and I feel better about the idea that future me can pick things up.
- This is my first time working entirely from VS Code. `Control ~` opens the terminal window and let me `python -m venv venv`, so I didn't need to have a separate command prompt open. ~~~Wish me luck with the git push, without having actually set it up in github prior~~~ - It worked great!.
- I had all the requirements in my head when I started, but I'm not convinced I'll remember them in a weeks time. I'm also concerned that I'll trip over steps, and forget why they exist. I think 'Requirements' are a nice checklist at the end of the project to make sure I didn't skip anything.

### Markdown
- Adding the links seemed useful initially, I've just been doing a bit of initial research, and didn't want that to go to waste when I closed my web browser. But I think my implementation may have been... naive. It really interrupts the flow of the to do list, making it hard to tell at a glance what's happening.
  - It's SOOOO nice being able to just have a few tabs open, rather than needing to keep my PC on for weeks at a time as I work on something! And it's quicker to jump between things I need.
  - Moving it to a **table makes it much easier to read** when rendered. It's a pain in markdown.
- You can use Windows' `Control ;` emoji and it renders in VS Code & github fine, that's how I got the ✅ in the Status column.
- Always search for a [cheat sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#links)
- I feel like I'm learning bits and pieces of html while I'm here, with the `</br>` and all...

### ~~Semantic~~ Fomantic
 - Just **steal the sample code from their demo page**. On their demo page they're like 'It's just this one line and look at the results!', but then you find out they have animations, etc, added which isn't in the demo code. `Right click > inspect` for the win!
 - That also applies to formatting for the paragraphs.
 - Fomantic has more features than Semantic did, and it was just lucky that I was looking through Reddit and saw that Semantic was abandoned.
   - Maybe I should check these sorts of things before I start? Usually I don't bother with forks. And frankly most of the changes I had to make to update it was in this README.md, the code itself had less changes..
   - Or care less about that sort of thing. [nes.css](https://github.com/nostalgic-css/NES.css/) hasn't been updated in 10 months, but I think I could still have fun. 

