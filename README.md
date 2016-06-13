# django-bad-migrations
Demo project that shows django generating migrations for ever.

# Running
To see behaviour run:

`for i in {1..5}; do ./manage.py makemigrations; done`

# Cause
The file `0002_rename_model.py` does not use CamelCase when renaming the
model from `OriginalModel` to `RenamedModel`. This appears to work at first
but when `makemigrations` is subsequently run it generates `AlterField`
migrations indefinitely.