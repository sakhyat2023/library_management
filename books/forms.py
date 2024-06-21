from django import forms
from .models import ReviewModel

class UserCommentFrom(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 6}),
        error_messages={
            'required': "You can't submit an empty comment. Please write something."
        }
    )
    class Meta:
        model = ReviewModel
        fields = ["content"]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {
                    "class": "px-0 w-full text-sm text-gray-900 border-0 focus:ring-0 focus:outline-none dark:text-white dark:placeholder-gray-400 dark:bg-gray-800",
                    "placeholder": "Write a comment...",
                },
                
            )