> https://ihatetomatoes.net/jquery-complete-beginners-datatypes-selectors/
> https://www.educba.com/jquery-if-statement/

## Setup
You can choose several sources for the jQuery library, I just didn't want to use google, so I chose the first one.
```html
<script src="https://code.jquery.com/jquery-latest.min.js" type="text/javascript"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
```

## Debugging
It's ugly, but:
> https://ihatetomatoes.net/jquery-for-complete-beginners-console-log-scrolltop/
```javascript
alert('your message');
console.log('your message');
```



## Selectors
Selectors tell the javascript what to respond to

> Writing all your code inside of the $(document).ready function will make sure that the code is executed **after the page is fully loaded**

```javascript
$(document).ready(function() {
    //start writing your javascript code here
    var pageWidth = 500,                         // Number
        message = 'this is our new message',     // String
        html = '<strong>content</strong>',       // htmlString
        animating = true,                        // Boolean - true or false
        object = {},                             // Object
        array = [1,2,3];                         // Array
    $('h1') // Selects the h1 element
    $('#intro') // Selects the element with id="intro"
    $('#gallery li') // Selects every list item within the id="gallery"
    $('#gallery .galleryItem') // Selects all elements with class galleryItems, inside the element with the id gallery
    $('.galleryItem') // Also selects every list item within the gallery

    //selects the first list item within the gallery
    $("#gallery li").eq(0)
    
    //selects the second list item within the gallery
    $("#gallery li").eq(1)
    
    //selects the last list item within the gallery
    $("#gallery li").eq(-1)
    
    // selects the list item containing a word 'dolor'
    $("li:contains('dolor')")
    
    // selects all links to https://ihatetomatoes.net
    $("a[href='https://ihatetomatoes.net']")
    
    // selects link who's href starts with https://ihatetomatoes.net
    $("a[href^='https://ihatetomatoes.net']")
    
    // selects all links inside any ol on the page
    $("#page-content ol").find("a")
    
    // this would select li and p elements
    $(".highlight").parent()
    
    // this would select ul which is a parent of span with class highlight
    $(".highlight").parents("ul")
});
```

## Reacting to changes
### Typing
> https://www.w3schools.com/jquery/tryit.asp?filename=tryjquery_event_keypress

Note: This doesn't seem to react to deleting keys?

```javascript
<script>
i = 0;
$(document).ready(function(){
  $("input").keypress(function(){
    $("span").text(i += 1);
  });
});
</script>
```

### Button Clicks
> https://www.w3schools.com/jquery/tryit.asp?filename=tryjquery_event_keypress_trigger

```javascript
<script>
i = 0;
$(document).ready(function(){
  $("p").keypress(function(){
    $("span").text(i += 1);
  });
  $("button").click(function(){
    $("p").keypress();
  });
});
</script>
```