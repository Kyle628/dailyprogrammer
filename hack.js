library = [{title: "The Hobbit", available: true},
           {title: "Great Gatsby", available: true},
           {title: "Gone With The Wind", available: true}];


function searchLibrary(title) {
    for (var i = 0; i < library.length; i++) {
        if (library[i]['title'] == title) {
            return library[i];
        }
    }
    return false;
}

function assert(expectedBehavior, descriptionOfBehavior) {
    if (!expectedBehavior) {
        console.log(descriptionOfBehavior);
    } else {
        console.log("test passed");
    }
}

assert(searchLibrary("The Hobbit") == library[0], "should have found this book in the library");

assert(searchLibrary("dsfjkavnjkdfv") == false, "should not have found this book in library");

function checkOut(title) {
    if (!searchLibrary(title)) {
        return false;
    }
    if (searchLibrary(title)['available'] == true) {
        searchLibrary(title)['available'] = false;
        return "book available";
    } else {
        return "unavailable";
    }
    // return false if book isn't in library
    // return book available if available
    // return "unavailable" if book not available
}

assert(checkOut("dsjghdkjdg") == false, "should not find this book");

assert(checkOut("The Hobbit") == "book available", "should have found book");

checkOut("Great Gatsby");
assert(checkOut("Great Gatsby") == "unavailable", "should not have been able to check this book out");
