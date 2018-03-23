from flask import Blueprint, flash, Markup, redirect, render_template, url_for,request,jsonify

from .forms import SectionForm,SectionContentForm,DocsForm,GapsForm
from .models import db, query_to_list, Section, SectionContent,Docs,Gaps


Contentmapperhelper = Blueprint("Contentmapperhelper", __name__)


@Contentmapperhelper.route("/")
def index():
    section_form = SectionForm()
    sc_form = SectionContentForm()
    doc_form=DocsForm()
    gap_form=GapsForm()
    
    return render_template("index.html",
                           section_form=section_form,
                           sc_form=sc_form,
                           doc_form=doc_form,
                           gap_form=gap_form)
                           


@Contentmapperhelper.route("/section", methods=("POST", ))
def add_section():
    '''Adds Section Title'''
    form = SectionForm()
    if form.validate_on_submit():
        section = Section()
        form.populate_obj(section)
        db.session.add(section)
        db.session.commit()
        flash("Added section")
        return redirect(url_for(".index"))

    return render_template("validation_error.html", form=form)


@Contentmapperhelper.route("/sectioncontent", methods=("POST",))
@Contentmapperhelper.route("/section/<int:section_id>/sectioncontent", methods=("POST",))
def add_sectioncontent(section_id=None):
    '''Add Scenarios, Description '''
    if section_id is None:
       
        form = SectionContentForm()
    else:
        section = Section.query.get_or_404(section_id)
        
        form = SectionContentForm(csrf_enabled=False, section=section)

    if form.validate_on_submit():
        sectioncontent=SectionContent()
        form.populate_obj(sectioncontent)
        sectioncontent.section_id = form.section.data.id
        db.session.add(sectioncontent)
        db.session.commit()
        flash("Added scenario,description for section {}".format(form.section.data.SectionTitle))
        return redirect(url_for(".index"))

    return render_template("validation_error.html", form=form)


@Contentmapperhelper.route("/doc", methods=("POST",))
@Contentmapperhelper.route("/sectioncontent/<int:sectioncontent_id>/doc", methods=("POST",))
def add_docs():
    '''Add Name, Link'''
    form = DocsForm()
    if form.validate_on_submit():
        doc = Docs()
        form.populate_obj(doc)
        db.session.add(doc)
        db.session.commit()
        flash("Added Docs")
        return redirect(url_for(".index"))

    return render_template("validation_error.html", form=form)

@Contentmapperhelper.route("/gap", methods=("POST",))
@Contentmapperhelper.route("/sectioncontent/<int:sectioncontent_id>/gap", methods=("POST",))
def add_gaps():
    '''Add GapDescription, Url'''
    form = GapsForm()
    if form.validate_on_submit():
        gap = Gaps()
        form.populate_obj(gap)
        db.session.add(gap)
        db.session.commit()
        flash("Added Gaps")
        return redirect(url_for(".index"))

    return render_template("validation_error.html", form=form)






