window.addEventListener("load" , function ()
{
    // Get click counter
    let clickcounterelement = document.getElementById("click-counter");
    let clickbuttonelement = document.getElementById("click-button");

    // Counter Value
    let counter = 0;

    // Click button function
    let clickbuttonfunction = function()
    {
        // Increment Counter
        counter++;

        // Update Counter Value
        clickcounterelement.innerHTML = counter;
    };

    // Attach button function
    clickbuttonelement.addEventListener("click", clickbuttonfunction);
});