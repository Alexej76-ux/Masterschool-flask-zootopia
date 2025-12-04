import json
def load_data(file_path):
  """ Loads a JSON file """
  with open (file_path, "r") as handle:
     return json.load(handle)
animals_data =load_data('animals_data.json')


def read_html(file_path):
  """ Load a JSON file """
  with open (file_path, "r") as handle:
     return handle.read()

def write_html(file_path):
  output =''
  html = read_html("animals_template.html")
  for animal_data in animals_data:
    output += f"Name: {animal_data['name']}\n"
    output += f"Diet: {animal_data['characteristics']['diet']}\n"
  html.replace("__REPLACE_ANIMALS_INFO__",output)
  return html

print(write_html(''))

