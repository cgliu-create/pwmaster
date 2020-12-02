function showIt(id){
    let element = document.getElementById(id);
    if (element == null){ return}
    element.style.display = 'block'
}
function dontShowIt(id){
    let element = document.getElementById(id);
    if (element == null){ return}
    element.style.display = 'none'
}

function closeNav(){
    var x = document.getElementById("mobilenav");
    if (x.style.display != "none") {
      x.style.display = "none";
    } 
}

document.addEventListener("DOMContentLoaded", () => {
    if (document.getElementById('addpassword')){
        document.getElementById('addpassword').onclick = () => {
            showIt('passwordform');
        };
    }
    if (document.getElementById('addpasswordcancel')){
        document.getElementById('addpasswordcancel').onclick = () => {
            dontShowIt('passwordform');
        };
    }
    if (document.getElementById('changepassword')){
        document.getElementById('changepassword').onclick = () => {
            showIt('changeform');
        };
    }
    if (document.getElementById('changecancel')){
        document.getElementById('changecancel').onclick = () => {
            dontShowIt('changeform');
        };
    }
    if (document.getElementById('deletepassword')){
        document.getElementById('deletepassword').onclick = () => {
            showIt('deleteform');
        };
    }
    if (document.getElementById('deletecancel')){
        document.getElementById('deletecancel').onclick = () => {
            dontShowIt('deleteform');
        };
    }
    if (document.getElementById('signinA')){
        document.getElementById('signinA').onclick = () => {
            showIt('signinform');
            closeNav();
        };
    }
    if (document.getElementById('signinB')){
        document.getElementById('signinB').onclick = () => {
            showIt('signinform');
            closeNav();
        };
    }
    if (document.getElementById('signupA')){
        document.getElementById('signupA').onclick = () => {
            showIt('signupform');
            closeNav();
        };
    }
    if (document.getElementById('signupB')){
        document.getElementById('signupB').onclick = () => {
            showIt('signupform');
            closeNav();
        };
    } 
    if (document.getElementById('signincancel')){
        document.getElementById('signincancel').onclick = () => {
            dontShowIt('signinform');
            closeNav();
        };
    } 
    if (document.getElementById('signupcancel')){
        document.getElementById('signupcancel').onclick = () => {
            dontShowIt('signupform');
            closeNav();
        };
    } 
});