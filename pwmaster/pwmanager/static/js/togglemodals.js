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

document.addEventListener("DOMContentLoaded", () => {
    document.getElementById('signinA').onclick = () => {
        showIt('signinform');
    };
    document.getElementById('signinB').onclick = () => {
        showIt('signinform');
    };
    document.getElementById('signupA').onclick = () => {
        showIt('signupform');
    };
    document.getElementById('signupB').onclick = () => {
        showIt('signupform');
    };

    document.getElementById('signincancel').onclick = () => {
        dontShowIt('signinform');
    };
    document.getElementById('signupcancel').onclick = () => {
        dontShowIt('signupform');
    };

    document.getElementById('addpassword').onclick = () => {
        showIt('passwordform');
    };
    document.getElementById('generatepassword').onclick = () => {
        showIt('generateform');
    };
    
    document.getElementById('addpasswordcancel').onclick = () => {
        dontShowIt('passwordform');
    };
    document.getElementById('generatepasswordcancel').onclick = () => {
        dontShowIt('generateform');
    };
});