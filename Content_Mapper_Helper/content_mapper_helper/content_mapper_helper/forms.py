from flask.ext.wtf import Form
from wtforms import fields,validators,HiddenField,SelectField,SubmitField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from .models import Section,SectionContent,Docs,Gaps

class SectionForm(Form):
    '''SectionForm with attribute Section Title'''
    SectionTitle = fields.StringField('Section Title')
   
   
class SectionContentForm(Form):
    '''SectionContent Form with attributes Section_Title & Scenario_Name- Select Fields , ScenarioName, Description - TextFields'''
    Section_Title = QuerySelectField(query_factory=lambda: Section.query.all(),get_label='SectionTitle',allow_blank=True,blank_text=('Select a Section Title'))
    ScenarioName = fields.StringField('Scenario Name')
    Description = fields.StringField(render_kw={'disabled':''})
    Scenario_Name = QuerySelectField(query_factory=lambda:SectionContent.query.all(),get_label='ScenarioName',allow_blank=True,blank_text=('Select a ScenarioName'))
   
    
class DocsForm(Form):
    '''Docs Form has two attributes Name , Link- TextFields'''
    Name = fields.StringField()
    Link = fields.StringField()

class GapsForm(Form):
    '''Gaps Form has two attributes GapDescription , Url- TextFields
    According to schemaversion-2.0 , Gaps has additional fields - VSTSLink, CreationDate, Tags, Categories and Hackevent details as list of key value pair in 'Sources'
    These fields need to be added to follow schema version 2:0. This follows Schema version-1:0
    '''

    GapDescription= fields.StringField()
    Url = fields.StringField() 


