from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError,BooleanField
from wtforms.validators import InputRequired,Email,EqualTo
from ..models import Blog

class BlogForm(FlaskForm):
  title = StringField('Enter title',validators = [InputRequired()])
  subtitle= StringField('Enter subtitle',validators = [InputRequired()])
  content = TextAreaField('make a blog', validators=[InputRequired()])
  submit = SubmitField('Post Blog')

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment')
    submit = SubmitField('Submit')
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')


