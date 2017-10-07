# -*- coding: utf-8 -*-
# try something like
import operator


def polarion_display_form():
    form = SQLFORM(db.polarion)
    if form.process().accepted:
        session.flash = 'form accepted'
        redirect(URL('polarion_view'))
    elif form.errors:
        response.flash = 'form has error'
    else:
        response.flash = 'please fill out the form'
    return locals()


def polarion_view():
    rows = db(db.polarion).select()
    print rows[0].TC_ID
    rows = sorted(rows, key=lambda k: k['TC_ID'])
    return locals()

def index(): return dict(message="hello from polarion.py")
