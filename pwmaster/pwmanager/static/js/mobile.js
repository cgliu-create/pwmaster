document.addEventListener("DOMContentLoaded", () => {

    var coll = document.getElementsByClassName("collapsible");
    var i;
    
    for (i = 0; i < coll.length; i++) {
      coll[i].addEventListener("click", function() {
        var content = this.nextElementSibling;
        if (content.style.display != "none") {
          content.style.display = "none";
        } else {
          content.style.display = "block";
        }
      });
    }
    
    var hamburger = document.getElementById("hamburger");
    hamburger.addEventListener("click", function() {
    var x = document.getElementById("mobilenav");
      if (x.style.display != "none") {
        x.style.display = "none";
      } else {
        x.style.display = "inline-flex";
        x.style.flexDirection = "column";
      }
    });
  
  
  });
  
  