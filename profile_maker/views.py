from django.shortcuts import render
from .forms import Profile_Form
from .models import User_Profile

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


def create_profile(request):
    form = Profile_Form()
    if request.method == 'POST':
        form = Profile_Form(request.POST, request.FILES)
        if form.is_valid():
            user_pr = form.save(commit=False)
            user_pr.display_picture = request.FILES['display_picture']
            file_type = user_pr.display_picture.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                return render(request, 'profile_maker/error.html')
            user_pr.save()
            return render(request, 'profile_maker/details.html', {'user_pr': user_pr})
    context = {"form": form,}
    return render(request, 'profile_maker/create.html', context)


# The views are simple to understand. We have imported the models and forms in this view file. Then we have defined a list IMAGE_FILE_TYPES. We use it to check the type of file.

# Then our function definition starts.

# In this function, we have defined a form object. It will render a form. Then we are using form validation to clean our form data. This function returns True or False. If the form has valid data, we can store the data locally. Then we are extracting the file type uploaded by the user.

# Since we are using file field, we have multiple attributes. The file URL contains the filetype after the ‘.’. We have used a basic string function split() for this purpose.

# The split() will split the string into parts where ‘.’ is present. You can get more on this in basic Python functions. In the next line, we are making it a lower type string. Then we are performing a check whether the file is an image file or not. We can skip this part if we use the image field.

# So, if the file is not an image file, it will render error.html.

# Otherwise, it will render details.html, showing the details we just filled. If the form is rendered for the first time, it will render create.html. Now, we understood the view function. Let’s make our templates.