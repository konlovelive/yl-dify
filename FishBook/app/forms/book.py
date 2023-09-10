from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForm(Form):
    #DataRequired是为了处理没有输入关键字但是输入了页码时，空格被当做索引值的情况
    q=StringField(validators=[DataRequired(),Length(min=1,max=30)])
    page=IntegerField(validators=[NumberRange(min=1,max=99)],default=1)