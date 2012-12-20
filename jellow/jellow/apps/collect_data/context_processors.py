from collect_data.forms import RatingForm

def rating_form(request):
    return {'rating_form': RatingForm()}
