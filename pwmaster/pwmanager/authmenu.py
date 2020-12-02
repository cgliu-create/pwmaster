from django.shortcuts import render

def mergeDict(x, y):
    z = x.copy()
    z.update(y)
    return z 

def renderauth(request, template_path, more_context={}):
    nava = {'signout':False, 'signin':True, 'signup':True}
    navb = {'signout':True, 'signin':False, 'signup':False}
    if not request.user.is_authenticated:
        loggedOutContext = mergeDict(nava, more_context)
        return render(request=request, template_name=template_path, context=loggedOutContext)
    if request.user.is_authenticated:
        loggedInContext = mergeDict(navb, more_context)
        return render(request=request, template_name=template_path, context=loggedInContext)
