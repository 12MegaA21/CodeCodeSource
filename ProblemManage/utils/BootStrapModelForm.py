from django import forms

class BootStrap:
    exclude_field = ['img', 'logo']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # 初始化父类
        # 如果本身样式里有值，则保留其他原来的属性，修改需要指定的属性，否则则直接设置
        for name, field in self.fields.items():
            if name in self.exclude_field:
                continue
            if field.widget.attrs:
                field.widget.attrs["class"] = "form-control"
                field.widget.attrs["placeholder"] = field.label
            else:
                field.widget.attrs = {"class": "form-control", "placeholder": field.label}

class BootStrapModelForm(BootStrap, forms.ModelForm):
    pass

class BootStrapForm(BootStrap, forms.Form):
    pass