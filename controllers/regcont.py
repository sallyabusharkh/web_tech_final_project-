
def home():
    login=False
    return locals()

def courses():
    grid = SQLFORM.grid(db.courses)
    return dict(grid=grid)

def addcourse():
    form = SQLFORM(db.courses)
    if form.process().accepted:
       response.flash = 'your form has accepted'
    elif form.errors:
        response.flash = 'form has errors ,please fixed your errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form)

def addSchedule():
    form = SQLFORM(db.coursessechedules)
    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form)


def schedules():
    grid = SQLFORM.grid(db.coursessechedules, csv=False)
    return dict(grid=grid)




def myCourses():
    auth.settings.expiration = 1
    return locals()
    


def analysis():         
    userCount=db(db.auth_user.id).count()
    return locals()

