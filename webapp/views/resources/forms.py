from wtforms import (
    StringField, SelectField, RadioField, HiddenField
)

from wtforms.validators import (
    InputRequired, Optional, Regexp
)

from wtforms.widgets import TextArea

from webapp.home.custom_validators import (
    valid_min_length
)

from webapp.home.intellectual_rights import (
    INTELLECTUAL_RIGHTS_CC0, INTELLECTUAL_RIGHTS_CC_BY
)

from webapp.home.forms import EDIForm


class AbstractForm(EDIForm):
    abstract = StringField('Abstract', widget=TextArea(),
                           validators=[Optional(), valid_min_length(min=20)])
    md5 = HiddenField('')


class IntellectualRightsForm(EDIForm):
    intellectual_rights_radio = RadioField('Intellectual Rights',
                                           choices=[("CC0", INTELLECTUAL_RIGHTS_CC0),
                                                    ("CCBY", INTELLECTUAL_RIGHTS_CC_BY),
                                                    ("Other", "Other (Enter text below)")
                                                    ], validators=[InputRequired()])
    intellectual_rights = StringField('', widget=TextArea(), validators=[])
    md5 = HiddenField('')


class KeywordSelectForm(EDIForm):
    pass


class KeywordForm(EDIForm):
    keyword = StringField('Keyword', validators=[])
    keyword_type = SelectField('Keyword Type (Optional)',
                               choices=[("", ""),
                                        ("place", "place"),
                                        ("stratum", "stratum"),
                                        ("taxonomic", "taxonomic"),
                                        ("temporal", "temporal"),
                                        ("theme", "theme")])
    md5 = HiddenField('')


class PubDateForm(EDIForm):
    pubdate = StringField('Publication Date',
                          validators=[Optional(), Regexp(r'^(\d\d\d\d)-(01|02|03|04|05|06|07|08|09|10|11|12)-(0[1-9]|[1-2]\d|30|31)|(\d\d\d\d)$', message='Invalid date format')])
    md5 = HiddenField('')


class PublicationPlaceForm(EDIForm):
    pubplace = StringField('Publication Place', validators=[])
    md5 = HiddenField('')


class TitleForm(EDIForm):
    title = StringField('Title', validators=[valid_min_length(min=20)])
    md5 = HiddenField('')
